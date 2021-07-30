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
import proto  # type: ignore

from google.cloud.gaming_v1.types import common
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.gaming.v1",
    manifest={
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
    },
)


class ListGameServerClustersRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.ListGameServerClusters.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the
            form:
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
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)
    order_by = proto.Field(proto.STRING, number=5,)


class ListGameServerClustersResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.ListGameServerClusters.

    Attributes:
        game_server_clusters (Sequence[google.cloud.gaming_v1.types.GameServerCluster]):
            The list of game server clusters.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (Sequence[str]):
            List of locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    game_server_clusters = proto.RepeatedField(
        proto.MESSAGE, number=1, message="GameServerCluster",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable = proto.RepeatedField(proto.STRING, number=4,)


class GetGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.GetGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to retrieve.
            Uses the form:

            ``projects/{project}/locations/{location}/realms/{realm-id}/gameServerClusters/{cluster}``.
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.CreateGameServerCluster.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
            ``projects/{project}/locations/{location}/realms/{realm-id}``.
        game_server_cluster_id (str):
            Required. The ID of the game server cluster
            resource to be created.
        game_server_cluster (google.cloud.gaming_v1.types.GameServerCluster):
            Required. The game server cluster resource to
            be created.
    """

    parent = proto.Field(proto.STRING, number=1,)
    game_server_cluster_id = proto.Field(proto.STRING, number=2,)
    game_server_cluster = proto.Field(
        proto.MESSAGE, number=3, message="GameServerCluster",
    )


class PreviewCreateGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.PreviewCreateGameServerCluster.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
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
    """

    parent = proto.Field(proto.STRING, number=1,)
    game_server_cluster_id = proto.Field(proto.STRING, number=2,)
    game_server_cluster = proto.Field(
        proto.MESSAGE, number=3, message="GameServerCluster",
    )
    preview_time = proto.Field(
        proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,
    )


class PreviewCreateGameServerClusterResponse(proto.Message):
    r"""Response message for
    GameServerClustersService.PreviewCreateGameServerCluster.

    Attributes:
        etag (str):
            The ETag of the game server cluster.
        target_state (google.cloud.gaming_v1.types.TargetState):
            The target state.
    """

    etag = proto.Field(proto.STRING, number=2,)
    target_state = proto.Field(proto.MESSAGE, number=3, message=common.TargetState,)


class DeleteGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.DeleteGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to delete.
            Uses the form:
            ``projects/{project}/locations/{location}/gameServerClusters/{cluster}``.
    """

    name = proto.Field(proto.STRING, number=1,)


class PreviewDeleteGameServerClusterRequest(proto.Message):
    r"""Request message for
    GameServerClustersService.PreviewDeleteGameServerCluster.

    Attributes:
        name (str):
            Required. The name of the game server cluster to delete.
            Uses the form:
            ``projects/{project}/locations/{location}/gameServerClusters/{cluster}``.
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
    """

    name = proto.Field(proto.STRING, number=1,)
    preview_time = proto.Field(
        proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,
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

    etag = proto.Field(proto.STRING, number=2,)
    target_state = proto.Field(proto.MESSAGE, number=3, message=common.TargetState,)


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

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
    """

    game_server_cluster = proto.Field(
        proto.MESSAGE, number=1, message="GameServerCluster",
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
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

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
    """

    game_server_cluster = proto.Field(
        proto.MESSAGE, number=1, message="GameServerCluster",
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )
    preview_time = proto.Field(
        proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,
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

    etag = proto.Field(proto.STRING, number=2,)
    target_state = proto.Field(proto.MESSAGE, number=3, message=common.TargetState,)


class GameServerClusterConnectionInfo(proto.Message):
    r"""The game server cluster connection information.
    Attributes:
        gke_cluster_reference (google.cloud.gaming_v1.types.GkeClusterReference):
            Reference to the GKE cluster where the game
            servers are installed.
        namespace (str):
            Namespace designated on the game server
            cluster where the Agones game server instances
            will be created. Existence of the namespace will
            be validated during creation.
    """

    gke_cluster_reference = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="cluster_reference",
        message="GkeClusterReference",
    )
    namespace = proto.Field(proto.STRING, number=5,)


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

    cluster = proto.Field(proto.STRING, number=1,)


class GameServerCluster(proto.Message):
    r"""A game server cluster resource.
    Attributes:
        name (str):
            Required. The resource name of the game server cluster. Uses
            the form:

            ``projects/{project}/locations/{location}/realms/{realm}/gameServerClusters/{cluster}``.
            For example,

            ``projects/my-project/locations/{location}/realms/zanzibar/gameServerClusters/my-onprem-cluster``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (Sequence[google.cloud.gaming_v1.types.GameServerCluster.LabelsEntry]):
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
    """

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    connection_info = proto.Field(
        proto.MESSAGE, number=5, message="GameServerClusterConnectionInfo",
    )
    etag = proto.Field(proto.STRING, number=6,)
    description = proto.Field(proto.STRING, number=7,)


__all__ = tuple(sorted(__protobuf__.manifest))
