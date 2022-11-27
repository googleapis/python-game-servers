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


from google.cloud.gaming_v1.services.game_server_clusters_service.async_client import (
    GameServerClustersServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_clusters_service.client import (
    GameServerClustersServiceClient,
)
from google.cloud.gaming_v1.services.game_server_configs_service.async_client import (
    GameServerConfigsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_configs_service.client import (
    GameServerConfigsServiceClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service.async_client import (
    GameServerDeploymentsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service.client import (
    GameServerDeploymentsServiceClient,
)
from google.cloud.gaming_v1.services.realms_service.async_client import (
    RealmsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.realms_service.client import RealmsServiceClient
from google.cloud.gaming_v1.types.common import (
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
from google.cloud.gaming_v1.types.game_server_clusters import (
    CreateGameServerClusterRequest,
    DeleteGameServerClusterRequest,
    GameServerCluster,
    GameServerClusterConnectionInfo,
    GameServerClusterView,
    GetGameServerClusterRequest,
    GkeClusterReference,
    KubernetesClusterState,
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
from google.cloud.gaming_v1.types.game_server_configs import (
    CreateGameServerConfigRequest,
    DeleteGameServerConfigRequest,
    FleetConfig,
    GameServerConfig,
    GetGameServerConfigRequest,
    ListGameServerConfigsRequest,
    ListGameServerConfigsResponse,
    ScalingConfig,
)
from google.cloud.gaming_v1.types.game_server_deployments import (
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
from google.cloud.gaming_v1.types.realms import (
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
    "KubernetesClusterState",
    "ListGameServerClustersRequest",
    "ListGameServerClustersResponse",
    "PreviewCreateGameServerClusterRequest",
    "PreviewCreateGameServerClusterResponse",
    "PreviewDeleteGameServerClusterRequest",
    "PreviewDeleteGameServerClusterResponse",
    "PreviewUpdateGameServerClusterRequest",
    "PreviewUpdateGameServerClusterResponse",
    "UpdateGameServerClusterRequest",
    "GameServerClusterView",
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
