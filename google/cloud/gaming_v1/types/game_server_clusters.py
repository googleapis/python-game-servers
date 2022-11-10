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
from typing import MutableMapping, MutableSequence

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.gaming_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.gaming.v1",
    manifest={
        "GameServerClusterView",
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
        "KubernetesClusterState",
    },
)


class GameServerClusterView(proto.Enum):
    r"""A view for GameServerCluster objects."""
    GAME_SERVER_CLUSTER_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class ListGameServerClustersRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.ListGameServerClusters.

    Attributes:
        parent (str):
            Required. The parent resource name, in the
            following form:
            "projects/{project}/locations/{location}/realms/{realm}".
        page_size (int):
            Optional. The maximum number of items to return. If
            unspecified, the server will pick an appropriate default.
            The server may return fewer items than requested. A caller
            should only rely on response's
            [next_page_token][google.cloud.gaming.v1.ListGameServerClustersResponse.next_page_token]
            to determine if there are more GameServerClusters left to be
            queried.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specifies the ordering of results following syntax
            at
            https://cloud.google.com/apis/design/design_patterns#sorting_order.
        view (google.cloud.gaming_v1.types.GameServerClusterView):
            Optional. View for the returned GameServerCluster objects.
            When ``FULL`` is specified, the ``cluster_state`` field is
            also returned in the GameServerCluster object, which
            includes the state of the referenced Kubernetes cluster such
            as versions and provider info. The default/unset value is
            GAME_SERVER_CLUSTER_VIEW_UNSPECIFIED, same as BASIC, which
            does not return the ``cluster_state`` field.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    view: "GameServerClusterView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="GameServerClusterView",
    )


class ListGameServerClustersResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.ListGameServerClusters.

    Attributes:
        game_server_clusters (MutableSequence[google.cloud.gaming_v1.types.GameServerCluster]):
            The list of game server clusters.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    game_server_clusters: MutableSequence["GameServerCluster"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GameServerCluster",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class GetGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.GetGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to retrieve,
            in the following form:
            ``projects/{project}/locations/{location}/realms/{realm-id}/gameServerClusters/{cluster}``.
        view (google.cloud.gaming_v1.types.GameServerClusterView):
            Optional. View for the returned GameServerCluster objects.
            When ``FULL`` is specified, the ``cluster_state`` field is
            also returned in the GameServerCluster object, which
            includes the state of the referenced Kubernetes cluster such
            as versions and provider info. The default/unset value is
            GAME_SERVER_CLUSTER_VIEW_UNSPECIFIED, same as BASIC, which
            does not return the ``cluster_state`` field.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "GameServerClusterView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="GameServerClusterView",
    )


class CreateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.CreateGameServerCluster.

    Attributes:
        parent (str):
            Required. The parent resource name, in the following form:
            ``projects/{project}/locations/{location}/realms/{realm-id}``.
        game_server_cluster_id (str):
            Required. The ID of the game server cluster
            resource to be created.
        game_server_cluster (google.cloud.gaming_v1.types.GameServerCluster):
            Required. The game server cluster resource to
            be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    game_server_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    game_server_cluster: "GameServerCluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GameServerCluster",
    )


class PreviewCreateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.PreviewCreateGameServerCluster.

    Attributes:
        parent (str):
            Required. The parent resource name, in the following form:
            ``projects/{project}/locations/{location}/realms/{realm}``.
        game_server_cluster_id (str):
            Required. The ID of the game server cluster
            resource to be created.
        game_server_cluster (google.cloud.gaming_v1.types.GameServerCluster):
            Required. The game server cluster resource to
            be created.
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
        view (google.cloud.gaming_v1.types.GameServerClusterView):
            Optional. This field is deprecated, preview
            will always return KubernetesClusterState.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    game_server_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    game_server_cluster: "GameServerCluster" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GameServerCluster",
    )
    preview_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    view: "GameServerClusterView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="GameServerClusterView",
    )


class PreviewCreateGameServerClusterResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.PreviewCreateGameServerCluster.

    Attributes:
        etag (str):
            The ETag of the game server cluster.
        target_state (google.cloud.gaming_v1.types.TargetState):
            The target state.
        cluster_state (google.cloud.gaming_v1.types.KubernetesClusterState):
            Output only. The state of the Kubernetes cluster in preview,
            this will be available if 'view' is set to ``FULL`` in the
            relevant List/Get/Preview request.
    """

    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_state: common.TargetState = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.TargetState,
    )
    cluster_state: "KubernetesClusterState" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="KubernetesClusterState",
    )


class DeleteGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.DeleteGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to delete, in
            the following form:
            ``projects/{project}/locations/{location}/gameServerClusters/{cluster}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PreviewDeleteGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.PreviewDeleteGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to delete, in
            the following form:
            ``projects/{project}/locations/{location}/gameServerClusters/{cluster}``.
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    preview_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class PreviewDeleteGameServerClusterResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.PreviewDeleteGameServerCluster.

    Attributes:
        etag (str):
            The ETag of the game server cluster.
        target_state (google.cloud.gaming_v1.types.TargetState):
            The target state.
    """

    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_state: common.TargetState = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.TargetState,
    )


class UpdateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.UpdateGameServerCluster.

    Attributes:
        game_server_cluster (google.cloud.gaming_v1.types.GameServerCluster):
            Required. The game server cluster to be updated. Only fields
            specified in update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. For the ``FieldMask`` definition,
            see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    game_server_cluster: "GameServerCluster" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GameServerCluster",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class PreviewUpdateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.UpdateGameServerCluster.

    Attributes:
        game_server_cluster (google.cloud.gaming_v1.types.GameServerCluster):
            Required. The game server cluster to be updated. Only fields
            specified in update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. For the ``FieldMask`` definition,
            see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
    """

    game_server_cluster: "GameServerCluster" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GameServerCluster",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    preview_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class PreviewUpdateGameServerClusterResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.PreviewUpdateGameServerCluster

    Attributes:
        etag (str):
            The ETag of the game server cluster.
        target_state (google.cloud.gaming_v1.types.TargetState):
            The target state.
    """

    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_state: common.TargetState = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.TargetState,
    )


class GameServerClusterConnectionInfo(proto.Message):
    r"""The game server cluster connection information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gke_cluster_reference (google.cloud.gaming_v1.types.GkeClusterReference):
            Reference to the GKE cluster where the game
            servers are installed.

            This field is a member of `oneof`_ ``cluster_reference``.
        namespace (str):
            Namespace designated on the game server
            cluster where the Agones game server instances
            will be created. Existence of the namespace will
            be validated during creation.
    """

    gke_cluster_reference: "GkeClusterReference" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="cluster_reference",
        message="GkeClusterReference",
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GkeClusterReference(proto.Message):
    r"""A reference to a GKE cluster.

    Attributes:
        cluster (str):
            The full or partial name of a GKE cluster, using one of the
            following forms:

            -  ``projects/{project}/locations/{location}/clusters/{cluster}``
            -  ``locations/{location}/clusters/{cluster}``
            -  ``{cluster}`` If project and location are not specified,
               the project and location of the GameServerCluster
               resource are used to generate the full name of the GKE
               cluster.
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GameServerCluster(proto.Message):
    r"""A game server cluster resource.

    Attributes:
        name (str):
            Required. The resource name of the game server cluster, in
            the following form:
            ``projects/{project}/locations/{location}/realms/{realm}/gameServerClusters/{cluster}``.
            For example,
            ``projects/my-project/locations/{location}/realms/zanzibar/gameServerClusters/my-onprem-cluster``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            The labels associated with this game server
            cluster. Each label is a key-value pair.
        connection_info (google.cloud.gaming_v1.types.GameServerClusterConnectionInfo):
            The game server cluster connection
            information. This information is used to manage
            game server clusters.
        etag (str):
            ETag of the resource.
        description (str):
            Human readable description of the cluster.
        cluster_state (google.cloud.gaming_v1.types.KubernetesClusterState):
            Output only. The state of the Kubernetes cluster, this will
            be available if 'view' is set to ``FULL`` in the relevant
            List/Get/Preview request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    connection_info: "GameServerClusterConnectionInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="GameServerClusterConnectionInfo",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    cluster_state: "KubernetesClusterState" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="KubernetesClusterState",
    )


class KubernetesClusterState(proto.Message):
    r"""The state of the Kubernetes cluster.

    Attributes:
        agones_version_installed (str):
            Output only. The version of Agones currently
            installed in the registered Kubernetes cluster.
        kubernetes_version_installed (str):
            Output only. The version of Kubernetes that
            is currently used in the registered Kubernetes
            cluster (as detected by the Cloud Game Servers
            service).
        installation_state (google.cloud.gaming_v1.types.KubernetesClusterState.InstallationState):
            Output only. The state for the installed
            versions of Agones/Kubernetes.
        version_installed_error_message (str):
            Output only. The detailed error message for
            the installed versions of Agones/Kubernetes.
        provider (str):
            Output only. The cloud provider type reported
            by the first node's providerID in the list of
            nodes on the Kubernetes endpoint. On Kubernetes
            platforms that support zero-node clusters (like
            GKE-on-GCP), the provider type will be empty.
        agones_version_targeted (str):
            Output only. The version of Agones that is
            targeted to be installed in the cluster.
    """

    class InstallationState(proto.Enum):
        r"""The state of the installed versions of Agones/Kubernetes. See
        also
        https://cloud.google.com/game-servers/docs/versions-and-upgrades.
        """
        INSTALLATION_STATE_UNSPECIFIED = 0
        AGONES_KUBERNETES_VERSION_SUPPORTED = 1
        AGONES_VERSION_UNSUPPORTED = 2
        AGONES_KUBERNETES_VERSION_UNSUPPORTED = 3
        AGONES_VERSION_UNRECOGNIZED = 4
        KUBERNETES_VERSION_UNRECOGNIZED = 5
        VERSION_VERIFICATION_FAILED = 6
        AGONES_NOT_INSTALLED = 7

    agones_version_installed: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kubernetes_version_installed: str = proto.Field(
        proto.STRING,
        number=2,
    )
    installation_state: InstallationState = proto.Field(
        proto.ENUM,
        number=3,
        enum=InstallationState,
    )
    version_installed_error_message: str = proto.Field(
        proto.STRING,
        number=4,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=5,
    )
    agones_version_targeted: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
