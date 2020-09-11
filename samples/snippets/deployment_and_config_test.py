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

import datetime
import time
import uuid

from google.api_core import exceptions

import pytest

import create_config
import create_deployment
import create_realm
import delete_config
import delete_deployment
import delete_realm
import get_config
import get_deployment
import get_rollout
import list_configs
import list_deployments
import update_deployment
import update_rollout_default
import update_rollout_override
import update_rollout_remove_default
import update_rollout_remove_override

PROJECT_ID = "python-docs-samples-tests"
CONFIG_ID = "my-game-server-config"
REALM_LOCATION = "global"

# The format of realm ID. This is used in the unit tests and cleanup below.
realm_id_format = 'test-realm-{}-{}'

# The format of deployment ID. This is used in the unit tests and cleanup below.
deployment_id_format = 'test-deployment-{}-{}'


@pytest.fixture(scope="session", autouse=True)
def clean_up_old_deployments():
    all_deployments = list_deployments.list_deployments(PROJECT_ID)
    for deployment in all_deployments:
        deployment_name = deployment.name
        deployment_id = deployment_name[deployment_name.rfind('/') + 1: len(deployment_name)]
        if deployment_id.find('test-deployment-') == 0:
            time_str = deployment_id[deployment_id.rfind('-') + 1: len(deployment_id)]
            test_date = datetime.datetime.utcfromtimestamp(int(time_str))
            now_date = datetime.datetime.utcfromtimestamp(int(time.time()))
            difftime = now_date - test_date

            # *NOTE* Restrict to deployments used in the tests older than 2 days
            #        to prevent thrashing in the case of async tests
            if (difftime.days > 2):
                print(f"Cleaning up old deployment {deployment_id} and its configs, difftime: {difftime}")
                clean_up_deployment_and_configs(deployment_id)


@pytest.fixture(scope="function")
def test_deployment():
    deployment_id = deployment_id_format.format(uuid.uuid4().hex, int(time.time()))

    print(f"Creating deployment {deployment_id} in project {PROJECT_ID}")
    create_deployment.create_deployment(PROJECT_ID, deployment_id)

    yield deployment_id

    print(f"Cleaning up deployment {deployment_id} in teardown")
    clean_up_deployment(deployment_id)


def clean_up_deployment(deployment_id):
    # Delete the deployment if it still exists.
    print(f"Deleting deployment: {deployment_id}")
    try:
        delete_deployment.delete_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return


@pytest.fixture(scope="function")
def test_deployment_with_config():
    deployment_id = deployment_id_format.format(uuid.uuid4().hex, int(time.time()))

    print(f"Creating deployment {deployment_id} in project {PROJECT_ID}")
    create_deployment.create_deployment(PROJECT_ID, deployment_id)

    print(f"Creating config {CONFIG_ID} in deployment {deployment_id} in project {PROJECT_ID}")
    create_config.create_config(PROJECT_ID, deployment_id, CONFIG_ID)

    yield deployment_id

    print(f"Cleaning up deployment {deployment_id} in teardown")
    clean_up_deployment_and_configs(deployment_id)


def clean_up_deployment_and_configs(deployment_id):
    # Delete the deployment and the game server configs in the deployment.
    try:
        get_deployment.get_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    try:
        update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    try:
        update_rollout_remove_override.update_rollout_remove_override(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return

    configs = list_configs.list_configs(PROJECT_ID, deployment_id)
    for config in configs:
        config_id = config.name.rsplit('/', 1)[-1]
        print(f"Deleting config {config_id} in deployment {deployment_id}")
        try:
            delete_config.delete_config(PROJECT_ID, deployment_id, config_id)
        except exceptions.NotFound:  # Ignore the non-existent config
            return

    print(f"Deleting deployment: {deployment_id}")
    try:
        delete_deployment.delete_deployment(PROJECT_ID, deployment_id)
    except exceptions.NotFound:  # Ignore the non-existent deployment
        return


@pytest.fixture(scope="function")
def test_realm():
    realm_id = realm_id_format.format(uuid.uuid4().hex, int(time.time()))

    print(f"Creating realm {realm_id} in location {REALM_LOCATION} in project {PROJECT_ID}")
    create_realm.create_realm(PROJECT_ID, REALM_LOCATION, realm_id)

    yield realm_id

    print(f"Cleaning up realm {realm_id} in teardown")
    clean_up_realm(realm_id)


def clean_up_realm(realm_id):
    # Delete the realm if it still exists.
    print(f"Deleting realm: {realm_id}")
    try:
        delete_realm.delete_realm(PROJECT_ID, REALM_LOCATION, realm_id)
    except exceptions.NotFound:  # Ignore the non-existent realm
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


def test_update_deployment(test_deployment):
    update_deployment.update_deployment(PROJECT_ID, test_deployment)
    deployment = get_deployment.get_deployment(PROJECT_ID, test_deployment)
    assert deployment.labels == {"label-key-1": "label-value-1", "label-key-2": "label-value-2"}


def test_delete_deployment(test_deployment):
    delete_deployment.delete_deployment(PROJECT_ID, test_deployment)
    with pytest.raises(exceptions.NotFound):
        get_deployment.get_deployment(PROJECT_ID, test_deployment)


def test_get_rollout(test_deployment):
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment)
    assert rollout.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment}/rollout"


def test_update_rollout_default(test_deployment_with_config):
    update_rollout_default.update_rollout_default(PROJECT_ID, test_deployment_with_config, CONFIG_ID)
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment_with_config)
    assert rollout.default_game_server_config == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment_with_config}/configs/{CONFIG_ID}"


def test_update_rollout_override(test_realm, test_deployment_with_config):
    update_rollout_override.update_rollout_override(PROJECT_ID, test_deployment_with_config, CONFIG_ID, REALM_LOCATION, test_realm)
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment_with_config)
    assert len(rollout.game_server_config_overrides) == 1
    assert rollout.game_server_config_overrides[0].config_version == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment_with_config}/configs/{CONFIG_ID}"
    assert rollout.game_server_config_overrides[0].realms_selector.realms == [f"projects/{PROJECT_ID}/locations/{REALM_LOCATION}/realms/{test_realm}"]


def test_update_rollout_remove_default(test_deployment):
    update_rollout_remove_default.update_rollout_remove_default(PROJECT_ID, test_deployment)
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment)
    assert rollout.default_game_server_config == ""


def test_update_rollout_remove_override(test_deployment):
    update_rollout_remove_override.update_rollout_remove_override(PROJECT_ID, test_deployment)
    rollout = get_rollout.get_rollout(PROJECT_ID, test_deployment)
    assert len(rollout.game_server_config_overrides) == 0


def test_create_conifg(test_deployment_with_config):
    print(f"Created config {CONFIG_ID} in deployment {test_deployment_with_config} in project {PROJECT_ID}")


def test_get_config(test_deployment_with_config):
    config = get_config.get_config(PROJECT_ID, test_deployment_with_config, CONFIG_ID)
    assert config.name == f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment_with_config}/configs/{CONFIG_ID}"


def test_list_configs(test_deployment_with_config):
    configs = list_configs.list_configs(PROJECT_ID, test_deployment_with_config)

    config_name_list = []
    for config in configs:
        config_name_list.append(config.name)

    config_name = f"projects/{PROJECT_ID}/locations/global/gameServerDeployments/{test_deployment_with_config}/configs/{CONFIG_ID}"
    assert config_name in config_name_list


def test_delete_config(test_deployment_with_config):
    delete_config.delete_config(PROJECT_ID, test_deployment_with_config, CONFIG_ID)
    with pytest.raises(exceptions.NotFound):
        get_config.get_config(PROJECT_ID, test_deployment_with_config, CONFIG_ID)
