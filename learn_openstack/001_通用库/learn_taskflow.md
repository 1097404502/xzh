
# taskflow 官方文档

https://docs.openstack.org/taskflow/latest/

```bash

```

# taskflow create_volume 详细流程
taskflow  基本属于 cinder 最 难读 的 模块, 对于 提升 编码 设计 水平, 也大有 帮助 ( 也许吧 )

首先 从 url 开始 
1. http://{{server_ip}}:8776/v2/{{project_id}}/volumes
1. cinder/api/v2/volumes : VolumeController.create 
2. 调用 volume/api.py:API.create
   在 def create 中 就开始了 taskflow 的 构建 与 执行.

## 准备 taskflow 所需要的 必要函数 与 store

得到 需要 执行的 flow_engine
但是 此处的 get_flow 是经过 业务 封装的 并不满足, 通用性
```bash

create_what = {
    'context': context,
    'raw_size': size,
    'name': name,
    'description': description,
    'snapshot': snapshot,
    'image_id': image_id,
    'raw_volume_type': volume_type,
    'metadata': metadata or {},
    'raw_availability_zone': availability_zone,
    'source_volume': source_volume,
    'scheduler_hints': scheduler_hints,
    'key_manager': self.key_manager,
    'optional_args': {'is_quota_committed': False},
    'consistencygroup': consistencygroup,
    'cgsnapshot': cgsnapshot,
    'multiattach': multiattach,
    'is_sys_vol': is_sys_vol,
    'share': share,
    'user_id': user_id,
    'flatten': flatten,
    'cluster_id': volume_type.get('cluster_id')
}
try:
    sched_rpcapi = (self.scheduler_rpcapi if (not cgsnapshot and
                    not source_cg) else None)
    volume_rpcapi = (self.volume_rpcapi if (not cgsnapshot and
                      not source_cg) else None)
    flow_engine = create_volume.get_flow(self.db,
                                          self.image_service,
                                          availability_zones,
                                          create_what,
                                          sched_rpcapi,
                                          volume_rpcapi)

``` 

## 查看 create_volue.get_flow

此 函数 内 直接 调用的 通用的 taskflow linear_flow.Flow

这是一个 线性flow 所有的 步骤 顺序 完成
return taskflow.engines.load(scheduler_flow, store=create_what)

scheduler_flow 包含了 所有 需要 顺序 执行的 所有类
这这些 需要 执行的 类 都包含了 __init__   _handle_failure  _notify_failure 以及 关键的 execute 函数.
其中 __init__ 返回了 flow 包含的 每个 需要 执行的 任务 实例,
engine.run 函数 会 运行 所有 任务 实例的 execute 函数.

store 中 则 包含 了 所有的 execute 函数 所需要的 参数

```bash
def get_flow(context, db_api, driver_api, request_spec=None,
             filter_properties=None,
             volume=None, snapshot_id=None, image_id=None):

    """Constructs and returns the scheduler entrypoint flow.

    This flow will do the following:

    1. Inject keys & values for dependent tasks.
    2. Extract a scheduler specification from the provided inputs.
    3. Use provided scheduler driver to select host and pass volume creation
       request further.
    """
    create_what = {
        'context': context,
        'raw_request_spec': request_spec,
        'filter_properties': filter_properties,
        'volume': volume,
        'snapshot_id': snapshot_id,
        'image_id': image_id,
    }

    flow_name = ACTION.replace(":", "_") + "_scheduler"
    scheduler_flow = linear_flow.Flow(flow_name)

    # This will extract and clean the spec from the starting values.
    scheduler_flow.add(ExtractSchedulerSpecTask(
        db_api,
        rebind={'request_spec': 'raw_request_spec'}))

    # This will activate the desired scheduler driver (and handle any
    # driver related failures appropriately).
    scheduler_flow.add(ScheduleCreateVolumeTask(db_api, driver_api))

    # Now load (but do not run) the flow using the provided initial data.
    return taskflow.engines.load(scheduler_flow, store=create_what)

```

