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

from google.cloud.gaming_v1.types import game_server_clusters
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import GameServerClustersServiceTransport


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
    def list_game_server_clusters(
        self
    ) -> Callable[
        [game_server_clusters.ListGameServerClustersRequest],
        game_server_clusters.ListGameServerClustersResponse,
    ]:
        r"""Return a callable for the list game server clusters method over gRPC.

        Lists Game Server Clusters in a given project and
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/ListGameServerClusters",
                request_serializer=game_server_clusters.ListGameServerClustersRequest.serialize,
                response_deserializer=game_server_clusters.ListGameServerClustersResponse.deserialize,
            )
        return self._stubs["list_game_server_clusters"]

    @property
    def get_game_server_cluster(
        self
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/GetGameServerCluster",
                request_serializer=game_server_clusters.GetGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.GameServerCluster.deserialize,
            )
        return self._stubs["get_game_server_cluster"]

    @property
    def create_game_server_cluster(
        self
    ) -> Callable[
        [game_server_clusters.CreateGameServerClusterRequest], operations.Operation
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/CreateGameServerCluster",
                request_serializer=game_server_clusters.CreateGameServerClusterRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_game_server_cluster"]

    @property
    def preview_create_game_server_cluster(
        self
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/PreviewCreateGameServerCluster",
                request_serializer=game_server_clusters.PreviewCreateGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewCreateGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_create_game_server_cluster"]

    @property
    def delete_game_server_cluster(
        self
    ) -> Callable[
        [game_server_clusters.DeleteGameServerClusterRequest], operations.Operation
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/DeleteGameServerCluster",
                request_serializer=game_server_clusters.DeleteGameServerClusterRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_game_server_cluster"]

    @property
    def preview_delete_game_server_cluster(
        self
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/PreviewDeleteGameServerCluster",
                request_serializer=game_server_clusters.PreviewDeleteGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewDeleteGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_delete_game_server_cluster"]

    @property
    def update_game_server_cluster(
        self
    ) -> Callable[
        [game_server_clusters.UpdateGameServerClusterRequest], operations.Operation
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/UpdateGameServerCluster",
                request_serializer=game_server_clusters.UpdateGameServerClusterRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["update_game_server_cluster"]

    @property
    def preview_update_game_server_cluster(
        self
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
                "/google.cloud.gaming.v1beta.GameServerClustersService/PreviewUpdateGameServerCluster",
                request_serializer=game_server_clusters.PreviewUpdateGameServerClusterRequest.serialize,
                response_deserializer=game_server_clusters.PreviewUpdateGameServerClusterResponse.deserialize,
            )
        return self._stubs["preview_update_game_server_cluster"]


__all__ = ("GameServerClustersServiceGrpcTransport",)
