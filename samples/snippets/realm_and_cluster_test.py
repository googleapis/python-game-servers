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

import create_cluster
import create_realm
import delete_cluster
import delete_realm
import get_cluster
import get_realm
import list_clusters
import list_realms
import update_cluster
import update_realm

PROJECT_ID = "python-docs-samples-tests"
REALM_LOCATION = "global"
CLUSTER_ID = "my-cluster"
GKE_CLUSTER_NAME = "projects/gcgs-client-lib-samples/locations/us-central1/clusters/gke-shared-default"


# The format of realm ID. This is used in the unit tests and cleanup below.
realm_id_format = 'test-realm-{}-{}'


@pytest.fixture(scope="session", autouse=True)
def clean_up_old_realms():
    all_realms = list_realms.list_realms(PROJECT_ID, REALM_LOCATION)
    for realm in all_realms:
        realm_name = realm.name
        realm_id = realm_name[realm_name.rfind('/') + 1: len(realm_name)]
        if realm_id.find('test-realm-') == 0:
            time_str = realm_id[realm_id.rfind('-') + 1: len(realm_id)]
            test_date = datetime.datetime.utcfromtimestamp(int(time_str))
            now_date = datetime.datetime.utcfromtimestamp(int(time.time()))
            difftime = now_date - test_date

            # *NOTE* Restrict to realms used in the tests older than 2 days
            #        to prevent thrashing in the case of async tests
            if (difftime.days > 2):
                print(f"Cleaning up old realm {realm_id} and its clusters, difftime: {difftime}")
                clean_up_realm_and_clusters(realm_id)


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


@pytest.fixture(scope="function")
def test_realm_with_cluster():
    realm_id = realm_id_format.format(uuid.uuid4().hex, int(time.time()))

    print(f"Creating realm {realm_id} in location {REALM_LOCATION} in project {PROJECT_ID}")
    create_realm.create_realm(PROJECT_ID, REALM_LOCATION, realm_id)

    print(f"Creating cluster {CLUSTER_ID} in realm {realm_id} in project {PROJECT_ID}")
    create_cluster.create_cluster(PROJECT_ID, REALM_LOCATION, realm_id, CLUSTER_ID, GKE_CLUSTER_NAME)

    yield realm_id

    print(f"Cleaning up realm {realm_id} in teardown")
    clean_up_realm_and_clusters(realm_id)


def clean_up_realm_and_clusters(realm_id):
    # Delete the realm and the game server clusters in the realm.
    try:
        get_realm.get_realm(PROJECT_ID, REALM_LOCATION, realm_id)
    except exceptions.NotFound:  # Ignore the non-existent realm
        return

    clusters = list_clusters.list_clusters(PROJECT_ID, REALM_LOCATION, realm_id)
    for cluster in clusters:
        cluster_id = cluster.name.rsplit('/', 1)[-1]
        print(f"Deleting cluster {cluster_id} in realm {realm_id}")
        try:
            delete_cluster.delete_cluster(PROJECT_ID, REALM_LOCATION, realm_id, cluster_id)
        except exceptions.NotFound:  # Ignore the non-existent cluster
            return

    print(f"Deleting realm: {realm_id}")
    try:
        delete_realm.delete_realm(PROJECT_ID, REALM_LOCATION, realm_id)
    except exceptions.NotFound:  # Ignore the non-existent realm
        return


def test_create_realm(test_realm):
    print(f"Created realm {test_realm} in project {PROJECT_ID}")


def test_get_realm(test_realm):
    realm = get_realm.get_realm(PROJECT_ID, REALM_LOCATION, test_realm)
    assert realm.name == f"projects/{PROJECT_ID}/locations/{REALM_LOCATION}/realms/{test_realm}"


def test_list_realms(test_realm):
    realms = list_realms.list_realms(PROJECT_ID, REALM_LOCATION)

    realm_name_list = []
    for realm in realms:
        realm_name_list.append(realm.name)

    realm_name = f"projects/{PROJECT_ID}/locations/{REALM_LOCATION}/realms/{test_realm}"
    assert realm_name in realm_name_list


def test_update_realm(test_realm):
    update_realm.update_realm(PROJECT_ID, REALM_LOCATION, test_realm)
    realm = get_realm.get_realm(PROJECT_ID, REALM_LOCATION, test_realm)
    assert realm.labels == {"label-key-1": "label-value-1", "label-key-2": "label-value-2"}


def test_delete_realm(test_realm):
    delete_realm.delete_realm(PROJECT_ID, REALM_LOCATION, test_realm)
    with pytest.raises(exceptions.NotFound):
        get_realm.get_realm(PROJECT_ID, REALM_LOCATION, test_realm)


def test_create_cluster(test_realm_with_cluster):
    print(f"Created cluster {CLUSTER_ID} in realm {test_realm_with_cluster} in project {PROJECT_ID}")


def test_get_cluster(test_realm_with_cluster):
    cluster = get_cluster.get_cluster(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster, CLUSTER_ID)
    assert cluster.name == f"projects/{PROJECT_ID}/locations/{REALM_LOCATION}/realms/{test_realm_with_cluster}/gameServerClusters/{CLUSTER_ID}"


def test_list_clusters(test_realm_with_cluster):
    clusters = list_clusters.list_clusters(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster)

    cluster_name_list = []
    for cluster in clusters:
        cluster_name_list.append(cluster.name)

    cluster_name = f"projects/{PROJECT_ID}/locations/{REALM_LOCATION}/realms/{test_realm_with_cluster}/gameServerClusters/{CLUSTER_ID}"
    assert cluster_name in cluster_name_list


def test_update_cluster(test_realm_with_cluster):
    update_cluster.update_cluster(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster, CLUSTER_ID)
    cluster = get_cluster.get_cluster(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster, CLUSTER_ID)
    assert cluster.labels == {"label-key-1": "label-value-1", "label-key-2": "label-value-2"}


def test_delete_cluster(test_realm_with_cluster):
    delete_cluster.delete_cluster(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster, CLUSTER_ID)
    with pytest.raises(exceptions.NotFound):
        get_cluster.get_cluster(PROJECT_ID, REALM_LOCATION, test_realm_with_cluster, CLUSTER_ID)
