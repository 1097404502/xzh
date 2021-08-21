# 从 41 上收集 cmd 输出
```bash

scp root@192.168.39.1:/root/codes/collect_out/ceph_v10_outbuf.gz  /home/lmk/essay/job/codes/

scp root@192.168.41.1:/root/codes/collect_out/ceph_v14_outbuf.gz  /home/lmk/essay/job/codes/

```

# 将 cmd 输出 发送到 开发机
```bash
scp /home/lmk/essay/job/codes/ceph_v14_outbuf.gz root@192.168.19.10:/root/cinder/cinder/tests/unit/ceph/cmd_data/
scp /home/lmk/essay/job/codes/ceph_v10_outbuf.gz root@192.168.19.10:/root/cinder/cinder/tests/unit/ceph/cmd_data/
```