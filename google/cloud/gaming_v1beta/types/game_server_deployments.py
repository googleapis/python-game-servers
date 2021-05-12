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

from google.cloud.gaming_v1beta.types import common
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.gaming.v1beta",
    manifest={
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
    },
)


class ListGameServerDeploymentsRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.ListGameServerDeployments.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of items to return. If
            unspecified, the server will pick an appropriate default.
            The server may return fewer items than requested. A caller
            should only rely on response's
            [next_page_token][google.cloud.gaming.v1beta.ListGameServerDeploymentsResponse.next_page_token]
            to determine if there are more GameServerDeployments left to
            be queried.
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


class ListGameServerDeploymentsResponse(proto.Message):
    r"""Response message for
    GameServerDeploymentsService.ListGameServerDeployments.

    Attributes:
        game_server_deployments (Sequence[google.cloud.gaming_v1beta.types.GameServerDeployment]):
            The list of game server deployments.
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

    game_server_deployments = proto.RepeatedField(
        proto.MESSAGE, number=1, message="GameServerDeployment",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable = proto.RepeatedField(proto.STRING, number=4,)


class GetGameServerDeploymentRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.GetGameServerDeployment.

    Attributes:
        name (str):
            Required. The name of the game server delpoyment to
            retrieve. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.
    """

    name = proto.Field(proto.STRING, number=1,)


class GetGameServerDeploymentRolloutRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.GetGameServerDeploymentRollout.

    Attributes:
        name (str):
            Required. The name of the game server delpoyment to
            retrieve. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/rollout``.
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateGameServerDeploymentRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.CreateGameServerDeployment.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
            ``projects/{project}/locations/{location}``.
        deployment_id (str):
            Required. The ID of the game server
            delpoyment resource to be created.
        game_server_deployment (google.cloud.gaming_v1beta.types.GameServerDeployment):
            Required. The game server delpoyment resource
            to be created.
    """

    parent = proto.Field(proto.STRING, number=1,)
    deployment_id = proto.Field(proto.STRING, number=2,)
    game_server_deployment = proto.Field(
        proto.MESSAGE, number=3, message="GameServerDeployment",
    )


class DeleteGameServerDeploymentRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.DeleteGameServerDeployment.

    Attributes:
        name (str):
            Required. The name of the game server delpoyment to delete.
            Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.
    """

    name = proto.Field(proto.STRING, number=1,)


class UpdateGameServerDeploymentRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.UpdateGameServerDeployment. Only
    allows updates for labels.

    Attributes:
        game_server_deployment (google.cloud.gaming_v1beta.types.GameServerDeployment):
            Required. The game server delpoyment to be updated. Only
            fields specified in update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. For the ``FieldMask`` definition,
            see

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
    """

    game_server_deployment = proto.Field(
        proto.MESSAGE, number=1, message="GameServerDeployment",
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class UpdateGameServerDeploymentRolloutRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.UpdateGameServerRolloutDeployment.

    Attributes:
        rollout (google.cloud.gaming_v1beta.types.GameServerDeploymentRollout):
            Required. The game server delpoyment rollout to be updated.
            Only fields specified in update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. For the ``FieldMask`` definition,
            see

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
    """

    rollout = proto.Field(
        proto.MESSAGE, number=1, message="GameServerDeploymentRollout",
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class FetchDeploymentStateRequest(proto.Message):
    r"""Request message for
    GameServerDeploymentsService.FetchDeploymentState.

    Attributes:
        name (str):
            Required. The name of the game server delpoyment. Uses the
            form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.
    """

    name = proto.Field(proto.STRING, number=1,)


class FetchDeploymentStateResponse(proto.Message):
    r"""Response message for
    GameServerDeploymentsService.FetchDeploymentState.

    Attributes:
        cluster_state (Sequence[google.cloud.gaming_v1beta.types.FetchDeploymentStateResponse.DeployedClusterState]):
            The state of the game server deployment in
            each game server cluster.
        unavailable (Sequence[str]):
            List of locations that could not be reached.
    """

    class DeployedClusterState(proto.Message):
        r"""The game server cluster changes made by the game server
        deployment.

        Attributes:
            cluster (str):
                The name of the cluster.
            fleet_details (Sequence[google.cloud.gaming_v1beta.types.DeployedFleetDetails]):
                The details about the Agones fleets and
                autoscalers created in the game server cluster.
        """

        cluster = proto.Field(proto.STRING, number=1,)
        fleet_details = proto.RepeatedField(
            proto.MESSAGE, number=2, message=common.DeployedFleetDetails,
        )

    cluster_state = proto.RepeatedField(
        proto.MESSAGE, number=1, message=DeployedClusterState,
    )
    unavailable = proto.RepeatedField(proto.STRING, number=2,)


class GameServerDeployment(proto.Message):
    r"""A game server deployment resource.
    Attributes:
        name (str):
            The resource name of the game server deployment. Uses the
            form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.
            For example,

            ``projects/my-project/locations/{location}/gameServerDeployments/my-deployment``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (Sequence[google.cloud.gaming_v1beta.types.GameServerDeployment.LabelsEntry]):
            The labels associated with this game server
            deployment. Each label is a key-value pair.
        etag (str):
            ETag of the resource.
        description (str):
            Human readable description of the game server
            delpoyment.
    """

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    etag = proto.Field(proto.STRING, number=7,)
    description = proto.Field(proto.STRING, number=8,)


class GameServerConfigOverride(proto.Message):
    r"""A game server config override.
    Attributes:
        realms_selector (google.cloud.gaming_v1beta.types.RealmSelector):
            Selector for choosing applicable realms.
        config_version (str):
            The game server config for this override.
    """

    realms_selector = proto.Field(
        proto.MESSAGE, number=1, oneof="selector", message=common.RealmSelector,
    )
    config_version = proto.Field(proto.STRING, number=100, oneof="change",)


class GameServerDeploymentRollout(proto.Message):
    r"""The game server deployment rollout which represents the
    desired rollout state.

    Attributes:
        name (str):
            The resource name of the game server deployment rollout.
            Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/rollout``.
            For example,

            ``projects/my-project/locations/{location}/gameServerDeployments/my-deployment/rollout``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        default_game_server_config (str):
            The default game server config is applied to all realms
            unless overridden in the rollout. For example,

            ``projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config``.
        game_server_config_overrides (Sequence[google.cloud.gaming_v1beta.types.GameServerConfigOverride]):
            Contains the game server config rollout
            overrides. Overrides are processed in the order
            they are listed. Once a match is found for a
            realm, the rest of the list is not processed.
        etag (str):
            ETag of the resource.
    """

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    default_game_server_config = proto.Field(proto.STRING, number=4,)
    game_server_config_overrides = proto.RepeatedField(
        proto.MESSAGE, number=5, message="GameServerConfigOverride",
    )
    etag = proto.Field(proto.STRING, number=6,)


class PreviewGameServerDeploymentRolloutRequest(proto.Message):
    r"""Request message for PreviewGameServerDeploymentRollout.
    Attributes:
        rollout (google.cloud.gaming_v1beta.types.GameServerDeploymentRollout):
            Required. The game server deployment rollout to be updated.
            Only fields specified in update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to update. At least one path must
            be supplied in this field. For the ``FieldMask`` definition,
            see

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview. Defaults to the immediately after the
            proposed rollout completes.
    """

    rollout = proto.Field(
        proto.MESSAGE, number=1, message="GameServerDeploymentRollout",
    )
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )
    preview_time = proto.Field(
        proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,
    )


class PreviewGameServerDeploymentRolloutResponse(proto.Message):
    r"""Response message for PreviewGameServerDeploymentRollout.
    This has details about the Agones fleet and autoscaler to be
    actuated.

    Attributes:
        unavailable (Sequence[str]):
            Locations that could not be reached on this
            request.
        etag (str):
            ETag of the game server deployment.
        target_state (google.cloud.gaming_v1beta.types.TargetState):
            The target state.
    """

    unavailable = proto.RepeatedField(proto.STRING, number=2,)
    etag = proto.Field(proto.STRING, number=3,)
    target_state = proto.Field(proto.MESSAGE, number=4, message=common.TargetState,)


__all__ = tuple(sorted(__protobuf__.manifest))
