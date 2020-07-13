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

from google.cloud.gaming_v1.types import game_server_deployments
from google.longrunning import operations_pb2 as operations  # type: ignore


class GameServerDeploymentsServiceTransport(abc.ABC):
    """Abstract transport class for GameServerDeploymentsService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
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
                credentials_file, scopes=scopes
            )
        elif credentials is None:
            credentials, _ = auth.default(scopes=scopes)

        # Save the credentials.
        self._credentials = credentials

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_game_server_deployments(
        self,
    ) -> typing.Callable[
        [game_server_deployments.ListGameServerDeploymentsRequest],
        typing.Union[
            game_server_deployments.ListGameServerDeploymentsResponse,
            typing.Awaitable[game_server_deployments.ListGameServerDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_game_server_deployment(
        self,
    ) -> typing.Callable[
        [game_server_deployments.GetGameServerDeploymentRequest],
        typing.Union[
            game_server_deployments.GameServerDeployment,
            typing.Awaitable[game_server_deployments.GameServerDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_game_server_deployment(
        self,
    ) -> typing.Callable[
        [game_server_deployments.CreateGameServerDeploymentRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_game_server_deployment(
        self,
    ) -> typing.Callable[
        [game_server_deployments.DeleteGameServerDeploymentRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_game_server_deployment(
        self,
    ) -> typing.Callable[
        [game_server_deployments.UpdateGameServerDeploymentRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_game_server_deployment_rollout(
        self,
    ) -> typing.Callable[
        [game_server_deployments.GetGameServerDeploymentRolloutRequest],
        typing.Union[
            game_server_deployments.GameServerDeploymentRollout,
            typing.Awaitable[game_server_deployments.GameServerDeploymentRollout],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_game_server_deployment_rollout(
        self,
    ) -> typing.Callable[
        [game_server_deployments.UpdateGameServerDeploymentRolloutRequest],
        typing.Union[operations.Operation, typing.Awaitable[operations.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_game_server_deployment_rollout(
        self,
    ) -> typing.Callable[
        [game_server_deployments.PreviewGameServerDeploymentRolloutRequest],
        typing.Union[
            game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
            typing.Awaitable[
                game_server_deployments.PreviewGameServerDeploymentRolloutResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_deployment_state(
        self,
    ) -> typing.Callable[
        [game_server_deployments.FetchDeploymentStateRequest],
        typing.Union[
            game_server_deployments.FetchDeploymentStateResponse,
            typing.Awaitable[game_server_deployments.FetchDeploymentStateResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("GameServerDeploymentsServiceTransport",)
