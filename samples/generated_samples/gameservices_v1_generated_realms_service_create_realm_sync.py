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
# Snippet for CreateRealm
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-game-servers


# [START gameservices_v1_generated_RealmsService_CreateRealm_sync]
from google.cloud import gaming_v1


def sample_create_realm():
    # Create a client
    client = gaming_v1.RealmsServiceClient()

    # Initialize request argument(s)
    realm = gaming_v1.Realm()
    realm.time_zone = "time_zone_value"

    request = gaming_v1.CreateRealmRequest(
        parent="parent_value",
        realm_id="realm_id_value",
        realm=realm,
    )

    # Make the request
    operation = client.create_realm(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END gameservices_v1_generated_RealmsService_CreateRealm_sync]