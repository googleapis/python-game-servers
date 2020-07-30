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

"""Google Cloud Game Servers sample for deleting a game server deployment.

Example usage:
    python delete_deployment.py --project-id <project-id> --deployment-id <deployment-id>
"""

import argparse

from google.cloud import gaming
from google.cloud.gaming_v1.types import game_server_deployments


# [START cloud_game_servers_deployment_delete]
def delete_deployment(project_id, deployment_id):
    """Deletes a game server deployment."""

    client = gaming.GameServerDeploymentsServiceClient()

    # Location is hard coded as global, as game server deployments can
    # only be created in global.  This is done for all operations on
    # game server deployments, as well as for its child resource types.
    request = game_server_deployments.DeleteGameServerDeploymentRequest(
        name=f"projects/{project_id}/locations/global/gameServerDeployments/{deployment_id}",
    )

    operation = client.delete_game_server_deployment(request)
    print(f"Delete deployment operation: {operation.operation.name}")
    operation.result(timeout=120)
# [END cloud_game_servers_deployment_delete]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--deployment-id', help='Your game server deployment ID.', required=True)

    args = parser.parse_args()

    delete_deployment(args.project_id, args.deployment_id)
