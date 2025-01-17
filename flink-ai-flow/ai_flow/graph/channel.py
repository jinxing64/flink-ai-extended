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
from typing import Text, Optional
from ai_flow.util.json_utils import Jsonable


class Channel(Jsonable):
    """ Node Object output"""

    def __init__(self,
                 node_id: Text,
                 port: Optional[int] = 0) -> None:
        """
        :param node_id: node identity id
        :param port: the index of output
        """
        super().__init__()
        self.node_id = node_id
        self.port = port


class NoneChannel(Channel):
    """ the node does not has output, identity the node"""

    def __init__(self, node_id: Text) -> None:
        super().__init__(node_id, None)
