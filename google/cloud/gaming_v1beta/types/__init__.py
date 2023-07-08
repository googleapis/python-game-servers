# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from .common import (
    DeployedFleetDetails,
    LabelSelector,
    OperationMetadata,
    OperationStatus,
    RealmSelector,
    Schedule,
    SpecSource,
    TargetDetails,
    TargetState,
)
from .game_server_clusters import (
    CreateGameServerClusterRequest,
    DeleteGameServerClusterRequest,
    GameServerCluster,
    GameServerClusterConnectionInfo,
    GetGameServerClusterRequest,
    GkeClusterReference,
    ListGameServerClustersRequest,
    ListGameServerClustersResponse,
    PreviewCreateGameServerClusterRequest,
    PreviewCreateGameServerClusterResponse,
    PreviewDeleteGameServerClusterRequest,
    PreviewDeleteGameServerClusterResponse,
    PreviewUpdateGameServerClusterRequest,
    PreviewUpdateGameServerClusterResponse,
    UpdateGameServerClusterRequest,
)
from .game_server_configs import (
    CreateGameServerConfigRequest,
    DeleteGameServerConfigRequest,
    FleetConfig,
    GameServerConfig,
    GetGameServerConfigRequest,
    ListGameServerConfigsRequest,
    ListGameServerConfigsResponse,
    ScalingConfig,
)
from .game_server_deployments import (
    CreateGameServerDeploymentRequest,
    DeleteGameServerDeploymentRequest,
    FetchDeploymentStateRequest,
    FetchDeploymentStateResponse,
    GameServerConfigOverride,
    GameServerDeployment,
    GameServerDeploymentRollout,
    GetGameServerDeploymentRequest,
    GetGameServerDeploymentRolloutRequest,
    ListGameServerDeploymentsRequest,
    ListGameServerDeploymentsResponse,
    PreviewGameServerDeploymentRolloutRequest,
    PreviewGameServerDeploymentRolloutResponse,
    UpdateGameServerDeploymentRequest,
    UpdateGameServerDeploymentRolloutRequest,
)
from .realms import (
    CreateRealmRequest,
    DeleteRealmRequest,
    GetRealmRequest,
    ListRealmsRequest,
    ListRealmsResponse,
    PreviewRealmUpdateRequest,
    PreviewRealmUpdateResponse,
    Realm,
    UpdateRealmRequest,
)

__all__ = (
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
