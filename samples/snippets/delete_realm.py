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

"""Google Cloud Game Servers sample for deleting a realm.

Example usage:
    python delete_realm.py --project-id <project-id> --location --realm-id <realm-id>
"""

import argparse

from google.cloud import gaming
from google.cloud.gaming_v1.types import realms


# [START cloud_game_servers_realm_delete]
def delete_realm(project_id, location, realm_id):
    """Deletes a realm."""

    client = gaming.RealmsServiceClient()

    request = realms.DeleteRealmRequest(
        name=f"projects/{project_id}/locations/{location}/realms/{realm_id}",
    )

    operation = client.delete_realm(request)
    print(f"Delete realm operation: {operation.operation.name}")
    operation.result(timeout=120)


# [END cloud_game_servers_realm_delete]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id", help="Your cloud project ID.", required=True)
    parser.add_argument("--location", help="Your realm location.", required=True)
    parser.add_argument("--realm-id", help="Your realm ID.", required=True)

    args = parser.parse_args()

    delete_realm(args.project_id, args.location, args.realm_id)
