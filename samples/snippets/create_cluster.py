#!/usr/bin/env python

# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Game Servers sample for creating a game server cluster.

Example usage:
    python create_cluster.py --project-id <project-id> --location <location>
        --realm-id <realm-id> --cluster-id <cluster-id> --gke-cluster-name <gke-cluster-name>
"""

import argparse

from google.cloud import gaming
from google.cloud.gaming_v1.types import game_server_clusters


# [START cloud_game_servers_cluster_create]
def create_cluster(project_id, location, realm_id, cluster_id, gke_cluster_name):
    """Creates a game server cluster."""

    client = gaming.GameServerClustersServiceClient()

    gke_cluster_reference = game_server_clusters.GkeClusterReference(
        cluster=gke_cluster_name,
    )
    request = game_server_clusters.CreateGameServerClusterRequest(
        parent=f"projects/{project_id}/locations/{location}/realms/{realm_id}",
        game_server_cluster_id=cluster_id,
        game_server_cluster=game_server_clusters.GameServerCluster(
            description="My Game Server Cluster",
            connection_info=game_server_clusters.GameServerClusterConnectionInfo(
                gke_cluster_reference=gke_cluster_reference,
                namespace="default",
            ),
        ),
    )

    operation = client.create_game_server_cluster(request)
    print(f"Create cluster operation: {operation.operation.name}")
    operation.result(timeout=120)
# [END cloud_game_servers_cluster_create]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--location', help='Your realm location.', required=True)
    parser.add_argument('--realm-id', help='Your realm ID.', required=True)
    parser.add_argument('--cluster-id', help='Your game server cluster ID.', required=True)
    parser.add_argument(
        '--gke-cluster-name',
        help='The name of the GKE cluster which is managed by the game server cluster being created.',
        required=True)

    args = parser.parse_args()

    create_cluster(args.project_id, args.location, args.realm_id, args.cluster_id, args.gke_cluster_name)
