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

"""Wait for an opertion for Google Cloud Game Servers."""

import time

# [START wait_for_operation]


def wait_for_operation(operation_client, operation_name):
    while True:
        print(f'Waiting for operation {operation_name} to finish...')

        operation = operation_client.get_operation(name=operation_name)

        if operation.done:
            print("operation done.")
            if operation.error.code:
                raise Exception(operation.error)
            return operation

        time.sleep(1)
# [END wait_for_operation]
