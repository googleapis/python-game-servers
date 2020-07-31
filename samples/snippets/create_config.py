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

"""Google Cloud Game Servers sample for creating a game server config.

Example usage:
    python create_config.py --project-id <project-id> --deployment-id <deployment-id> --config-id <config-id>
"""

import argparse

from google.cloud import gaming
from google.cloud.gaming_v1.types import game_server_configs

# [START cloud_game_servers_config_create]

# FLEET_SPEC is the spec portion of an agones Fleet.  It must be in JSON format.
# See https://agones.dev/site/docs/reference/fleet/ for more on fleets.
FLEET_SPEC = """
{
   "replicas": 10,
   "scheduling": "Packed",
   "strategy": {
      "type": "RollingUpdate",
      "rollingUpdate": {
         "maxSurge": "25%",
         "maxUnavailable": "25%"
      }
   },
   "template": {
      "metadata": {
         "labels": {
            "gameName": "udp-server"
         }
      },
      "spec": {
         "ports": [
            {
               "name": "default",
               "portPolicy": "Dynamic",
               "containerPort": 2156,
               "protocol": "TCP"
            }
         ],
         "health": {
            "initialDelaySeconds": 30,
            "periodSeconds": 60
         },
         "sdkServer": {
            "logLevel": "Info",
            "grpcPort": 9357,
            "httpPort": 9358
         },
         "template": {
            "spec": {
               "containers": [
                  {
                     "name": "dedicated",
                     "image": "gcr.io/agones-images/udp-server:0.17",
                     "imagePullPolicy": "Always",
                     "resources": {
                        "requests": {
                           "memory": "200Mi",
                           "cpu": "500m"
                        },
                        "limits": {
                           "memory": "200Mi",
                           "cpu": "500m"
                        }
                     }
                  }
               ]
            }
         }
      }
   }
}
"""


def create_config(project_id, deployment_id, config_id):
    """Creates a game server config."""

    client = gaming.GameServerConfigsServiceClient()

    fleet_config = game_server_configs.FleetConfig(
        name="my-fleet-spec", fleet_spec=FLEET_SPEC,
    )

    # Location is hard coded as global, as game server configs can
    # only be created in global.  This is done for all operations on
    # game server configs.
    request = game_server_configs.CreateGameServerConfigRequest(
        parent=f"projects/{project_id}/locations/global/gameServerDeployments/{deployment_id}",
        config_id=config_id,
        game_server_config=game_server_configs.GameServerConfig(
            description="My Game Server Config", fleet_configs=[fleet_config],
        ),
    )

    operation = client.create_game_server_config(request)
    print(f"Create config operation: {operation.operation.name}")
    operation.result(timeout=120)


# [END cloud_game_servers_config_create]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id", help="Your cloud project ID.", required=True)
    parser.add_argument(
        "--deployment-id", help="Your game server deployment ID.", required=True
    )
    parser.add_argument(
        "--config-id", help="Your game server config ID.", required=True
    )

    args = parser.parse_args()

    create_config(args.project_id, args.deployment_id, args.config_id)
