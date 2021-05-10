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

from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.gaming.v1beta",
    manifest={
        "OperationMetadata",
        "OperationStatus",
        "LabelSelector",
        "RealmSelector",
        "Schedule",
        "SpecSource",
        "TargetDetails",
        "TargetState",
        "DeployedFleetDetails",
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.
    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
        unreachable (Sequence[str]):
            Output only. List of Locations that could not
            be reached.
        operation_status (Sequence[google.cloud.gaming_v1beta.types.OperationMetadata.OperationStatusEntry]):
            Output only. Operation status for Game
            Services API operations. Operation status is in
            the form of key-value pairs where keys are
            resource IDs and the values show the status of
            the operation. In case of failures, the value
            includes an error code and error message.
    """

    create_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    target = proto.Field(proto.STRING, number=3,)
    verb = proto.Field(proto.STRING, number=4,)
    status_message = proto.Field(proto.STRING, number=5,)
    requested_cancellation = proto.Field(proto.BOOL, number=6,)
    api_version = proto.Field(proto.STRING, number=7,)
    unreachable = proto.RepeatedField(proto.STRING, number=8,)
    operation_status = proto.MapField(
        proto.STRING, proto.MESSAGE, number=9, message="OperationStatus",
    )


class OperationStatus(proto.Message):
    r"""
    Attributes:
        done (bool):
            Output only. Whether the operation is done or
            still in progress.
        error_code (google.cloud.gaming_v1beta.types.OperationStatus.ErrorCode):
            The error code in case of failures.
        error_message (str):
            The human-readable error message.
    """

    class ErrorCode(proto.Enum):
        r""""""
        ERROR_CODE_UNSPECIFIED = 0
        INTERNAL_ERROR = 1
        PERMISSION_DENIED = 2
        CLUSTER_CONNECTION = 3

    done = proto.Field(proto.BOOL, number=1,)
    error_code = proto.Field(proto.ENUM, number=2, enum=ErrorCode,)
    error_message = proto.Field(proto.STRING, number=3,)


class LabelSelector(proto.Message):
    r"""The label selector, used to group labels on the resources.
    Attributes:
        labels (Sequence[google.cloud.gaming_v1beta.types.LabelSelector.LabelsEntry]):
            Resource labels for this selector.
    """

    labels = proto.MapField(proto.STRING, proto.STRING, number=1,)


class RealmSelector(proto.Message):
    r"""The realm selector, used to match realm resources.
    Attributes:
        realms (Sequence[str]):
            List of realms to match.
    """

    realms = proto.RepeatedField(proto.STRING, number=1,)


class Schedule(proto.Message):
    r"""The schedule of a recurring or one time event. The event's time span
    is specified by start_time and end_time. If the scheduled event's
    timespan is larger than the cron_spec + cron_job_duration, the event
    will be recurring. If only cron_spec + cron_job_duration are
    specified, the event is effective starting at the local time
    specified by cron_spec, and is recurring.

    ::

        start_time|-------[cron job]-------[cron job]-------[cron job]---|end_time
        cron job: cron spec start time + duration


    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start time of the event.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end time of the event.
        cron_job_duration (google.protobuf.duration_pb2.Duration):
            The duration for the cron job event. The
            duration of the event is effective after the
            cron job's start time.
        cron_spec (str):
            The cron definition of the scheduled event.
            See https://en.wikipedia.org/wiki/Cron. Cron
            spec specifies the local time as defined by the
            realm.
    """

    start_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    cron_job_duration = proto.Field(
        proto.MESSAGE, number=3, message=duration_pb2.Duration,
    )
    cron_spec = proto.Field(proto.STRING, number=4,)


class SpecSource(proto.Message):
    r"""Encapsulates Agones fleet spec and Agones autoscaler spec
    sources.

    Attributes:
        game_server_config_name (str):
            The game server config resource. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}``.
        name (str):
            The name of the Agones leet config or Agones
            scaling config used to derive the Agones fleet
            or Agones autoscaler spec.
    """

    game_server_config_name = proto.Field(proto.STRING, number=1,)
    name = proto.Field(proto.STRING, number=2,)


class TargetDetails(proto.Message):
    r"""Details about the Agones resources.
    Attributes:
        game_server_cluster_name (str):
            The game server cluster name. Uses the form:

            ``projects/{project}/locations/{location}/realms/{realm}/gameServerClusters/{cluster}``.
        game_server_deployment_name (str):
            The game server deployment name. Uses the form:

            ``projects/{project}/locations/{location}/gameServerDeployments/{deployment_id}``.
        fleet_details (Sequence[google.cloud.gaming_v1beta.types.TargetDetails.TargetFleetDetails]):
            Agones fleet details for game server clusters
            and game server deployments.
    """

    class TargetFleetDetails(proto.Message):
        r"""Details of the target Agones fleet.
        Attributes:
            fleet (google.cloud.gaming_v1beta.types.TargetDetails.TargetFleetDetails.TargetFleet):
                Reference to target Agones fleet.
            autoscaler (google.cloud.gaming_v1beta.types.TargetDetails.TargetFleetDetails.TargetFleetAutoscaler):
                Reference to target Agones fleet autoscaling
                policy.
        """

        class TargetFleet(proto.Message):
            r"""Target Agones fleet specification.
            Attributes:
                name (str):
                    The name of the Agones fleet.
                spec_source (google.cloud.gaming_v1beta.types.SpecSource):
                    Encapsulates the source of the Agones fleet
                    spec. The Agones fleet spec source.
            """

            name = proto.Field(proto.STRING, number=1,)
            spec_source = proto.Field(proto.MESSAGE, number=2, message="SpecSource",)

        class TargetFleetAutoscaler(proto.Message):
            r"""Target Agones autoscaler policy reference.
            Attributes:
                name (str):
                    The name of the Agones autoscaler.
                spec_source (google.cloud.gaming_v1beta.types.SpecSource):
                    Encapsulates the source of the Agones fleet
                    spec. Details about the Agones autoscaler spec.
            """

            name = proto.Field(proto.STRING, number=1,)
            spec_source = proto.Field(proto.MESSAGE, number=2, message="SpecSource",)

        fleet = proto.Field(
            proto.MESSAGE,
            number=1,
            message="TargetDetails.TargetFleetDetails.TargetFleet",
        )
        autoscaler = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TargetDetails.TargetFleetDetails.TargetFleetAutoscaler",
        )

    game_server_cluster_name = proto.Field(proto.STRING, number=1,)
    game_server_deployment_name = proto.Field(proto.STRING, number=2,)
    fleet_details = proto.RepeatedField(
        proto.MESSAGE, number=3, message=TargetFleetDetails,
    )


class TargetState(proto.Message):
    r"""Encapsulates the Target state.
    Attributes:
        details (Sequence[google.cloud.gaming_v1beta.types.TargetDetails]):
            Details about Agones fleets.
    """

    details = proto.RepeatedField(proto.MESSAGE, number=1, message="TargetDetails",)


class DeployedFleetDetails(proto.Message):
    r"""Details of the deployed Agones fleet.
    Attributes:
        deployed_fleet (google.cloud.gaming_v1beta.types.DeployedFleetDetails.DeployedFleet):
            Information about the Agones fleet.
        deployed_autoscaler (google.cloud.gaming_v1beta.types.DeployedFleetDetails.DeployedFleetAutoscaler):
            Information about the Agones autoscaler for
            that fleet.
    """

    class DeployedFleet(proto.Message):
        r"""Agones fleet specification and details.
        Attributes:
            fleet (str):
                The name of the Agones fleet.
            fleet_spec (str):
                The fleet spec retrieved from the Agones
                fleet.
            spec_source (google.cloud.gaming_v1beta.types.SpecSource):
                The source spec that is used to create the
                Agones fleet. The GameServerConfig resource may
                no longer exist in the system.
            status (google.cloud.gaming_v1beta.types.DeployedFleetDetails.DeployedFleet.DeployedFleetStatus):
                The current status of the Agones fleet.
                Includes count of game servers in various
                states.
        """

        class DeployedFleetStatus(proto.Message):
            r"""DeployedFleetStatus has details about the Agones fleets such
            as how many are running, how many allocated, and so on.

            Attributes:
                ready_replicas (int):
                    The number of GameServer replicas in the
                    READY state in this fleet.
                allocated_replicas (int):
                    The number of GameServer replicas in the
                    ALLOCATED state in this fleet.
                reserved_replicas (int):
                    The number of GameServer replicas in the
                    RESERVED state in this fleet. Reserved instances
                    won't be deleted on scale down, but won't cause
                    an autoscaler to scale up.
                replicas (int):
                    The total number of current GameServer
                    replicas in this fleet.
            """

            ready_replicas = proto.Field(proto.INT64, number=1,)
            allocated_replicas = proto.Field(proto.INT64, number=2,)
            reserved_replicas = proto.Field(proto.INT64, number=3,)
            replicas = proto.Field(proto.INT64, number=4,)

        fleet = proto.Field(proto.STRING, number=1,)
        fleet_spec = proto.Field(proto.STRING, number=2,)
        spec_source = proto.Field(proto.MESSAGE, number=3, message="SpecSource",)
        status = proto.Field(
            proto.MESSAGE,
            number=5,
            message="DeployedFleetDetails.DeployedFleet.DeployedFleetStatus",
        )

    class DeployedFleetAutoscaler(proto.Message):
        r"""Details about the Agones autoscaler.
        Attributes:
            autoscaler (str):
                The name of the Agones autoscaler.
            spec_source (google.cloud.gaming_v1beta.types.SpecSource):
                The source spec that is used to create the
                autoscaler. The GameServerConfig resource may no
                longer exist in the system.
            fleet_autoscaler_spec (str):
                The autoscaler spec retrieved from Agones.
        """

        autoscaler = proto.Field(proto.STRING, number=1,)
        spec_source = proto.Field(proto.MESSAGE, number=4, message="SpecSource",)
        fleet_autoscaler_spec = proto.Field(proto.STRING, number=3,)

    deployed_fleet = proto.Field(proto.MESSAGE, number=1, message=DeployedFleet,)
    deployed_autoscaler = proto.Field(
        proto.MESSAGE, number=2, message=DeployedFleetAutoscaler,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
