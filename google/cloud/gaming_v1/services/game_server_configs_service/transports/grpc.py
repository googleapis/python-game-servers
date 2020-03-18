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

from google.cloud.gaming_v1.types import game_server_configs
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import GameServerConfigsServiceTransport


class GameServerConfigsServiceGrpcTransport(GameServerConfigsServiceTransport):
    """gRPC backend transport for GameServerConfigsService.

    The Game Server Config configures the game servers in an
    Agones fleet.

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
    def list_game_server_configs(
        self
    ) -> Callable[
        [game_server_configs.ListGameServerConfigsRequest],
        game_server_configs.ListGameServerConfigsResponse,
    ]:
        r"""Return a callable for the list game server configs method over gRPC.

        Lists Game Server Configs in a given project,
        Location, and Game Server Deployment.

        Returns:
            Callable[[~.ListGameServerConfigsRequest],
                    ~.ListGameServerConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_game_server_configs" not in self._stubs:
            self._stubs["list_game_server_configs"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerConfigsService/ListGameServerConfigs",
                request_serializer=game_server_configs.ListGameServerConfigsRequest.serialize,
                response_deserializer=game_server_configs.ListGameServerConfigsResponse.deserialize,
            )
        return self._stubs["list_game_server_configs"]

    @property
    def get_game_server_config(
        self
    ) -> Callable[
        [game_server_configs.GetGameServerConfigRequest],
        game_server_configs.GameServerConfig,
    ]:
        r"""Return a callable for the get game server config method over gRPC.

        Gets details of a single Game Server Config.

        Returns:
            Callable[[~.GetGameServerConfigRequest],
                    ~.GameServerConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_game_server_config" not in self._stubs:
            self._stubs["get_game_server_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerConfigsService/GetGameServerConfig",
                request_serializer=game_server_configs.GetGameServerConfigRequest.serialize,
                response_deserializer=game_server_configs.GameServerConfig.deserialize,
            )
        return self._stubs["get_game_server_config"]

    @property
    def create_game_server_config(
        self
    ) -> Callable[
        [game_server_configs.CreateGameServerConfigRequest], operations.Operation
    ]:
        r"""Return a callable for the create game server config method over gRPC.

        Creates a new Game Server Config in a given project,
        Location, and Game Server Deployment. Game Server
        Configs are immutable, and are not applied until
        referenced in the Game Server Deployment Rollout
        resource.

        Returns:
            Callable[[~.CreateGameServerConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_game_server_config" not in self._stubs:
            self._stubs["create_game_server_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerConfigsService/CreateGameServerConfig",
                request_serializer=game_server_configs.CreateGameServerConfigRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_game_server_config"]

    @property
    def delete_game_server_config(
        self
    ) -> Callable[
        [game_server_configs.DeleteGameServerConfigRequest], operations.Operation
    ]:
        r"""Return a callable for the delete game server config method over gRPC.

        Deletes a single Game Server Config. The deletion
        will fail if the Game Server Config is referenced in a
        Game Server Deployment Rollout.

        Returns:
            Callable[[~.DeleteGameServerConfigRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_game_server_config" not in self._stubs:
            self._stubs["delete_game_server_config"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.GameServerConfigsService/DeleteGameServerConfig",
                request_serializer=game_server_configs.DeleteGameServerConfigRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_game_server_config"]


__all__ = ("GameServerConfigsServiceGrpcTransport",)
