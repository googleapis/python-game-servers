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

"""Google Cloud Game Servers sample for listing game server configs.

Example usage:
    python list_configs.py --project-id <project-id>  --deployment-id <deployment-id>
"""

import argparse

from google.cloud import gaming


# [START cloud_game_servers_config_list]
def list_configs(project_id, deployment_id):
    """Lists the existing game server deployments."""

    client = gaming.GameServerConfigsServiceClient()

    # Location is hard coded as global, as game server configs can
    # only be created in global.  This is done for all operations on
    # game server configs.
    response = client.list_game_server_configs(
        parent=f"projects/{project_id}/locations/global/gameServerDeployments/{deployment_id}"
    )

    for config in response.game_server_configs:
        print(f"Name: {config.name}")

    return response.game_server_configs
# [END cloud_game_servers_config_list]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--deployment-id', help='Your game server deployment ID.', required=True)

    args = parser.parse_args()

    list_configs(args.project_id, args.deployment_id)
