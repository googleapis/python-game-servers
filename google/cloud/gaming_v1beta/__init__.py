# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.gaming import gapic_version as package_version

__version__ = package_version.__version__


from .services.game_server_clusters_service import (
    GameServerClustersServiceAsyncClient,
    GameServerClustersServiceClient,
)
from .services.game_server_configs_service import (
    GameServerConfigsServiceAsyncClient,
    GameServerConfigsServiceClient,
)
from .services.game_server_deployments_service import (
    GameServerDeploymentsServiceAsyncClient,
    GameServerDeploymentsServiceClient,
)
from .services.realms_service import RealmsServiceAsyncClient, RealmsServiceClient
from .types.common import (
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
from .types.game_server_clusters import (
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
from .types.game_server_configs import (
    CreateGameServerConfigRequest,
    DeleteGameServerConfigRequest,
    FleetConfig,
    GameServerConfig,
    GetGameServerConfigRequest,
    ListGameServerConfigsRequest,
    ListGameServerConfigsResponse,
    ScalingConfig,
)
from .types.game_server_deployments import (
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
from .types.realms import (
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
