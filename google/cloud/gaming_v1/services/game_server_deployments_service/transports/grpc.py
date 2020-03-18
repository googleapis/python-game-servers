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

from typing import Callable, Dict

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore

import grpc  # type: ignore

from google.cloud.gaming_v1.types import game_server_deployments
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import GameServerDeploymentsServiceTransport


class GameServerDeploymentsServiceGrpcTransport(GameServerDeploymentsServiceTransport):
    """gRPC backend transport for GameServerDeploymentsService.

    The Game Server Deployment is used to control the deployment
    of Agones fleets.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        channel: grpc.Channel = None
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
        """
        # Sanity check: Ensure that channel and credentials are not both
        # provided.
        if channel:
            credentials = False

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}  # type: Dict[str, Callable]

        # If a channel was explicitly provided, set it.
        if channel:
            self._grpc_channel = channel

    @classmethod
    def create_channel(
        cls,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        **kwargs
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return grpc_helpers.create_channel(
            host, credentials=credentials, scopes=cls.AUTH_SCOPES, **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = self.create_channel(
                self._host, credentials=self._credentials
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def list_game_server_deployments(
        self
    ) -> Callable[
        [game_server_deployments.ListGameServerDeploymentsRequest],
        game_server_deployments.ListGameServerDeploymentsResponse,
    ]:
        r"""Return a callable for the list game server deployments method over gRPC.

        Lists Game Server Deployments in a given project and
        Location.

        Returns:
            Callable[[~.ListGameServerDeploymentsRequest],
                    ~.ListGameServerDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_game_server_deployments" not in self._stubs:
            self._stubs["list_game_server_deployments"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/ListGameServerDeployments",
                request_serializer=game_server_deployments.ListGameServerDeploymentsRequest.serialize,
                response_deserializer=game_server_deployments.ListGameServerDeploymentsResponse.deserialize,
            )
        return self._stubs["list_game_server_deployments"]

    @property
    def get_game_server_deployment(
        self
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRequest],
        game_server_deployments.GameServerDeployment,
    ]:
        r"""Return a callable for the get game server deployment method over gRPC.

        Gets details of a single Game Server Deployment.

        Returns:
            Callable[[~.GetGameServerDeploymentRequest],
                    ~.GameServerDeployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_game_server_deployment" not in self._stubs:
            self._stubs["get_game_server_deployment"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/GetGameServerDeployment",
                request_serializer=game_server_deployments.GetGameServerDeploymentRequest.serialize,
                response_deserializer=game_server_deployments.GameServerDeployment.deserialize,
            )
        return self._stubs["get_game_server_deployment"]

    @property
    def create_game_server_deployment(
        self
    ) -> Callable[
        [game_server_deployments.CreateGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the create game server deployment method over gRPC.

        Creates a new Game Server Deployment in a given
        project and Location.

        Returns:
            Callable[[~.CreateGameServerDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_game_server_deployment" not in self._stubs:
            self._stubs[
                "create_game_server_deployment"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/CreateGameServerDeployment",
                request_serializer=game_server_deployments.CreateGameServerDeploymentRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_game_server_deployment"]

    @property
    def delete_game_server_deployment(
        self
    ) -> Callable[
        [game_server_deployments.DeleteGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the delete game server deployment method over gRPC.

        Deletes a single Game Server Deployment.

        Returns:
            Callable[[~.DeleteGameServerDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_game_server_deployment" not in self._stubs:
            self._stubs[
                "delete_game_server_deployment"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/DeleteGameServerDeployment",
                request_serializer=game_server_deployments.DeleteGameServerDeploymentRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_game_server_deployment"]

    @property
    def update_game_server_deployment(
        self
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the update game server deployment method over gRPC.

        Patches a Game Server Deployment.

        Returns:
            Callable[[~.UpdateGameServerDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_game_server_deployment" not in self._stubs:
            self._stubs[
                "update_game_server_deployment"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/UpdateGameServerDeployment",
                request_serializer=game_server_deployments.UpdateGameServerDeploymentRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["update_game_server_deployment"]

    @property
    def get_game_server_deployment_rollout(
        self
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRolloutRequest],
        game_server_deployments.GameServerDeploymentRollout,
    ]:
        r"""Return a callable for the get game server deployment
        rollout method over gRPC.

        Gets details a single Game Server Deployment Rollout.

        Returns:
            Callable[[~.GetGameServerDeploymentRolloutRequest],
                    ~.GameServerDeploymentRollout]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_game_server_deployment_rollout" not in self._stubs:
            self._stubs[
                "get_game_server_deployment_rollout"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/GetGameServerDeploymentRollout",
                request_serializer=game_server_deployments.GetGameServerDeploymentRolloutRequest.serialize,
                response_deserializer=game_server_deployments.GameServerDeploymentRollout.deserialize,
            )
        return self._stubs["get_game_server_deployment_rollout"]

    @property
    def update_game_server_deployment_rollout(
        self
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRolloutRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the update game server deployment
        rollout method over gRPC.

        Patches a single Game Server Deployment Rollout. The method will
        not return an error if the update does not affect any existing
        realms. For example - if the default_game_server_config is
        changed but all existing realms use the override, that is valid.
        Similarly, if a non existing realm is explicitly called out in
        game_server_config_overrides field, that will also not result in
        an error.

        Returns:
            Callable[[~.UpdateGameServerDeploymentRolloutRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_game_server_deployment_rollout" not in self._stubs:
            self._stubs[
                "update_game_server_deployment_rollout"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/UpdateGameServerDeploymentRollout",
                request_serializer=game_server_deployments.UpdateGameServerDeploymentRolloutRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["update_game_server_deployment_rollout"]

    @property
    def preview_game_server_deployment_rollout(
        self
    ) -> Callable[
        [game_server_deployments.PreviewGameServerDeploymentRolloutRequest],
        game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
    ]:
        r"""Return a callable for the preview game server deployment
        rollout method over gRPC.

        Previews the Game Server Deployment Rollout. This API
        does not mutate the Rollout resource.

        Returns:
            Callable[[~.PreviewGameServerDeploymentRolloutRequest],
                    ~.PreviewGameServerDeploymentRolloutResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_game_server_deployment_rollout" not in self._stubs:
            self._stubs[
                "preview_game_server_deployment_rollout"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/PreviewGameServerDeploymentRollout",
                request_serializer=game_server_deployments.PreviewGameServerDeploymentRolloutRequest.serialize,
                response_deserializer=game_server_deployments.PreviewGameServerDeploymentRolloutResponse.deserialize,
            )
        return self._stubs["preview_game_server_deployment_rollout"]

    @property
    def fetch_deployment_state(
        self
    ) -> Callable[
        [game_server_deployments.FetchDeploymentStateRequest],
        game_server_deployments.FetchDeploymentStateResponse,
    ]:
        r"""Return a callable for the fetch deployment state method over gRPC.

        Retrieves information about the current state of the
        Game Server Ddeployment. Gathers all the Agones fleets
        and Agones autoscalers, including fleets running an
        older version of the Game Server Deployment.

        Returns:
            Callable[[~.FetchDeploymentStateRequest],
                    ~.FetchDeploymentStateResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_deployment_state" not in self._stubs:
            self._stubs["fetch_deployment_state"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerDeploymentsService/FetchDeploymentState",
                request_serializer=game_server_deployments.FetchDeploymentStateRequest.serialize,
                response_deserializer=game_server_deployments.FetchDeploymentStateResponse.deserialize,
            )
        return self._stubs["fetch_deployment_state"]


__all__ = ("GameServerDeploymentsServiceGrpcTransport",)
