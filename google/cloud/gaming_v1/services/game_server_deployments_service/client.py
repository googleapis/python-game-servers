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
from google.cloud.gaming_v1.services.game_server_deployments_service import pagers
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import game_server_deployments
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from .transports.base import GameServerDeploymentsServiceTransport
from .transports.grpc import GameServerDeploymentsServiceGrpcTransport


class GameServerDeploymentsServiceClientMeta(type):
    """Metaclass for the GameServerDeploymentsService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = (
        OrderedDict()
    )  # type: Dict[str, Type[GameServerDeploymentsServiceTransport]]
    _transport_registry["grpc"] = GameServerDeploymentsServiceGrpcTransport

    def get_transport_class(
        cls, label: str = None
    ) -> Type[GameServerDeploymentsServiceTransport]:
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


class GameServerDeploymentsServiceClient(
    metaclass=GameServerDeploymentsServiceClientMeta
):
    """The Game Server Deployment is used to control the deployment
    of Agones fleets.
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
    def game_server_deployment_path(
        project: str, location: str, deployment: str
    ) -> str:
        """Return a fully-qualified game_server_deployment string."""
        return "projects/{project}/locations/{location}/gameServerDeployments/{deployment}".format(
            project=project, location=location, deployment=deployment
        )

    @staticmethod
    def game_server_deployment_rollout_path(
        project: str, location: str, deployment: str
    ) -> str:
        """Return a fully-qualified game_server_deployment_rollout string."""
        return "projects/{project}/locations/{location}/gameServerDeployments/{deployment}/rollout".format(
            project=project, location=location, deployment=deployment
        )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, GameServerDeploymentsServiceTransport] = None,
        client_options: ClientOptions = DEFAULT_OPTIONS,
    ) -> None:
        """Instantiate the game server deployments service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.GameServerDeploymentsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, GameServerDeploymentsServiceTransport):
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

    def list_game_server_deployments(
        self,
        request: game_server_deployments.ListGameServerDeploymentsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListGameServerDeploymentsPager:
        r"""Lists Game Server Deployments in a given project and
        Location.

        Args:
            request (:class:`~.game_server_deployments.ListGameServerDeploymentsRequest`):
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
            ~.pagers.ListGameServerDeploymentsPager:
                Response message for
                GameServerDeploymentsService.ListGameServerDeployments.
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

        request = game_server_deployments.ListGameServerDeploymentsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_game_server_deployments,
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
        response = pagers.ListGameServerDeploymentsPager(
            method=rpc, request=request, response=response
        )

        # Done; return the response.
        return response

    def get_game_server_deployment(
        self,
        request: game_server_deployments.GetGameServerDeploymentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.GameServerDeployment:
        r"""Gets details of a single Game Server Deployment.

        Args:
            request (:class:`~.game_server_deployments.GetGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.GetGameServerDeployment.
            name (:class:`str`):
                Required. The name of the Game Server Deployment to
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
            ~.game_server_deployments.GameServerDeployment:
                A Game Server Deployment resource.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
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
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_game_server_deployment,
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

    def create_game_server_deployment(
        self,
        request: game_server_deployments.CreateGameServerDeploymentRequest = None,
        *,
        parent: str = None,
        game_server_deployment: game_server_deployments.GameServerDeployment = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Creates a new Game Server Deployment in a given
        project and Location.

        Args:
            request (:class:`~.game_server_deployments.CreateGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.CreateGameServerDeployment.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:
                ``projects/{project}/locations/{location}``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            game_server_deployment (:class:`~.game_server_deployments.GameServerDeployment`):
                Required. The Game Server Deployment
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_deployments.GameServerDeployment``:
                A Game Server Deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, game_server_deployment]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.CreateGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if game_server_deployment is not None:
            request.game_server_deployment = game_server_deployment

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.create_game_server_deployment,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_game_server_deployment(
        self,
        request: game_server_deployments.DeleteGameServerDeploymentRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Game Server Deployment.

        Args:
            request (:class:`~.game_server_deployments.DeleteGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.DeleteGameServerDeployment.
            name (:class:`str`):
                Required. The name of the Game Server Deployment to
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_deployments.GameServerDeployment``:
                A Game Server Deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
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
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_game_server_deployment,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_game_server_deployment(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRequest = None,
        *,
        game_server_deployment: game_server_deployments.GameServerDeployment = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Patches a Game Server Deployment.

        Args:
            request (:class:`~.game_server_deployments.UpdateGameServerDeploymentRequest`):
                The request object. Request message for
                GameServerDeploymentsService.UpdateGameServerDeployment.
                Only allows updates for labels.
            game_server_deployment (:class:`~.game_server_deployments.GameServerDeployment`):
                Required. The Game Server Deployment to be updated. Only
                fields specified in update_mask are updated.
                This corresponds to the ``game_server_deployment`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_deployments.GameServerDeployment``:
                A Game Server Deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([game_server_deployment, update_mask]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = game_server_deployments.UpdateGameServerDeploymentRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if game_server_deployment is not None:
            request.game_server_deployment = game_server_deployment
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.update_game_server_deployment,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_game_server_deployment_rollout(
        self,
        request: game_server_deployments.GetGameServerDeploymentRolloutRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.GameServerDeploymentRollout:
        r"""Gets details a single Game Server Deployment Rollout.

        Args:
            request (:class:`~.game_server_deployments.GetGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                GameServerDeploymentsService.GetGameServerDeploymentRollout.
            name (:class:`str`):
                Required. The name of the Game Server Deployment to
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
            ~.game_server_deployments.GameServerDeploymentRollout:
                The Game Server Deployment Rollout
                which represents the desired rollout
                state.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
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
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_game_server_deployment_rollout,
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

    def update_game_server_deployment_rollout(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRolloutRequest = None,
        *,
        rollout: game_server_deployments.GameServerDeploymentRollout = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Patches a single Game Server Deployment Rollout. The method will
        not return an error if the update does not affect any existing
        realms. For example - if the default_game_server_config is
        changed but all existing realms use the override, that is valid.
        Similarly, if a non existing realm is explicitly called out in
        game_server_config_overrides field, that will also not result in
        an error.

        Args:
            request (:class:`~.game_server_deployments.UpdateGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                GameServerDeploymentsService.UpdateGameServerRolloutDeployment.
            rollout (:class:`~.game_server_deployments.GameServerDeploymentRollout`):
                Required. The Game Server Deployment Rollout to be
                updated. Only fields specified in update_mask are
                updated.
                This corresponds to the ``rollout`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
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
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.game_server_deployments.GameServerDeployment``:
                A Game Server Deployment resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([rollout, update_mask]):
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
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.update_game_server_deployment_rollout,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            game_server_deployments.GameServerDeployment,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def preview_game_server_deployment_rollout(
        self,
        request: game_server_deployments.PreviewGameServerDeploymentRolloutRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.PreviewGameServerDeploymentRolloutResponse:
        r"""Previews the Game Server Deployment Rollout. This API
        does not mutate the Rollout resource.

        Args:
            request (:class:`~.game_server_deployments.PreviewGameServerDeploymentRolloutRequest`):
                The request object. Request message for
                PreviewGameServerDeploymentRollout.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.game_server_deployments.PreviewGameServerDeploymentRolloutResponse:
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
        rpc = gapic_v1.method.wrap_method(
            self._transport.preview_game_server_deployment_rollout,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Done; return the response.
        return response

    def fetch_deployment_state(
        self,
        request: game_server_deployments.FetchDeploymentStateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> game_server_deployments.FetchDeploymentStateResponse:
        r"""Retrieves information about the current state of the
        Game Server Ddeployment. Gathers all the Agones fleets
        and Agones autoscalers, including fleets running an
        older version of the Game Server Deployment.

        Args:
            request (:class:`~.game_server_deployments.FetchDeploymentStateRequest`):
                The request object. Request message for
                GameServerDeploymentsService.FetchDeploymentState.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.game_server_deployments.FetchDeploymentStateResponse:
                Response message for
                GameServerDeploymentsService.FetchDeploymentState.

        """
        # Create or coerce a protobuf request object.

        request = game_server_deployments.FetchDeploymentStateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.fetch_deployment_state,
            default_timeout=None,
            client_info=_client_info,
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

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


__all__ = ("GameServerDeploymentsServiceClient",)
