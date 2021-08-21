 

# 切换到 稳定的 victoria 版本
```bash
git clone https://opendev.org/openstack/cinder.git

git checkout remotes/origin/stable/victoria


sed  "s/^flake8-logging-format/# flake8-logging-format /"    ./test-requirements.txt

sed -i  "s/^flake8-logging-format/# flake8-logging-format /"    ./test-requirements.txt




/root/cinder/.tox/pep8/bin/python -m pip install \
                        nose \
                        -r requirements.txt \
                        -r  test-requirements.txt \
                        --trusted-host mirrors.cloud.aliyuncs.com  \
                        --trusted-host pypi.org


Ignoring importlib-metadata: markers 'python_version < "3.8"' don't match your environment
ERROR: Could not find a version that satisfies the requirement test-requirements.txt (from versions: none)
ERROR: No matching distribution found for test-requirements.txt


```


# python 必须 小于 3.8
```bash

/root/app/python3710/bin/python3
rm -rf ~/env_py3
/root/app/python3710/bin/python3 -m venv ~/env_py3

source ~/env_py3/bin/activate

```

# psycopg2 报错
```bash

sed "s/psycopg2>/psycopg2-binary>/" test-requirements.txt

sed -i "s/psycopg2>/psycopg2-binary>/" test-requirements.txt

```
# 生成 配置
```bash

# 漫长等待
/root/env_py3/bin/tox -egenconfig

```
