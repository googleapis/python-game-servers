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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.gaming_v1.types import game_server_clusters
from google.longrunning import operations_pb2  # type: ignore
from .base import GameServerClustersServiceTransport, DEFAULT_CLIENT_INFO


class GameServerClustersServiceGrpcTransport(GameServerClustersServiceTransport):
    """gRPC backend transport for GameServerClustersService.

    The game server cluster maps to Kubernetes clusters running
    Agones and is used to manage fleets within clusters.

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
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
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
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "gameservices.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
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
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def list_game_server_clusters(
        self,
    ) -> Callable[
        [game_server_clusters.ListGameServerClustersRequest],
        game_server_clusters.ListGameServerClustersResponse,
    ]:
        r"""Return a callable for the list game server clusters method over gRPC.

        Lists game server clusters in a given project and
        location.

        Returns:
            Callable[[~.ListGameServerClustersRequest],
                    ~.ListGameServerClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_game_server_clusters" not in self._stubs:
            self._stubs["list_game_server_clusters"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/ListGameServerClusters",
                request_serializer=game_server_clusters.ListGameServerClustersRequest.serialize,
                response_deserializer=game_server_clusters.ListGameServerClustersResponse.deserialize,
            )
        return self._stubs["list_game_server_clusters"]

    @property
    def get_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.GetGameServerClusterRequest],
        game_server_clusters.GameServerCluster,
    ]:
        r"""Return a callable for the get game server cluster method over gRPC.

        Gets details of a single game server cluster.

        Returns:
            Callable[[~.GetGameServerClusterRequest],
                    ~.GameServerCluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_game_server_cluster" not in self._stubs:
            self._stubs["get_game_server_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/GetGameServerCluster",
                request_serializer=game_server_clusters.GetGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.GameServerCluster.deserialize,
            )
        return self._stubs["get_game_server_cluster"]

    @property
    def create_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.CreateGameServerClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create game server cluster method over gRPC.

        Creates a new game server cluster in a given project
        and location.

        Returns:
            Callable[[~.CreateGameServerClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_game_server_cluster" not in self._stubs:
            self._stubs["create_game_server_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/CreateGameServerCluster",
                request_serializer=game_server_clusters.CreateGameServerClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_game_server_cluster"]

    @property
    def preview_create_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.PreviewCreateGameServerClusterRequest],
        game_server_clusters.PreviewCreateGameServerClusterResponse,
    ]:
        r"""Return a callable for the preview create game server
        cluster method over gRPC.

        Previews creation of a new game server cluster in a
        given project and location.

        Returns:
            Callable[[~.PreviewCreateGameServerClusterRequest],
                    ~.PreviewCreateGameServerClusterResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_create_game_server_cluster" not in self._stubs:
            self._stubs[
                "preview_create_game_server_cluster"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/PreviewCreateGameServerCluster",
                request_serializer=game_server_clusters.PreviewCreateGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewCreateGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_create_game_server_cluster"]

    @property
    def delete_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.DeleteGameServerClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete game server cluster method over gRPC.

        Deletes a single game server cluster.

        Returns:
            Callable[[~.DeleteGameServerClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_game_server_cluster" not in self._stubs:
            self._stubs["delete_game_server_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/DeleteGameServerCluster",
                request_serializer=game_server_clusters.DeleteGameServerClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_game_server_cluster"]

    @property
    def preview_delete_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.PreviewDeleteGameServerClusterRequest],
        game_server_clusters.PreviewDeleteGameServerClusterResponse,
    ]:
        r"""Return a callable for the preview delete game server
        cluster method over gRPC.

        Previews deletion of a single game server cluster.

        Returns:
            Callable[[~.PreviewDeleteGameServerClusterRequest],
                    ~.PreviewDeleteGameServerClusterResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_delete_game_server_cluster" not in self._stubs:
            self._stubs[
                "preview_delete_game_server_cluster"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/PreviewDeleteGameServerCluster",
                request_serializer=game_server_clusters.PreviewDeleteGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewDeleteGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_delete_game_server_cluster"]

    @property
    def update_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.UpdateGameServerClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update game server cluster method over gRPC.

        Patches a single game server cluster.

        Returns:
            Callable[[~.UpdateGameServerClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_game_server_cluster" not in self._stubs:
            self._stubs["update_game_server_cluster"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/UpdateGameServerCluster",
                request_serializer=game_server_clusters.UpdateGameServerClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_game_server_cluster"]

    @property
    def preview_update_game_server_cluster(
        self,
    ) -> Callable[
        [game_server_clusters.PreviewUpdateGameServerClusterRequest],
        game_server_clusters.PreviewUpdateGameServerClusterResponse,
    ]:
        r"""Return a callable for the preview update game server
        cluster method over gRPC.

        Previews updating a GameServerCluster.

        Returns:
            Callable[[~.PreviewUpdateGameServerClusterRequest],
                    ~.PreviewUpdateGameServerClusterResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_update_game_server_cluster" not in self._stubs:
            self._stubs[
                "preview_update_game_server_cluster"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1.GameServerClustersService/PreviewUpdateGameServerCluster",
                request_serializer=game_server_clusters.PreviewUpdateGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewUpdateGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_update_game_server_cluster"]


__all__ = ("GameServerClustersServiceGrpcTransport",)
