
#  nova 元数据 /var/lib/nova
```bash

grep 'error' -r /var/lib/nova/
Binary file /var/lib/nova/instances/virtio-win.vfd matches
/var/lib/nova/instances/6abe9bd0-0d55-4e0d-9c5e-d7c0aa181b30/console.log:2021-06-04 17:50:58.428 4788 ERROR cloudbaseinit.init [-] plugin 'SetUserSSHPublicKeysPlugin' failed with error '[WinError 2] 系统找不到指定的文件。': FileNotFoundError: [WinError 2] 系统找不到指定的文件。
/var/lib/nova/instances/6abe9bd0-0d55-4e0d-9c5e-d7c0aa181b30/console.log:2021-06-04 17:51:01.084 4788 ERROR cloudbaseinit.init [-] plugin 'ConfigWinRMListenerPlugin' failed with error '(-2147023143, '终结点映射器中没有更多的终结点可用。', None, None)': pywintypes.com_error: (-2147023143, '终结点映射器中没有更多的终结点可用。', None, None)
/var/lib/nova/instances/6abe9bd0-0d55-4e0d-9c5e-d7c0aa181b30/console.log:2021-06-04 17:51:01.100 4788 ERROR cloudbaseinit.init [-] (-2147023143, '终结点映射器中没有更多的终结点可用。', None, None): pywintypes.com_error: (-2147023143, '终结点映射器中没有更多的终结点可用。', None, None)
/var/lib/nova/instances/6abe9bd0-0d55-4e0d-9c5e-d7c0aa181b30/console.log:2021-06-04 17:51:01.100 4788 ERROR cloudbaseinit.init pywintypes.com_error: (-2147221021, '操作无法使用', None, None)
/var/lib/nova/instances/6abe9bd0-0d55-4e0d-9c5e-d7c0aa181b30/console.log:2021-06-04 17:51:01.100 4788 ERROR cloudbaseinit.init pywintypes.com_error: (-2147023143, '终结点映射器中没有更多的终结点可用。', None, None)
-
```
