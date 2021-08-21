

# 主要步骤
1. 准备 开发 环境
  - 1. 制作 zcloud 镜像
  - 2. 利用 虚拟机 快速搭建 研发环境
  - 3. 搭建 一个 zcloud
  - 4. 搭建 一个 ceph
  - 5. 相互 认证 准备
2. cluster 开发
   - 1. 定义 cluster, ClusterExtraSpecs结构体, 编写version迁移文件 , 对数据库进行 升级.
   - 2. create api 以及 cli, 能够 在 命令行 以及 api 接口 创建 cluster. 
   - 3. 能够 查看 指定 cluster 的 状态( ceph -s ).
   - 3. next 先完成 以上工作.