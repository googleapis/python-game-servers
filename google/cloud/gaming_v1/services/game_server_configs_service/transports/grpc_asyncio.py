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

from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.gaming_v1.types import game_server_configs
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import GameServerConfigsServiceTransport
from .grpc import GameServerConfigsServiceGrpcTransport


class GameServerConfigsServiceGrpcAsyncIOTransport(GameServerConfigsServiceTransport):
    """gRPC AsyncIO backend transport for GameServerConfigsService.

    The Game Server Config configures the game servers in an
    Agones fleet.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        scopes: Optional[Sequence[str]] = None,
        **kwargs
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host, credentials=credentials, scopes=scopes, **kwargs
        )

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None
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
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.

        Raises:
          google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                ssl_credentials=ssl_credentials,
                scopes=self.AUTH_SCOPES,
            )

        # Run the base constructor.
        super().__init__(host=host, credentials=credentials)
        self._stubs = {}

    @property
    def grpc_channel(self) -> aio.Channel:
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
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def list_game_server_configs(
        self
    ) -> Callable[
        [game_server_configs.ListGameServerConfigsRequest],
        Awaitable[game_server_configs.ListGameServerConfigsResponse],
    ]:
        r"""Return a callable for the list game server configs method over gRPC.

        Lists Game Server Configs in a given project,
        Location, and Game Server Deployment.

        Returns:
            Callable[[~.ListGameServerConfigsRequest],
                    Awaitable[~.ListGameServerConfigsResponse]]:
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
        Awaitable[game_server_configs.GameServerConfig],
    ]:
        r"""Return a callable for the get game server config method over gRPC.

        Gets details of a single Game Server Config.

        Returns:
            Callable[[~.GetGameServerConfigRequest],
                    Awaitable[~.GameServerConfig]]:
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
        [game_server_configs.CreateGameServerConfigRequest],
        Awaitable[operations.Operation],
    ]:
        r"""Return a callable for the create game server config method over gRPC.

        Creates a new Game Server Config in a given project,
        Location, and Game Server Deployment. Game Server
        Configs are immutable, and are not applied until
        referenced in the Game Server Deployment Rollout
        resource.

        Returns:
            Callable[[~.CreateGameServerConfigRequest],
                    Awaitable[~.Operation]]:
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
        [game_server_configs.DeleteGameServerConfigRequest],
        Awaitable[operations.Operation],
    ]:
        r"""Return a callable for the delete game server config method over gRPC.

        Deletes a single Game Server Config. The deletion
        will fail if the Game Server Config is referenced in a
        Game Server Deployment Rollout.

        Returns:
            Callable[[~.DeleteGameServerConfigRequest],
                    Awaitable[~.Operation]]:
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


__all__ = ("GameServerConfigsServiceGrpcAsyncIOTransport",)
