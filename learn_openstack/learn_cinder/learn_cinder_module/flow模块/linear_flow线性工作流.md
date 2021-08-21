# 线性工作流 介绍
线性工作流 中下一个任务必须等待上一个任务被完成，才可以 执行下一个任务

# 我们来看一下 openstack 提供的 linear_flow 的一个实际 demo
这个 flow 的作用就是 创建一个 volume 。

官方注释 写的很明白，得到 执行 以下 6个步骤的 工作流。

api_flow = linear_flow.Flow(flow_name)
这句话就类似于 我们之前 讲异步提到的 job_list[] 空列表

之后    api_flow.add(QuotaReserveTask(),
                 EntryCreateTask(db_api),
                 QuotaCommitTask())
就是给这个 空列表中 按照任务顺序添加 需要被执行的任务。

更棒的地方在于，我们之前的课程中，是自己 循环 启动了一个个 异步任务。
但是 api_flow 自身就拥有 run 方法

run 中的 flow_engine 就是 通过 get_flow 方法得到的，他会保证 linear_flow 中的任务,得到 **"异步的启动，并保证 有序的执行"**

我们要理解  "异步的启动，并保证 有序的执行"
如果我们单纯 需要 有序执行，我们只是 f1();f2();f3(); 即可
但是 f1, f2 ,本身 很可能 并不是 计算 密集型操作，他们并不比阻塞 cpu。
所以我们要 "异步的启动，并保证 有序的执行"

```bash
with flow_utils.DynamicLogListener(flow_engine, logger=LOG):
  flow_engine.run()
  vref = flow_engine.storage.fetch('volume')
  LOG.info(_LI("Volume created successfully."), resource=vref)
  return vref
```

get_flow
```python
def get_flow(db_api, image_service_api, availability_zones, create_what,
             scheduler_rpcapi=None, volume_rpcapi=None):
    """Constructs and returns the api entrypoint flow.

    This flow will do the following:

    1. Inject keys & values for dependent tasks.
    2. Extracts and validates the input keys & values.
    3. Reserves the quota (reverts quota on any failures).
    4. Creates the database entry.
    5. Commits the quota.
    6. Casts to volume manager or scheduler for further processing.
    """

    # ACTION = 'volume:create'
    flow_name = ACTION.replace(":", "_") + "_api"
    api_flow = linear_flow.Flow(flow_name)

    api_flow.add(ExtractVolumeRequestTask(
        image_service_api,
        availability_zones,
        rebind={'size': 'raw_size',
                'availability_zone': 'raw_availability_zone',
                'volume_type': 'raw_volume_type'}))
    api_flow.add(QuotaReserveTask(),
                 EntryCreateTask(db_api),
                 QuotaCommitTask())

    if scheduler_rpcapi and volume_rpcapi:
        # This will cast it out to either the scheduler or volume manager via
        # the rpc apis provided.
        api_flow.add(VolumeCastTask(scheduler_rpcapi, volume_rpcapi, db_api))

    # Now load (but do not run) the flow using the provided initial data.
    return taskflow.engines.load(api_flow, store=create_what)
```