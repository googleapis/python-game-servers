# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Snippet for CreateGameServerCluster
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-game-servers


# [START gameservices_v1beta_generated_GameServerClustersService_CreateGameServerCluster_sync]
from google.cloud import gaming_v1beta


def sample_create_game_server_cluster():
    # Create a client
    client = gaming_v1beta.GameServerClustersServiceClient()

    # Initialize request argument(s)
    game_server_cluster = gaming_v1beta.GameServerCluster()
    game_server_cluster.name = "name_value"

    request = gaming_v1beta.CreateGameServerClusterRequest(
        parent="parent_value",
        game_server_cluster_id="game_server_cluster_id_value",
        game_server_cluster=game_server_cluster,
    )

    # Make the request
    operation = client.create_game_server_cluster(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END gameservices_v1beta_generated_GameServerClustersService_CreateGameServerCluster_sync]
