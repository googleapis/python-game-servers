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

"""Google Cloud Game Servers sample for listing realms.

Example usage:
    python list_realms.py --project-id <project-id> --location <location>
"""

import argparse

from google.cloud import gaming

# [START cloud_game_servers_realm_list]


def list_realms(project_id, location):
    """Lists the existing realms."""

    client = gaming.RealmsServiceClient()

    response = client.list_realms(
        parent=f"projects/{project_id}/locations/{location}"
    )

    for realm in response.realms:
        print(f"Name: {realm.name}")

    return response.realms
# [END cloud_game_servers_realm_list]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', help='Your cloud project ID.', required=True)
    parser.add_argument('--location', help='Your realm location.', required=True)

    args = parser.parse_args()

    list_realms(args.project_id, args.location)
