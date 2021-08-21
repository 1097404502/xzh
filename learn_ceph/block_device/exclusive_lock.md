# 排他锁
排他锁 ，在每个 images 被挂载到 客户机上的时候，都会启用。
当任何 客户机被 正常使用的时候，正常删除的时候，排他锁 都会得到正常的释放。

***** 特殊情况下。 例如，断电，物理服务器 宕机，那么 排他锁 可能 得不到很好的释放。

可以采用以下方式打破限制。
1. the Mon instructs the relevant OSDs to no longer serve requests from the old client process;

2. 采用 快备份 images，在新的 images 上进行操作