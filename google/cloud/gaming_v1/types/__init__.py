# -*- coding: utf-8 -*-

# Copyright (C) 2019  Google LLC
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
    OperationMetadata,
    OperationStatus,
    LabelSelector,
    RealmSelector,
    Schedule,
    SpecSource,
    TargetDetails,
    TargetState,
    DeployedFleetDetails,
)
from .game_server_configs import (
    ListGameServerConfigsRequest,
    ListGameServerConfigsResponse,
    GetGameServerConfigRequest,
    CreateGameServerConfigRequest,
    DeleteGameServerConfigRequest,
    ScalingConfig,
    FleetConfig,
    GameServerConfig,
)
from .game_server_deployments import (
    ListGameServerDeploymentsRequest,
    ListGameServerDeploymentsResponse,
    GetGameServerDeploymentRequest,
    GetGameServerDeploymentRolloutRequest,
    CreateGameServerDeploymentRequest,
    DeleteGameServerDeploymentRequest,
    UpdateGameServerDeploymentRequest,
    UpdateGameServerDeploymentRolloutRequest,
    FetchDeploymentStateRequest,
    FetchDeploymentStateResponse,
    GameServerDeployment,
    GameServerConfigOverride,
    GameServerDeploymentRollout,
    PreviewGameServerDeploymentRolloutRequest,
    PreviewGameServerDeploymentRolloutResponse,
)
from .realms import (
    ListRealmsRequest,
    ListRealmsResponse,
    GetRealmRequest,
    CreateRealmRequest,
    DeleteRealmRequest,
    UpdateRealmRequest,
    PreviewRealmUpdateRequest,
    PreviewRealmUpdateResponse,
    Realm,
)
from .game_server_clusters import (
    ListGameServerClustersRequest,
    ListGameServerClustersResponse,
    GetGameServerClusterRequest,
    CreateGameServerClusterRequest,
    PreviewCreateGameServerClusterRequest,
    PreviewCreateGameServerClusterResponse,
    DeleteGameServerClusterRequest,
    PreviewDeleteGameServerClusterRequest,
    PreviewDeleteGameServerClusterResponse,
    UpdateGameServerClusterRequest,
    PreviewUpdateGameServerClusterRequest,
    PreviewUpdateGameServerClusterResponse,
    GameServerClusterConnectionInfo,
    GkeClusterReference,
    GameServerCluster,
)


__all__ = (
    "OperationMetadata",
    "OperationStatus",
    "LabelSelector",
    "RealmSelector",
    "Schedule",
    "SpecSource",
    "TargetDetails",
    "TargetState",
    "DeployedFleetDetails",
    "ListGameServerConfigsRequest",
    "ListGameServerConfigsResponse",
    "GetGameServerConfigRequest",
    "CreateGameServerConfigRequest",
    "DeleteGameServerConfigRequest",
    "ScalingConfig",
    "FleetConfig",
    "GameServerConfig",
    "ListGameServerDeploymentsRequest",
    "ListGameServerDeploymentsResponse",
    "GetGameServerDeploymentRequest",
    "GetGameServerDeploymentRolloutRequest",
    "CreateGameServerDeploymentRequest",
    "DeleteGameServerDeploymentRequest",
    "UpdateGameServerDeploymentRequest",
    "UpdateGameServerDeploymentRolloutRequest",
    "FetchDeploymentStateRequest",
    "FetchDeploymentStateResponse",
    "GameServerDeployment",
    "GameServerConfigOverride",
    "GameServerDeploymentRollout",
    "PreviewGameServerDeploymentRolloutRequest",
    "PreviewGameServerDeploymentRolloutResponse",
    "ListRealmsRequest",
    "ListRealmsResponse",
    "GetRealmRequest",
    "CreateRealmRequest",
    "DeleteRealmRequest",
    "UpdateRealmRequest",
    "PreviewRealmUpdateRequest",
    "PreviewRealmUpdateResponse",
    "Realm",
    "ListGameServerClustersRequest",
    "ListGameServerClustersResponse",
    "GetGameServerClusterRequest",
    "CreateGameServerClusterRequest",
    "PreviewCreateGameServerClusterRequest",
    "PreviewCreateGameServerClusterResponse",
    "DeleteGameServerClusterRequest",
    "PreviewDeleteGameServerClusterRequest",
    "PreviewDeleteGameServerClusterResponse",
    "UpdateGameServerClusterRequest",
    "PreviewUpdateGameServerClusterRequest",
    "PreviewUpdateGameServerClusterResponse",
    "GameServerClusterConnectionInfo",
    "GkeClusterReference",
    "GameServerCluster",
)
