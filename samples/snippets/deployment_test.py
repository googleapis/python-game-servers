# Copyright 2020, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from google.api_core import exceptions

import pytest

import create_deployment
import delete_deployment
import get_deployment
import get_rollout
import list_deployments
import update_rollout_remove_default

PROJECT_ID = "python-docs-samples-tests"


@pytest.fixture(scope="function")
def test_deployment():
    deployment_id = "deployment-{}".format(uuid.uuid4())

    print(f"Creating deployment {deployment_id} in project {PROJECT_ID}")
    create_deployment.create_deployment(PROJECT_ID, deployment_id)

    yield deployment_id

    print(f"Cleaning up deployment {deployment_id} in teardown")
    clean_up_deployment(deployment_id)


def clean_up_deployment(deployment_id):
    # Delete the deployment if it still exists.
    try:
        get_deployment.get_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    try:
        update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    print(f"Deleting deployment: {deployment_id}")
    try:
        delete_deployment.delete_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return


def test_create_deployment(test_deployment):
    print(f"Created deployment {test_deployment} in project {PROJECT_ID}")


def test_get_deployment(test_deployment):
    deployment = get_deployment.get_deployment(PROJECT_ID, test_deployment)
    assert deployment.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment}"


def test_list_deployments(test_deployment):
    deployments = list_deployments.list_deployments(PROJECT_ID)

    deployment_name_list = []
    for deployment in deployments:
        deployment_name_list.append(deployment.name)

    deployment_name = f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment}"
    assert deployment_name in deployment_name_list


def test_delete_deployment(test_deployment):
    delete_deployment.delete_deployment(PROJECT_ID, test_deployment)
    with pytest.raises(exceptions.NotFound):
        get_deployment.get_deployment(PROJECT_ID, test_deployment)


def test_get_rollout(test_deployment):
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment)
    assert rollout.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment}/rollout"


def test_update_rollout_remove_default(test_deployment):
    update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, test_deployment)
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment)
    assert rollout.default_game_server_config == ""
