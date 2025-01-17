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
from ai_flow.common.properties import Properties
from ai_flow.util.json_utils import Jsonable


class ArtifactMeta(Jsonable):
    """define artifact meta """

    def __init__(self,
                 name: Text,
                 data_format: Text,
                 description: Text = None,
                 batch_uri: Text = None,
                 stream_uri: Text = None,
                 create_time: int = None,
                 update_time: int = None,
                 properties: Properties = None,
                 uuid: int = None) -> None:
        """ create artifact meta
        Args:
            name: artifact name
            data_format: csv, json, etc.
            description: artifact description
            batch_uri: batch data persistent storage
            stream_uri: stream data persistent storage
            create_time: create artifact datetime
            update_time: update artifact datetime
            properties: properties for the artifact
        """
        self.name = name
        self.data_format = data_format
        self.description = description
        self.batch_uri = batch_uri
        self.stream_uri = stream_uri
        self.create_time = create_time
        self.update_time = update_time
        self.properties = properties
        self.uuid = uuid


# artifact api
def create_artifact(name: Text,
                    data_format: Text = None,
                    description: Text = None,
                    batch_uri: Text = None,
                    stream_uri: Text = None,
                    create_time: int = None,
                    update_time: int = None,
                    properties: Properties = None) -> ArtifactMeta:
    return ArtifactMeta(name, data_format, description, batch_uri, stream_uri,
                        create_time, update_time, properties)
