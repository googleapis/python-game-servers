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

from .services.game_server_clusters_service import GameServerClustersServiceClient
from .services.game_server_clusters_service import GameServerClustersServiceAsyncClient
from .services.game_server_configs_service import GameServerConfigsServiceClient
from .services.game_server_configs_service import GameServerConfigsServiceAsyncClient
from .services.game_server_deployments_service import GameServerDeploymentsServiceClient
from .services.game_server_deployments_service import (
    GameServerDeploymentsServiceAsyncClient,
)
from .services.realms_service import RealmsServiceClient
from .services.realms_service import RealmsServiceAsyncClient

from .types.common import DeployedFleetDetails
from .types.common import LabelSelector
from .types.common import OperationMetadata
from .types.common import OperationStatus
from .types.common import RealmSelector
from .types.common import Schedule
from .types.common import SpecSource
from .types.common import TargetDetails
from .types.common import TargetState
from .types.game_server_clusters import CreateGameServerClusterRequest
from .types.game_server_clusters import DeleteGameServerClusterRequest
from .types.game_server_clusters import GameServerCluster
from .types.game_server_clusters import GameServerClusterConnectionInfo
from .types.game_server_clusters import GetGameServerClusterRequest
from .types.game_server_clusters import GkeClusterReference
from .types.game_server_clusters import ListGameServerClustersRequest
from .types.game_server_clusters import ListGameServerClustersResponse
from .types.game_server_clusters import PreviewCreateGameServerClusterRequest
from .types.game_server_clusters import PreviewCreateGameServerClusterResponse
from .types.game_server_clusters import PreviewDeleteGameServerClusterRequest
from .types.game_server_clusters import PreviewDeleteGameServerClusterResponse
from .types.game_server_clusters import PreviewUpdateGameServerClusterRequest
from .types.game_server_clusters import PreviewUpdateGameServerClusterResponse
from .types.game_server_clusters import UpdateGameServerClusterRequest
from .types.game_server_configs import CreateGameServerConfigRequest
from .types.game_server_configs import DeleteGameServerConfigRequest
from .types.game_server_configs import FleetConfig
from .types.game_server_configs import GameServerConfig
from .types.game_server_configs import GetGameServerConfigRequest
from .types.game_server_configs import ListGameServerConfigsRequest
from .types.game_server_configs import ListGameServerConfigsResponse
from .types.game_server_configs import ScalingConfig
from .types.game_server_deployments import CreateGameServerDeploymentRequest
from .types.game_server_deployments import DeleteGameServerDeploymentRequest
from .types.game_server_deployments import FetchDeploymentStateRequest
from .types.game_server_deployments import FetchDeploymentStateResponse
from .types.game_server_deployments import GameServerConfigOverride
from .types.game_server_deployments import GameServerDeployment
from .types.game_server_deployments import GameServerDeploymentRollout
from .types.game_server_deployments import GetGameServerDeploymentRequest
from .types.game_server_deployments import GetGameServerDeploymentRolloutRequest
from .types.game_server_deployments import ListGameServerDeploymentsRequest
from .types.game_server_deployments import ListGameServerDeploymentsResponse
from .types.game_server_deployments import PreviewGameServerDeploymentRolloutRequest
from .types.game_server_deployments import PreviewGameServerDeploymentRolloutResponse
from .types.game_server_deployments import UpdateGameServerDeploymentRequest
from .types.game_server_deployments import UpdateGameServerDeploymentRolloutRequest
from .types.realms import CreateRealmRequest
from .types.realms import DeleteRealmRequest
from .types.realms import GetRealmRequest
from .types.realms import ListRealmsRequest
from .types.realms import ListRealmsResponse
from .types.realms import PreviewRealmUpdateRequest
from .types.realms import PreviewRealmUpdateResponse
from .types.realms import Realm
from .types.realms import UpdateRealmRequest

__all__ = (
    "GameServerClustersServiceAsyncClient",
    "GameServerConfigsServiceAsyncClient",
    "GameServerDeploymentsServiceAsyncClient",
    "RealmsServiceAsyncClient",
    "CreateGameServerClusterRequest",
    "CreateGameServerConfigRequest",
    "CreateGameServerDeploymentRequest",
    "CreateRealmRequest",
    "DeleteGameServerClusterRequest",
    "DeleteGameServerConfigRequest",
    "DeleteGameServerDeploymentRequest",
    "DeleteRealmRequest",
    "DeployedFleetDetails",
    "FetchDeploymentStateRequest",
    "FetchDeploymentStateResponse",
    "FleetConfig",
    "GameServerCluster",
    "GameServerClusterConnectionInfo",
    "GameServerClustersServiceClient",
    "GameServerConfig",
    "GameServerConfigOverride",
    "GameServerConfigsServiceClient",
    "GameServerDeployment",
    "GameServerDeploymentRollout",
    "GameServerDeploymentsServiceClient",
    "GetGameServerClusterRequest",
    "GetGameServerConfigRequest",
    "GetGameServerDeploymentRequest",
    "GetGameServerDeploymentRolloutRequest",
    "GetRealmRequest",
    "GkeClusterReference",
    "LabelSelector",
    "ListGameServerClustersRequest",
    "ListGameServerClustersResponse",
    "ListGameServerConfigsRequest",
    "ListGameServerConfigsResponse",
    "ListGameServerDeploymentsRequest",
    "ListGameServerDeploymentsResponse",
    "ListRealmsRequest",
    "ListRealmsResponse",
    "OperationMetadata",
    "OperationStatus",
    "PreviewCreateGameServerClusterRequest",
    "PreviewCreateGameServerClusterResponse",
    "PreviewDeleteGameServerClusterRequest",
    "PreviewDeleteGameServerClusterResponse",
    "PreviewGameServerDeploymentRolloutRequest",
    "PreviewGameServerDeploymentRolloutResponse",
    "PreviewRealmUpdateRequest",
    "PreviewRealmUpdateResponse",
    "PreviewUpdateGameServerClusterRequest",
    "PreviewUpdateGameServerClusterResponse",
    "Realm",
    "RealmSelector",
    "RealmsServiceClient",
    "ScalingConfig",
    "Schedule",
    "SpecSource",
    "TargetDetails",
    "TargetState",
    "UpdateGameServerClusterRequest",
    "UpdateGameServerDeploymentRequest",
    "UpdateGameServerDeploymentRolloutRequest",
    "UpdateRealmRequest",
)
