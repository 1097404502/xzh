

# recive manager 接收消息的 manager
```bash


import oslo_messaging as messaging
from oslo_log import log as logging


from cinder import manager
from cinder import objects
from cinder import context
from cinder import exception


from cinder.i18n import _, _LE, _LI, _LW
from cinder.volume import utils as vol_utils

LOG = logging.getLogger(__name__)


class BackendManager(manager.Manager):
    """Manages backend process."""

    RPC_API_VERSION = '2.0'

    target = messaging.Target(version=RPC_API_VERSION)

    # host like node01@backend-db02abac-e464
    def __init__(self, volume_driver=None, service_name=None,
                 *args, **kwargs):
        """Load the driver from the one specified in args, or from flags."""

        super(BackendManager, self).__init__(*args, **kwargs)

    def init_host(self):
        pass

    def init_host_with_rpc(self):
        pass

    def output_message(self, context, topic, message):
        print('recive: %s, %s ' % (topic, message) )


```