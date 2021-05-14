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
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.gaming_v1beta.services.game_server_deployments_service import pagers
from google.cloud.gaming_v1beta.types import common
from google.cloud.gaming_v1beta.types import game_server_deployments
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import GameServerDeploymentsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import GameServerDeploymentsServiceGrpcAsyncIOTransport
from .client import GameServerDeploymentsServiceClient


class GameServerDeploymentsServiceAsyncClient:
    """The game server deployment is used to control the deployment
    of Agones fleets.
    """

    _client: GameServerDeploymentsServiceClient

    DEFAULT_ENDPOINT = GameServerDeploymentsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GameServerDeploymentsServiceClient.DEFAULT_MTLS_ENDPOINT

    game_server_deployment_path = staticmethod(
        GameServerDeploymentsServiceClient.game_server_deployment_path
    )
    parse_game_server_deployment_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_game_server_deployment_path
    )
    game_server_deployment_rollout_path = staticmethod(
        GameServerDeploymentsServiceClient.game_server_deployment_rollout_path
    )
    parse_game_server_deployment_rollout_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_game_server_deployment_rollout_path
    )
    common_billing_account_path = staticmethod(
        GameServerDeploymentsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        GameServerDeploymentsServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        GameServerDeploymentsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        GameServerDeploymentsServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        GameServerDeploymentsServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        GameServerDeploymentsServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            GameServerDeploymentsServiceAsyncClient: The constructed client.
        """
        return GameServerDeploymentsServiceClient.from_service_account_info.__func__(GameServerDeploymentsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            GameServerDeploymentsServiceAsyncClient: The constructed client.
        """
        return GameServerDeploymentsServiceClient.from_service_account_file.__func__(GameServerDeploymentsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> GameServerDeploymentsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            GameServerDeploymentsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(GameServerDeploymentsServiceClient).get_transport_class,
        type(GameServerDeploymentsServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, GameServerDeploymentsServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the game server deployments service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.GameServerDeploymentsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = GameServerDeploymentsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_game_server_deployments(
        self,
        request: game_server_deployments.ListGameServerDeploymentsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListGameServerDeploymentsAsyncPager:
        r"""Lists game server deployments in a given project and
        location.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.ListGameServerDeploymentsRequest`):
                The request object. Request message for
                GameServerDeploymentsService.ListGameServerDeployments.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1beta.services.game_server_deployments_service.pagers.ListGameServerDeploymentsAsyncPager:
                Response message for
                GameServerDeploymentsService.ListGameServerDeployments.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.ListGameServerDeploymentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_game_server_deployments,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListGameServerDeploymentsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_game_server_deployment(
        self,
        request: game_server_deployments.GetGameServerDeploymentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.GameServerDeployment:
        r"""Gets details of a single game server deployment.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.GetGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.GetGameServerDeployment.
            name (:class:`str`):
                Required. The name of the game server delpoyment to
                retrieve. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1beta.types.GameServerDeployment:
                A game server deployment resource.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.GetGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_game_server_deployment,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_game_server_deployment(
        self,
        request: game_server_deployments.CreateGameServerDeploymentRequest = None,
        *,
        parent: str = None,
        game_server_deployment: game_server_deployments.GameServerDeployment = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new game server deployment in a given
        project and location.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.CreateGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.CreateGameServerDeployment.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            game_server_deployment (:class:`google.cloud.gaming_v1beta.types.GameServerDeployment`):
                Required. The game server delpoyment
                resource to be created.

                This corresponds to the ``game_server_deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gaming_v1beta.types.GameServerDeployment`
                A game server deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, game_server_deployment])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.CreateGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if game_server_deployment is not None:
            request.game_server_deployment = game_server_deployment

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_game_server_deployment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_game_server_deployment(
        self,
        request: game_server_deployments.DeleteGameServerDeploymentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a single game server deployment.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.DeleteGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.DeleteGameServerDeployment.
            name (:class:`str`):
                Required. The name of the game server delpoyment to
                delete. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.DeleteGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_game_server_deployment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_game_server_deployment(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRequest = None,
        *,
        game_server_deployment: game_server_deployments.GameServerDeployment = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Patches a game server deployment.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.UpdateGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.UpdateGameServerDeployment.
                Only allows updates for labels.
            game_server_deployment (:class:`google.cloud.gaming_v1beta.types.GameServerDeployment`):
                Required. The game server delpoyment to be updated. Only
                fields specified in update_mask are updated.

                This corresponds to the ``game_server_deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. For the ``FieldMask``
                definition, see

                https: //developers.google.com/protocol-buffers //
                /docs/reference/google.protobuf#fieldmask

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gaming_v1beta.types.GameServerDeployment`
                A game server deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([game_server_deployment, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.UpdateGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if game_server_deployment is not None:
            request.game_server_deployment = game_server_deployment
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_game_server_deployment,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("game_server_deployment.name", request.game_server_deployment.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_game_server_deployment_rollout(
        self,
        request: game_server_deployments.GetGameServerDeploymentRolloutRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.GameServerDeploymentRollout:
        r"""Gets details a single game server deployment rollout.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.GetGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                GameServerDeploymentsService.GetGameServerDeploymentRollout.
            name (:class:`str`):
                Required. The name of the game server delpoyment to
                retrieve. Uses the form:

                ``projects/{project}/locations/{location}/gameServerDeployments/{deployment}/rollout``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1beta.types.GameServerDeploymentRollout:
                The game server deployment rollout
                which represents the desired rollout
                state.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.GetGameServerDeploymentRolloutRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_game_server_deployment_rollout,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_game_server_deployment_rollout(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRolloutRequest = None,
        *,
        rollout: game_server_deployments.GameServerDeploymentRollout = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Patches a single game server deployment rollout. The method will
        not return an error if the update does not affect any existing
        realms. For example - if the default_game_server_config is
        changed but all existing realms use the override, that is valid.
        Similarly, if a non existing realm is explicitly called out in
        game_server_config_overrides field, that will also not result in
        an error.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.UpdateGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                GameServerDeploymentsService.UpdateGameServerRolloutDeployment.
            rollout (:class:`google.cloud.gaming_v1beta.types.GameServerDeploymentRollout`):
                Required. The game server delpoyment rollout to be
                updated. Only fields specified in update_mask are
                updated.

                This corresponds to the ``rollout`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. For the ``FieldMask``
                definition, see

                https: //developers.google.com/protocol-buffers //
                /docs/reference/google.protobuf#fieldmask

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.gaming_v1beta.types.GameServerDeployment`
                A game server deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([rollout, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.UpdateGameServerDeploymentRolloutRequest(
            request
        )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if rollout is not None:
            request.rollout = rollout
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_game_server_deployment_rollout,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("rollout.name", request.rollout.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def preview_game_server_deployment_rollout(
        self,
        request: game_server_deployments.PreviewGameServerDeploymentRolloutRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.PreviewGameServerDeploymentRolloutResponse:
        r"""Previews the game server deployment rollout. This API
        does not mutate the rollout resource.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.PreviewGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                PreviewGameServerDeploymentRollout.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1beta.types.PreviewGameServerDeploymentRolloutResponse:
                Response message for
                PreviewGameServerDeploymentRollout. This
                has details about the Agones fleet and
                autoscaler to be actuated.

        """
        # Create or coerce a protobuf request object.
        request = game_server_deployments.PreviewGameServerDeploymentRolloutRequest(
            request
        )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.preview_game_server_deployment_rollout,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("rollout.name", request.rollout.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def fetch_deployment_state(
        self,
        request: game_server_deployments.FetchDeploymentStateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.FetchDeploymentStateResponse:
        r"""Retrieves information about the current state of the
        game server deployment. Gathers all the Agones fleets
        and Agones autoscalers, including fleets running an
        older version of the game server deployment.

        Args:
            request (:class:`google.cloud.gaming_v1beta.types.FetchDeploymentStateRequest`):
                The request object. Request message for
                GameServerDeploymentsService.FetchDeploymentState.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.gaming_v1beta.types.FetchDeploymentStateResponse:
                Response message for
                GameServerDeploymentsService.FetchDeploymentState.

        """
        # Create or coerce a protobuf request object.
        request = game_server_deployments.FetchDeploymentStateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.fetch_deployment_state,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-game-servers",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("GameServerDeploymentsServiceAsyncClient",)
