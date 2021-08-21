# 无法并发
2021-02-09 19:16:04.274 1968849 WARNING oslo.messaging._drivers.impl_rabbit [req-601018ee-e36c-4858-9e6f-440cb44cd4bc - - - - -] Process forked after connection established! This can result in unpredictable behavior. See: http://docs.openstack.org/developer/oslo.messaging/transport.html
2021-02-09 19:16:04.276 1968849 ERROR oslo.messaging._drivers.impl_rabbit [req-601018ee-e36c-4858-9e6f-440cb44cd4bc - - - - -] Failed to publish message to topic 'cinder-scheduler_fanout': Basic.publish: (505) UNEXPECTED_FRAME - expected content body, got non content body frame instead
2021-02-09 19:16:04.276 1951240 ERROR oslo.messaging._drivers.impl_rabbit [req-601018ee-e36c-4858-9e6f-440cb44cd4bc - - - - -] AMQP server 192.168.40.10:5672 closed the connection. Check login credentials: Socket closed
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task [req-601018ee-e36c-4858-9e6f-440cb44cd4bc - - - - -] Error during VolumeManager._publish_service_capabilities
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task Traceback (most recent call last):
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_service/periodic_task.py", line 220, in run_periodic_tasks
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     task(self, context)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/cinder/manager.py", line 173, in _publish_service_capabilities
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.last_capabilities)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/cinder/scheduler/rpcapi.py", line 168, in update_service_capabilities
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     capabilities=capabilities)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 135, in cast
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.transport._send(self.target, ctxt, msg, retry=self.retry)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/transport.py", line 91, in _send
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     timeout=timeout, retry=retry)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 470, in send
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     retry=retry)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/amqpdriver.py", line 444, in _send
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     conn.fanout_send(target.topic, msg, retry=retry)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1242, in fanout_send
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self._ensure_publishing(self._publish, exchange, msg, retry=retry)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1111, in _ensure_publishing
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.ensure(method, retry=retry, error_callback=_error_callback)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 758, in ensure
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     ret, channel = autoretry_method()
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/connection.py", line 436, in _ensured
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     return fun(*args, **kwargs)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/connection.py", line 508, in __call__
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     return fun(*args, channel=channels[0], **kwargs), channels[0]
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 734, in execute_method
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     method()
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/oslo_messaging/_drivers/impl_rabbit.py", line 1130, in _publish
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     routing_key=routing_key)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/messaging.py", line 85, in __init__
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.revive(self._channel)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/messaging.py", line 222, in revive
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.declare()
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/messaging.py", line 105, in declare
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.exchange.declare()
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/kombu/entity.py", line 174, in declare
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     nowait=nowait, passive=passive,
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/channel.py", line 622, in exchange_declare
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     (40, 11),  # Channel.exchange_declare_ok
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/abstract_channel.py", line 67, in wait
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     self.channel_id, allowed_methods, timeout)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/connection.py", line 274, in _wait_method
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     wait()
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/abstract_channel.py", line 69, in wait
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     return self.dispatch_method(method_sig, args, content)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/abstract_channel.py", line 87, in dispatch_method
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     return amqp_method(self, args)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task   File "/usr/lib/python2.7/site-packages/amqp/connection.py", line 530, in _close
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task     (class_id, method_id), ConnectionError)
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task UnexpectedFrame: Basic.publish: (505) UNEXPECTED_FRAME - expected content body, got non content body frame instead
2021-02-09 19:16:04.277 1968849 ERROR oslo_service.periodic_task


Make _send_method() deliver frames contiguously, resolving issue 507 

Ensure frames can not be interspersed on send


grep "_send_method()" -r /usr/lib/python2.7/site-packages/amqp

grep "_send_method()" -r /root/cinder/.tox/py27/lib/python2.7/site-packages/amqp



 File "/usr/lib/python2.7/site-packages/cinder/scheduler/rpcapi.py", line 168, in update_service_capabilities


# 导致报错的原因
multiprocessing 建立在 fork 的基础上
打开了多个 rabbit 连接之后。某些定时任务 造成了冲突。

#  python 判断当前进程是不是 主进程

# 查看 消息队列状态
systemctl  restart rabbitmq-server.service
systemctl status rabbitmq-server.service

# 创建云硬盘失败
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo_messaging/rpc/dispatcher.py", line 138, in _dispatch_and_reply
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher     incoming.message))
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo_messaging/rpc/dispatcher.py", line 185, in _dispatch
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher     return self._do_dispatch(endpoint, method, ctxt, args)
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo_messaging/rpc/dispatcher.py", line 127, in _do_dispatch
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 657, in create_volume
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher     _run_flow()
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 645, in _run_flow
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher     raise ex
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Image already exists.
2021-02-09 20:29:37.009 7975 ERROR oslo_messaging.rpc.dispatcher