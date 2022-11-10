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

from google.cloud.gaming_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.gaming.v1beta",
    manifest={
        "ListRealmsRequest",
        "ListRealmsResponse",
        "GetRealmRequest",
        "CreateRealmRequest",
        "DeleteRealmRequest",
        "UpdateRealmRequest",
        "PreviewRealmUpdateRequest",
        "PreviewRealmUpdateResponse",
        "Realm",
    },
)


class ListRealmsRequest(proto.Message):
    r"""Request message for RealmsService.ListRealms.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of items to return. If
            unspecified, server will pick an appropriate default. Server
            may return fewer items than requested. A caller should only
            rely on response's
            [next_page_token][google.cloud.gaming.v1beta.ListRealmsResponse.next_page_token]
            to determine if there are more realms left to be queried.
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


class ListRealmsResponse(proto.Message):
    r"""Response message for RealmsService.ListRealms.

    Attributes:
        realms (MutableSequence[google.cloud.gaming_v1beta.types.Realm]):
            The list of realms.
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

    realms: MutableSequence["Realm"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Realm",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetRealmRequest(proto.Message):
    r"""Request message for RealmsService.GetRealm.

    Attributes:
        name (str):
            Required. The name of the realm to retrieve. Uses the form:
            ``projects/{project}/locations/{location}/realms/{realm}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRealmRequest(proto.Message):
    r"""Request message for RealmsService.CreateRealm.

    Attributes:
        parent (str):
            Required. The parent resource name. Uses the form:
            ``projects/{project}/locations/{location}``.
        realm_id (str):
            Required. The ID of the realm resource to be
            created.
        realm (google.cloud.gaming_v1beta.types.Realm):
            Required. The realm resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    realm_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    realm: "Realm" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Realm",
    )


class DeleteRealmRequest(proto.Message):
    r"""Request message for RealmsService.DeleteRealm.

    Attributes:
        name (str):
            Required. The name of the realm to delete. Uses the form:
            ``projects/{project}/locations/{location}/realms/{realm}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRealmRequest(proto.Message):
    r"""Request message for RealmsService.UpdateRealm.

    Attributes:
        realm (google.cloud.gaming_v1beta.types.Realm):
            Required. The realm to be updated. Only fields specified in
            update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
    """

    realm: "Realm" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Realm",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class PreviewRealmUpdateRequest(proto.Message):
    r"""Request message for RealmsService.PreviewRealmUpdate.

    Attributes:
        realm (google.cloud.gaming_v1beta.types.Realm):
            Required. The realm to be updated. Only fields specified in
            update_mask are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see

            https: //developers.google.com/protocol-buffers //
            /docs/reference/google.protobuf#fieldmask
        preview_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target timestamp to compute the
            preview.
    """

    realm: "Realm" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Realm",
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


class PreviewRealmUpdateResponse(proto.Message):
    r"""Response message for RealmsService.PreviewRealmUpdate.

    Attributes:
        etag (str):
            ETag of the realm.
        target_state (google.cloud.gaming_v1beta.types.TargetState):
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


class Realm(proto.Message):
    r"""A realm resource.

    Attributes:
        name (str):
            The resource name of the realm. Uses the form:
            ``projects/{project}/locations/{location}/realms/{realm}``.
            For example,
            ``projects/my-project/locations/{location}/realms/my-realm``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        labels (MutableMapping[str, str]):
            The labels associated with this realm. Each
            label is a key-value pair.
        time_zone (str):
            Required. Time zone where all policies
            targeting this realm are evaluated. The value of
            this field must be from the IANA time zone
            database: https://www.iana.org/time-zones.
        etag (str):
            ETag of the resource.
        description (str):
            Human readable description of the realm.
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
    time_zone: str = proto.Field(
        proto.STRING,
        number=6,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
