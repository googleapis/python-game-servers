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

PROJECT_ID = "gcgs-client-lib-samples-python"
DEPLOYMENT_ID_1 = "deployment-{}".format(uuid.uuid4())


@pytest.fixture(scope="function", autouse=True)
def teardown():

    yield DEPLOYMENT_ID_1

    print("Cleaning up resources in teardown")
    clean_up_resources(DEPLOYMENT_ID_1)


def clean_up_resources(deployment_id):
    # Delete the deployment if it still exists.
    try:
        get_deployment.get_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    print(f"Deleting Game Server Deployment: {deployment_id}")
    update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, deployment_id)
    try:
        delete_deployment.delete_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return


def test_deployments():
    create_deployment.create_deployment(PROJECT_ID, DEPLOYMENT_ID_1)
    deployment1 = get_deployment.get_deployment(PROJECT_ID, DEPLOYMENT_ID_1)
    assert deployment1.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{DEPLOYMENT_ID_1}"

    deployments = list_deployments.list_deployments(PROJECT_ID)
    assert len(deployments) > 0

    rollout1 = get_rollout.get_rollout(PROJECT_ID, DEPLOYMENT_ID_1)
    assert rollout1.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{DEPLOYMENT_ID_1}/rollout"

    update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, DEPLOYMENT_ID_1)
    rollout1 = get_rollout.get_rollout(PROJECT_ID, DEPLOYMENT_ID_1)
    assert rollout1.default_game_server_config == ""

    delete_deployment.delete_deployment(PROJECT_ID, DEPLOYMENT_ID_1)

    with pytest.raises(exceptions.NotFound):
        get_deployment.get_deployment(PROJECT_ID, DEPLOYMENT_ID_1)
