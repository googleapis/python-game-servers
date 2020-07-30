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

"""Google Cloud Game Servers sample for getting a game server config.

Example usage:
    python get_config.py --project-id <project-id> --deployment-id <deployment-id> --config-id <config-id>
"""

import argparse

from google.cloud import gaming
from google.cloud.gaming_v1.types import game_server_configs


# [START cloud_game_servers_config_get]
def get_config(project_id, deployment_id, config_id):
    """Gets a game server config."""

    client = gaming.GameServerConfigsServiceClient()

    # Location is hard coded as global, as game server configs can
    # only be created in global.  This is done for all operations on
    # game server configs.
    request = game_server_configs.GetGameServerConfigRequest(
        name=f"projects/{project_id}/locations/global/gameServerDeployments/{deployment_id}/configs/{config_id}",
    )

    response = client.get_game_server_config(request)
    print(f"Get config response:\n{response}")
    return response
# [END cloud_game_servers_config_get]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--deployment-id', help='Your game server deployment ID.', required=True)
    parser.add_argument('--config-id', help='Your game server config ID.', required=True)

    args = parser.parse_args()

    get_config(args.project_id, args.config_id, args.deployment_id)
