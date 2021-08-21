# 获取之前必须 先注册

## 向 group 注册

```bash

CONF.register_opts(volume_opts, group = "normal")

```

## 直接 通过 CONF 属性访问，只会 默认寻找 DEFAULT 中的值
oslo_config.cfg.NoSuchOptError: no such option max_over_subscription_ratio in group [DEFAULT]

## 获取 非默认 group 中的值 的方法
```bash

CONF._get("normal").max_over_subscription_ratio

```