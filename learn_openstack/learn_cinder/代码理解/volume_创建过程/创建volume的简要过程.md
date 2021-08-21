
# 创建 过程
1. v2/volume/api  create
2. cinder/volume/api create
3. scheduler_rpcapi

```bash

```


# 创建顺序
1. web 或者 cinderclint 提交 volume_create 请求
2. 请求 会被 url 到 api 映射到以下函数
 /root/cinder/cinder/volume/api.py:218 def create 
    def create(self, context, size, name, description, snapshot=None,
               image_id=None, volume_type=None, metadata=None,
               availability_zone=None, source_volume=None,
               scheduler_hints=None,
               source_replica=None, consistencygroup=None,
               cgsnapshot=None, multiattach=False, source_cg=None):

  1. 参数检查
      其中检查参数的 格式合法性， 也会检查 资源存量 是否足够。
```bash
# 参数检查内容很多，列举一个
if size and (not strutils.is_int_like(size) or int(size) <= 0):
    msg = _('Invalid volume size provided for create request: %s '
            '(size argument must be an integer (or string '
            'representation of an integer) and greater '
            'than zero).') % size
    raise exception.InvalidInput(reason=msg)

```

  2. 通过之后，创建 sched_rpcapi volume_rpcapi  flow_engine

其中 /root/cinder/cinder/volume/rpcapi.py:35 volume_rpcapi  中有更加详细的创建过程
```python
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

  3. 执行 flow_engine 创建 volume

```python
# Attaching this listener will capture all of the notifications that
# taskflow sends out and redirect them to a more useful log for
# cinders debugging (or error reporting) usage.
with flow_utils.DynamicLogListener(flow_engine, logger=LOG):
    flow_engine.run()
    vref = flow_engine.storage.fetch('volume')
    LOG.info(_LI("Volume created successfully."), resource=vref)
    return vref
```


  4. 返回 vref ，volume 对象的ref(引用对象)



# volume_rpc_api 创建 volume 过程
```bash

def create_volume(self, ctxt, volume, host, request_spec,
                  filter_properties, allow_reschedule=True):
    request_spec_p = jsonutils.to_primitive(request_spec)
    msg_args = {'volume_id': volume.id, 'request_spec': request_spec_p,
                'filter_properties': filter_properties,
                'allow_reschedule': allow_reschedule}
    if self.client.can_send_version('2.0'):
        version = '2.0'
        msg_args['volume'] = volume
    elif self.client.can_send_version('1.32'):
        version = '1.32'
        msg_args['volume'] = volume
    else:
        version = '1.24'

    cctxt = self._get_cctxt(host, version)
    request_spec_p = jsonutils.to_primitive(request_spec)
    """Invoke a method and return immediately. See RPCClient.cast()."""
    cctxt.cast(ctxt, 'create_volume', **msg_args)

# 实际上 到此为止 创建服务就是 cctxt 向消息队列提供了一个任务
-->
self.transport._send(self.target, ctxt, msg, retry=self.retry)


```


## 判断 list 或者 map 中是否 有哪些键名
```bash
# Check that the required keys are present, return an error if they
# are not.
required_keys = set(['ref', 'host'])
missing_keys = list(required_keys - set(volume.keys()))

if missing_keys:
    # 代表 这些 键名 不全部存在
    msg = _("The following elements are required: %s") % \
        ', '.join(missing_keys)
    raise exc.HTTPBadRequest(explanation=msg)

```