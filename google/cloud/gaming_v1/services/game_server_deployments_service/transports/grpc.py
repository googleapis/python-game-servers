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

from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore


import grpc  # type: ignore

from google.cloud.gaming_v1.types import game_server_deployments
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import GameServerDeploymentsServiceTransport


class GameServerDeploymentsServiceGrpcTransport(GameServerDeploymentsServiceTransport):
    """gRPC backend transport for GameServerDeploymentsService.

    The game server deployment is used to control the deployment
    of Agones fleets.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
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
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
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
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
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

            if credentials is None:
                credentials, _ = auth.default(scopes=self.AUTH_SCOPES)

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
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
        )

        self._stubs = {}  # type: Dict[str, Callable]

    @classmethod
    def create_channel(
        cls,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
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
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            **kwargs
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
                self._host, credentials=self._credentials,
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
        self,
    ) -> Callable[
        [game_server_deployments.ListGameServerDeploymentsRequest],
        game_server_deployments.ListGameServerDeploymentsResponse,
    ]:
        r"""Return a callable for the list game server deployments method over gRPC.

        Lists game server deployments in a given project and
        location.

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
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRequest],
        game_server_deployments.GameServerDeployment,
    ]:
        r"""Return a callable for the get game server deployment method over gRPC.

        Gets details of a single game server deployment.

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
        self,
    ) -> Callable[
        [game_server_deployments.CreateGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the create game server deployment method over gRPC.

        Creates a new game server deployment in a given
        project and location.

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
        self,
    ) -> Callable[
        [game_server_deployments.DeleteGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the delete game server deployment method over gRPC.

        Deletes a single game server deployment.

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
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the update game server deployment method over gRPC.

        Patches a game server deployment.

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
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRolloutRequest],
        game_server_deployments.GameServerDeploymentRollout,
    ]:
        r"""Return a callable for the get game server deployment
        rollout method over gRPC.

        Gets details a single game server deployment rollout.

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
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRolloutRequest],
        operations.Operation,
    ]:
        r"""Return a callable for the update game server deployment
        rollout method over gRPC.

        Patches a single game server deployment rollout. The method will
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
        self,
    ) -> Callable[
        [game_server_deployments.PreviewGameServerDeploymentRolloutRequest],
        game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
    ]:
        r"""Return a callable for the preview game server deployment
        rollout method over gRPC.

        Previews the game server deployment rollout. This API
        does not mutate the rollout resource.

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
        self,
    ) -> Callable[
        [game_server_deployments.FetchDeploymentStateRequest],
        game_server_deployments.FetchDeploymentStateResponse,
    ]:
        r"""Return a callable for the fetch deployment state method over gRPC.

        Retrieves information about the current state of the
        game server deployment. Gathers all the Agones fleets
        and Agones autoscalers, including fleets running an
        older version of the game server deployment.

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
