# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
# Snippet for DeleteRealm
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-game-servers


# [START gameservices_generated_gaming_v1beta_RealmsService_DeleteRealm_async]
from google.cloud import gaming_v1beta


async def sample_delete_realm():
    # Create a client
    client = gaming_v1beta.RealmsServiceAsyncClient()

    # Initialize request argument(s)
    request = gaming_v1beta.DeleteRealmRequest(
        name="name_value",
    )

    # Make the request
    operation = client.delete_realm(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END gameservices_generated_gaming_v1beta_RealmsService_DeleteRealm_async]
