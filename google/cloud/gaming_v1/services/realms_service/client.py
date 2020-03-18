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
from google.cloud.gaming_v1.services.realms_service import pagers
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import realms
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from .transports.base import RealmsServiceTransport
from .transports.grpc import RealmsServiceGrpcTransport


class RealmsServiceClientMeta(type):
    """Metaclass for the RealmsService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[RealmsServiceTransport]]
    _transport_registry["grpc"] = RealmsServiceGrpcTransport

    def get_transport_class(cls, label: str = None) -> Type[RealmsServiceTransport]:
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


class RealmsServiceClient(metaclass=RealmsServiceClientMeta):
    """A Realm is a grouping of Game Server Clusters that are
    considered interchangeable.
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
    def realm_path(project: str, location: str, realm: str) -> str:
        """Return a fully-qualified realm string."""
        return "projects/{project}/locations/{location}/realms/{realm}".format(
            project=project, location=location, realm=realm
        )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, RealmsServiceTransport] = None,
        client_options: ClientOptions = DEFAULT_OPTIONS,
    ) -> None:
        """Instantiate the realms service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.RealmsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client.
        """
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, RealmsServiceTransport):
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

    def list_realms(
        self,
        request: realms.ListRealmsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRealmsPager:
        r"""Lists Realms in a given project and Location.

        Args:
            request (:class:`~.realms.ListRealmsRequest`):
                The request object. Request message for
                RealmsService.ListRealms.
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
            ~.pagers.ListRealmsPager:
                Response message for
                RealmsService.ListRealms.
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

        request = realms.ListRealmsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.list_realms, default_timeout=None, client_info=_client_info
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
        response = pagers.ListRealmsPager(
            method=rpc, request=request, response=response
        )

        # Done; return the response.
        return response

    def get_realm(
        self,
        request: realms.GetRealmRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> realms.Realm:
        r"""Gets details of a single Realm.

        Args:
            request (:class:`~.realms.GetRealmRequest`):
                The request object. Request message for
                RealmsService.GetRealm.
            name (:class:`str`):
                Required. The name of the Realm to retrieve. Uses the
                form:
                ``projects/{project}/locations/{location}/realms/{realm}``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.realms.Realm:
                A Realm resource.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = realms.GetRealmRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.get_realm, default_timeout=None, client_info=_client_info
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

    def create_realm(
        self,
        request: realms.CreateRealmRequest = None,
        *,
        parent: str = None,
        realm: realms.Realm = None,
        realm_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Creates a new Realm in a given project and Location.

        Args:
            request (:class:`~.realms.CreateRealmRequest`):
                The request object. Request message for
                RealmsService.CreateRealm.
            parent (:class:`str`):
                Required. The parent resource name. Uses the form:
                ``projects/{project}/locations/{location}``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            realm (:class:`~.realms.Realm`):
                Required. The Realm resource to be
                created.
                This corresponds to the ``realm`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            realm_id (:class:`str`):
                Required. The ID of the Realm
                resource to be created.
                This corresponds to the ``realm_id`` field
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
                :class:``~.realms.Realm``: A Realm resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([parent, realm, realm_id]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = realms.CreateRealmRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if realm is not None:
            request.realm = realm
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if realm_id is not None:
            request.realm_id = realm_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.create_realm, default_timeout=None, client_info=_client_info
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            realms.Realm,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_realm(
        self,
        request: realms.DeleteRealmRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Deletes a single Realm.

        Args:
            request (:class:`~.realms.DeleteRealmRequest`):
                The request object. Request message for
                RealmsService.DeleteRealm.
            name (:class:`str`):
                Required. The name of the Realm to delete. Uses the
                form:
                ``projects/{project}/locations/{location}/realms/{realm}``.
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
                :class:``~.realms.Realm``: A Realm resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = realms.DeleteRealmRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.delete_realm, default_timeout=None, client_info=_client_info
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            realms.Realm,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def update_realm(
        self,
        request: realms.UpdateRealmRequest = None,
        *,
        realm: realms.Realm = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Patches a single Realm.

        Args:
            request (:class:`~.realms.UpdateRealmRequest`):
                The request object. Request message for
                RealmsService.UpdateRealm.
            realm (:class:`~.realms.Realm`):
                Required. The Realm to be updated. Only fields specified
                in update_mask are updated.
                This corresponds to the ``realm`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
                Required. The update mask applies to the resource. For
                the ``FieldMask`` definition, see

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
                :class:``~.realms.Realm``: A Realm resource.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([realm, update_mask]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = realms.UpdateRealmRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if realm is not None:
            request.realm = realm
        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.update_realm, default_timeout=None, client_info=_client_info
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            realms.Realm,
            metadata_type=common.OperationMetadata,
        )

        # Done; return the response.
        return response

    def preview_realm_update(
        self,
        request: realms.PreviewRealmUpdateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> realms.PreviewRealmUpdateResponse:
        r"""Previews patches to a single Realm.

        Args:
            request (:class:`~.realms.PreviewRealmUpdateRequest`):
                The request object. Request message for
                RealmsService.PreviewRealmUpdate.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.realms.PreviewRealmUpdateResponse:
                Response message for
                RealmsService.PreviewRealmUpdate.

        """
        # Create or coerce a protobuf request object.

        request = realms.PreviewRealmUpdateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._transport.preview_realm_update,
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


__all__ = ("RealmsServiceClient",)
