# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for PreviewDeleteGameServerCluster
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-game-servers


# [START gameservices_generated_gaming_v1_GameServerClustersService_PreviewDeleteGameServerCluster_async]
from google.cloud import gaming_v1


async def sample_preview_delete_game_server_cluster():
    # Create a client
    client = gaming_v1.GameServerClustersServiceAsyncClient()

    # Initialize request argument(s)
    request = gaming_v1.PreviewDeleteGameServerClusterRequest(
        name="name_value",
    )

    # Make the request
    response = await client.preview_delete_game_server_cluster(request=request)

    # Handle response
    print(response)

# [END gameservices_generated_gaming_v1_GameServerClustersService_PreviewDeleteGameServerCluster_async]
