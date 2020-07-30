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

"""Google Cloud Game Servers sample for listing game server clusters.

Example usage:
    python list_clusters.py --project-id <project-id> --location <location> --realm-id <realm-id>
"""

import argparse

from google.cloud import gaming


# [START cloud_game_servers_cluster_list]
def list_clusters(project_id, location, realm_id):
    """Lists the existing game server clusters."""

    client = gaming.GameServerClustersServiceClient()

    response = client.list_game_server_clusters(
        parent=f"projects/{project_id}/locations/{location}/realms/{realm_id}"
    )

    for cluster in response.game_server_clusters:
        print(f"Name: {cluster.name}")

    return response.game_server_clusters
# [END cloud_game_servers_cluster_list]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--location', help='Your realm location.', required=True)
    parser.add_argument('--realm-id', help='Your realm ID.', required=True)

    args = parser.parse_args()

    list_clusters(args.project_id, args.location, args.realm_id)
