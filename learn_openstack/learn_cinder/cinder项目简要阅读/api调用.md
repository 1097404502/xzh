# openstacl 中的 api 类型
在openstack中不管程序内部之间的调用还是，对于openstack中的各种服务的和功能的内部调用，还是外部调用都是通过api的形式来进行的。这里分析一下openstack中的几种常见api类型。

# 1.第一种是程序内部的api主要是给本机程序内部使用，
如nova_master/nova/compute/api.py文件中的api class主要是为了给manager去调用，其中调用哪个api class也是利用openstack中非常重要的动态载入方法来确定的，非常灵活，我认为这种用法非常向c#，c++这类语言中的面向接口编程，甚至更为灵活，充分利用了动态语言的优点。

# 2. 一种api是rpc api，就是通过高级消息队列的方式，实现不同主机的方法的远程调用。
如nova_master/nova/compute/rpcapi.py，其中调用的方法都是manager中的方法。通过rpc的方式是实现分布式程序的基本方法，采用消息队列的rpc方式是目前流行的多种云计算框架实现的普遍方式。

# 3. 另一种api就是通过web资源的方式暴露给外界的api，将提供的服务暴露成web资源，可以方便外界的访问
openstack是同过起一个对应一类api的WSGIService服务来实现对外的服务。

再一种api就是client api，是对web api的封装，提供这种形式的api主要是方便用户对复杂的web资源形式的api的调用，简化了操作，便于用户通过程序调用。

