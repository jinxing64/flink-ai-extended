#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from typing import Text
import logging
from ai_flow.util.json_utils import Jsonable
from ai_flow.deployer.listener import register_job_status_listener, BaseJobStatusListener
from ai_flow.workflow.job_handler import BaseJobHandler

AbstractJobHandler = BaseJobHandler
AbstractJobStatusListener = BaseJobStatusListener


class AbstractPlatform(Jsonable):
    """
    ai flow job must run on one platform, such as local k8s etc.
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def platform() -> Text:
        """
        :return platform name:
        """
        raise NotImplementedError("not implement platform")

    @staticmethod
    def job_status_listener() -> type(AbstractJobStatusListener):
        """
        :return AbstractJobStatusListener class:
        """
        raise NotImplementedError("not implement AbstractJobStatusListener")


def register_platform(platform: type(AbstractPlatform)):
    logging.debug('register platform {}'.format(platform.platform()))
    register_job_status_listener(platform.job_status_listener()())
