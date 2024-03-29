
# 发送rpc 调用的 代码
```bash

cat send_rpc.py

#!/usr/bin/env python
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Starter script for Cinder OS API."""

import eventlet
eventlet.monkey_patch()

import logging as python_logging
import sys

from cinder import objects

from oslo_config import cfg
from oslo_log import log as logging
from oslo_reports import guru_meditation_report as gmr
from oslo_reports import opts as gmr_opts

from cinder import i18n
i18n.enable_lazy()

# Need to register global_opts
from cinder.common import config
from cinder import rpc
from cinder import service
from cinder import utils
from cinder import version


# NOTE: cinder-api register some options of volume types
# which used to distinguish configured volume types.
# With implementation issues, register related options
# here for cinder-api, not use same configuration method
# for cinder-volume.
backend_opts = [
    cfg.StrOpt('volume_backend_name',
               help='Name override of volume backend value.'),
    cfg.StrOpt('rbd_pool',
               help='Name override of ceph pool value.')
]

CONF = cfg.CONF


def main():
    objects.register_all()
    gmr_opts.set_defaults(CONF)
    CONF(sys.argv[1:], project='cinder',
         version=version.version_string())
    config.set_middleware_defaults()
    logging.setup(CONF, "cinder")
    python_logging.captureWarnings(True)
    utils.monkey_patch()

    gmr.TextGuruMeditation.setup_autorun(version, conf=CONF)
    if CONF.enabled_backends:
        for backend in CONF.enabled_backends:
            CONF.register_opts(backend_opts, group=backend)

    rpc.init(CONF)
    # launcher = service.process_launcher()
    # server = service.WSGIService('osapi_volume')
    # launcher.launch_service(server, workers=server.workers)
    # launcher.wait()


from cinder.backend import rpcapi as backend_rpcapi

from cinder import objects

from cinder import context

if __name__=='__main__':
    main()
    ctxt = context.get_admin_context()
    # objects.register_all()
    _r = backend_rpcapi.BackendAPI()
    _r.output_message(ctxt,'topic11','hellooooooooooooooooooooooooooooooooo   rabbit')



```