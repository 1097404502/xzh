# Copyright 2012, Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Client side of the scheduler manager RPC API.
"""

from oslo_config import cfg
from oslo_serialization import jsonutils
from cinder.volume import utils

from cinder import rpc


CONF = cfg.CONF


class BackendAPI(rpc.RPCAPI):
    """Client side of the scheduler rpc API.

    API version history:

    .. code-block:: none

        1.0 - Initial version.
        1.1 - Add create_volume() method
        1.2 - Add request_spec, filter_properties arguments to
              create_volume()
        1.3 - Add migrate_volume_to_host() method
        1.4 - Add retype method
        1.5 - Add manage_existing method
        1.6 - Add create_consistencygroup method
        1.7 - Add get_active_pools method
        1.8 - Add sending object over RPC in create_consistencygroup method
        1.9 - Adds support for sending objects over RPC in create_volume()
        1.10 - Adds support for sending objects over RPC in retype()
        1.11 - Adds support for sending objects over RPC in
               migrate_volume_to_host()

        ... Mitaka supports messaging 1.11. Any changes to existing methods in
        1.x after this point should be done so that they can handle version cap
        set to 1.11.

        2.0 - Remove 1.x compatibility
    """

    RPC_API_VERSION = '2.0'
    TOPIC = CONF.backend_topic
    BINARY = 'cinder-backend'

    def _compat_ver(self, current, legacy):
        if self.client.can_send_version(current):
            return current
        else:
            return legacy


    def update_service_capabilities(self, ctxt,
                                    service_name, host,
                                    capabilities):
        # FIXME(flaper87): What to do with fanout?
        version = self._compat_ver('2.0', '1.0')
        cctxt = self.client.prepare(fanout=True, version=version)
        cctxt.cast(ctxt, 'update_service_capabilities',
                   service_name=service_name, host=host,
                   capabilities=capabilities)

    def output_message(self, ctxt, topic,message):
        version = self._compat_ver('2.0', '1.0')
        cctxt = self.client.prepare(version=version)
        message_args = {
            'topic':topic,
            'message':message
        }
        cctxt.cast(ctxt, 'output_message',**message_args)