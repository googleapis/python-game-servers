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

import abc
import typing

from google import auth
from google.api_core import exceptions  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.gaming_v1beta.types import game_server_clusters
from google.longrunning import operations_pb2 as operations  # type: ignore


class GameServerClustersServiceTransport(abc.ABC):
    """Abstract transport class for GameServerClustersService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_game_server_clusters(
        self,
    ) -> typing.Callable[
        [game_server_clusters.ListGameServerClustersRequest],
        typing.Union[
            game_server_clusters.ListGameServerClustersResponse,
            typing.Awaitable[game_server_clusters.ListGameServerClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.GetGameServerClusterRequest],
        typing.Union[
            game_server_clusters.GameServerCluster,
            typing.Awaitable[game_server_clusters.GameServerCluster],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.CreateGameServerClusterRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_create_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.PreviewCreateGameServerClusterRequest],
        typing.Union[
            game_server_clusters.PreviewCreateGameServerClusterResponse,
            typing.Awaitable[
                game_server_clusters.PreviewCreateGameServerClusterResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.DeleteGameServerClusterRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_delete_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.PreviewDeleteGameServerClusterRequest],
        typing.Union[
            game_server_clusters.PreviewDeleteGameServerClusterResponse,
            typing.Awaitable[
                game_server_clusters.PreviewDeleteGameServerClusterResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.UpdateGameServerClusterRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_update_game_server_cluster(
        self,
    ) -> typing.Callable[
        [game_server_clusters.PreviewUpdateGameServerClusterRequest],
        typing.Union[
            game_server_clusters.PreviewUpdateGameServerClusterResponse,
            typing.Awaitable[
                game_server_clusters.PreviewUpdateGameServerClusterResponse
            ],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("GameServerClustersServiceTransport",)
