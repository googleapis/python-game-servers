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

from google.cloud.gaming_v1.services.game_server_clusters_service.client import (
    GameServerClustersServiceClient,
)
from google.cloud.gaming_v1.services.game_server_clusters_service.async_client import (
    GameServerClustersServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_configs_service.client import (
    GameServerConfigsServiceClient,
)
from google.cloud.gaming_v1.services.game_server_configs_service.async_client import (
    GameServerConfigsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service.client import (
    GameServerDeploymentsServiceClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service.async_client import (
    GameServerDeploymentsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.realms_service.client import RealmsServiceClient
from google.cloud.gaming_v1.services.realms_service.async_client import (
    RealmsServiceAsyncClient,
)

from google.cloud.gaming_v1.types.common import DeployedFleetDetails
from google.cloud.gaming_v1.types.common import LabelSelector
from google.cloud.gaming_v1.types.common import OperationMetadata
from google.cloud.gaming_v1.types.common import OperationStatus
from google.cloud.gaming_v1.types.common import RealmSelector
from google.cloud.gaming_v1.types.common import Schedule
from google.cloud.gaming_v1.types.common import SpecSource
from google.cloud.gaming_v1.types.common import TargetDetails
from google.cloud.gaming_v1.types.common import TargetState
from google.cloud.gaming_v1.types.game_server_clusters import (
    CreateGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    DeleteGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import GameServerCluster
from google.cloud.gaming_v1.types.game_server_clusters import (
    GameServerClusterConnectionInfo,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    GetGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import GkeClusterReference
from google.cloud.gaming_v1.types.game_server_clusters import (
    ListGameServerClustersRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    ListGameServerClustersResponse,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewCreateGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewCreateGameServerClusterResponse,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewDeleteGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewDeleteGameServerClusterResponse,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewUpdateGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    PreviewUpdateGameServerClusterResponse,
)
from google.cloud.gaming_v1.types.game_server_clusters import (
    UpdateGameServerClusterRequest,
)
from google.cloud.gaming_v1.types.game_server_configs import (
    CreateGameServerConfigRequest,
)
from google.cloud.gaming_v1.types.game_server_configs import (
    DeleteGameServerConfigRequest,
)
from google.cloud.gaming_v1.types.game_server_configs import FleetConfig
from google.cloud.gaming_v1.types.game_server_configs import GameServerConfig
from google.cloud.gaming_v1.types.game_server_configs import GetGameServerConfigRequest
from google.cloud.gaming_v1.types.game_server_configs import (
    ListGameServerConfigsRequest,
)
from google.cloud.gaming_v1.types.game_server_configs import (
    ListGameServerConfigsResponse,
)
from google.cloud.gaming_v1.types.game_server_configs import ScalingConfig
from google.cloud.gaming_v1.types.game_server_deployments import (
    CreateGameServerDeploymentRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    DeleteGameServerDeploymentRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    FetchDeploymentStateRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    FetchDeploymentStateResponse,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    GameServerConfigOverride,
)
from google.cloud.gaming_v1.types.game_server_deployments import GameServerDeployment
from google.cloud.gaming_v1.types.game_server_deployments import (
    GameServerDeploymentRollout,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    GetGameServerDeploymentRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    GetGameServerDeploymentRolloutRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    ListGameServerDeploymentsRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    ListGameServerDeploymentsResponse,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    PreviewGameServerDeploymentRolloutRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    PreviewGameServerDeploymentRolloutResponse,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    UpdateGameServerDeploymentRequest,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
    UpdateGameServerDeploymentRolloutRequest,
)
from google.cloud.gaming_v1.types.realms import CreateRealmRequest
from google.cloud.gaming_v1.types.realms import DeleteRealmRequest
from google.cloud.gaming_v1.types.realms import GetRealmRequest
from google.cloud.gaming_v1.types.realms import ListRealmsRequest
from google.cloud.gaming_v1.types.realms import ListRealmsResponse
from google.cloud.gaming_v1.types.realms import PreviewRealmUpdateRequest
from google.cloud.gaming_v1.types.realms import PreviewRealmUpdateResponse
from google.cloud.gaming_v1.types.realms import Realm
from google.cloud.gaming_v1.types.realms import UpdateRealmRequest

__all__ = (
    "GameServerClustersServiceClient",
    "GameServerClustersServiceAsyncClient",
    "GameServerConfigsServiceClient",
    "GameServerConfigsServiceAsyncClient",
    "GameServerDeploymentsServiceClient",
    "GameServerDeploymentsServiceAsyncClient",
    "RealmsServiceClient",
    "RealmsServiceAsyncClient",
    "DeployedFleetDetails",
    "LabelSelector",
    "OperationMetadata",
    "OperationStatus",
    "RealmSelector",
    "Schedule",
    "SpecSource",
    "TargetDetails",
    "TargetState",
    "CreateGameServerClusterRequest",
    "DeleteGameServerClusterRequest",
    "GameServerCluster",
    "GameServerClusterConnectionInfo",
    "GetGameServerClusterRequest",
    "GkeClusterReference",
    "ListGameServerClustersRequest",
    "ListGameServerClustersResponse",
    "PreviewCreateGameServerClusterRequest",
    "PreviewCreateGameServerClusterResponse",
    "PreviewDeleteGameServerClusterRequest",
    "PreviewDeleteGameServerClusterResponse",
    "PreviewUpdateGameServerClusterRequest",
    "PreviewUpdateGameServerClusterResponse",
    "UpdateGameServerClusterRequest",
    "CreateGameServerConfigRequest",
    "DeleteGameServerConfigRequest",
    "FleetConfig",
    "GameServerConfig",
    "GetGameServerConfigRequest",
    "ListGameServerConfigsRequest",
    "ListGameServerConfigsResponse",
    "ScalingConfig",
    "CreateGameServerDeploymentRequest",
    "DeleteGameServerDeploymentRequest",
    "FetchDeploymentStateRequest",
    "FetchDeploymentStateResponse",
    "GameServerConfigOverride",
    "GameServerDeployment",
    "GameServerDeploymentRollout",
    "GetGameServerDeploymentRequest",
    "GetGameServerDeploymentRolloutRequest",
    "ListGameServerDeploymentsRequest",
    "ListGameServerDeploymentsResponse",
    "PreviewGameServerDeploymentRolloutRequest",
    "PreviewGameServerDeploymentRolloutResponse",
    "UpdateGameServerDeploymentRequest",
    "UpdateGameServerDeploymentRolloutRequest",
    "CreateRealmRequest",
    "DeleteRealmRequest",
    "GetRealmRequest",
    "ListRealmsRequest",
    "ListRealmsResponse",
    "PreviewRealmUpdateRequest",
    "PreviewRealmUpdateResponse",
    "Realm",
    "UpdateRealmRequest",
)
