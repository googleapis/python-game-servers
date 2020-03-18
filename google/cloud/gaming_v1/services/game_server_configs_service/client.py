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

from collections import OrderedDict
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation
from google.cloud.gaming_v1.services.game_server_configs_service import pagers
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import game_server_configs
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from .transports.base import GameServerConfigsServiceTransport
from .transports.grpc import GameServerConfigsServiceGrpcTransport


class GameServerConfigsServiceClientMeta(type):
    """Metaclass for the GameServerConfigsService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[GameServerConfigsServiceTransport]]
    _transport_registry["grpc"] = GameServerConfigsServiceGrpcTransport

    def get_transport_class(
        cls, label: str = None
    ) -> Type[GameServerConfigsServiceTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class GameServerConfigsServiceClient(metaclass=GameServerConfigsServiceClientMeta):
    """The Game Server Config configures the game servers in an
    Agones fleet.
    """

    DEFAULT_OPTIONS = ClientOptions.ClientOptions(
        api_endpoint="gameservices.googleapis.com"
    )

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            {@api.name}: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @staticmethod
    def game_server_config_path(
        project: str, location: str, deployment: str, config: str
    ) -> str:
        """Return a fully-qualified game_server_config string."""
        return "projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}".format(
            project=project, location=location, deployment=deployment, config=config
        )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, GameServerConfigsServiceTransport] = None,
        client_options: ClientOptions = DEFAULT_OPTIONS,
    ) -> None:
        """Instantiate the game server configs service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.GameServerConfigsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, GameServerConfigsServiceTransport):
            if credentials:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                host=client_options.api_endpoint or "gameservices.googleapis.com",
            )

    def list_game_server_configs(
        self,
        request: game_server_configs.ListGameServerConfigsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListGameServerConfigsPager:
        r"""Lists Game Server Configs in a given project,
        Location, and Game Server Deployment.

        Args:
            request (:class:`~.game_server_configs.ListGameServerConfigsRequest`):
                The request object. Request message for
                GameServerConfigsService.ListGameServerConfigs.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/*``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListGameServerConfigsPager:
                Response message for
                GameServerConfigsService.ListGameServerConfigs.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_configs.ListGameServerConfigsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_game_server_configs,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListGameServerConfigsPager(
            method=rpc, request=request, response=response
        )

        # Done; return the response.
        return response

    def get_game_server_config(
        self,
        request: game_server_configs.GetGameServerConfigRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_configs.GameServerConfig:
        r"""Gets details of a single Game Server Config.

        Args:
            request (:class:`~.game_server_configs.GetGameServerConfigRequest`):
                The request object. Request message for
                GameServerConfigsService.GetGameServerConfig.
            name (:class:`str`):
                Required. The name of the Game Server Config to
                retrieve. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.game_server_configs.GameServerConfig:
                A Game Server Config resource.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_configs.GetGameServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_game_server_config,
            default_timeout=None,
            client_info=_client_info,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Done; return the response.
        return response

    def create_game_server_config(
        self,
        request: game_server_configs.CreateGameServerConfigRequest = None,
        *,
        parent: str = None,
        game_server_config: game_server_configs.GameServerConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Creates a new Game Server Config in a given project,
        Location, and Game Server Deployment. Game Server
        Configs are immutable, and are not applied until
        referenced in the Game Server Deployment Rollout
        resource.

        Args:
            request (:class:`~.game_server_configs.CreateGameServerConfigRequest`):
                The request object. Request message for
                GameServerConfigsService.CreateGameServerConfig.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            game_server_config (:class:`~.game_server_configs.GameServerConfig`):
                Required. The Game Server Config
                resource to be created.
                This corresponds to the ``game_server_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_configs.GameServerConfig``: A
                Game Server Config resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, game_server_config]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_configs.CreateGameServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if game_server_config is not None:
            request.game_server_config = game_server_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.create_game_server_config,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_configs.GameServerConfig,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_game_server_config(
        self,
        request: game_server_configs.DeleteGameServerConfigRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Game Server Config. The deletion
        will fail if the Game Server Config is referenced in a
        Game Server Deployment Rollout.

        Args:
            request (:class:`~.game_server_configs.DeleteGameServerConfigRequest`):
                The request object. Request message for
                GameServerConfigsService.DeleteGameServerConfig.
            name (:class:`str`):
                Required. The name of the Game Server Config to delete.
                Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/configs/{config}``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_configs.GameServerConfig``: A
                Game Server Config resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_configs.DeleteGameServerConfigRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_game_server_config,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_configs.GameServerConfig,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response


try:
    _client_info = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-game-servers"
        ).version
    )
except pkg_resources.DistributionNotFound:
    _client_info = gapic_v1.client_info.ClientInfo()


__all__ = ("GameServerConfigsServiceClient",)
