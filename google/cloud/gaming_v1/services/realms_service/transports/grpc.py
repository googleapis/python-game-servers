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

from google.cloud.gaming_v1.types import realms
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import RealmsServiceTransport


class RealmsServiceGrpcTransport(RealmsServiceTransport):
    """gRPC backend transport for RealmsService.

    A realm is a grouping of game server clusters that are
    considered interchangeable.

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
    def list_realms(
        self,
    ) -> Callable[[realms.ListRealmsRequest], realms.ListRealmsResponse]:
        r"""Return a callable for the list realms method over gRPC.

        Lists realms in a given project and location.

        Returns:
            Callable[[~.ListRealmsRequest],
                    ~.ListRealmsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_realms" not in self._stubs:
            self._stubs["list_realms"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/ListRealms",
                request_serializer=realms.ListRealmsRequest.serialize,
                response_deserializer=realms.ListRealmsResponse.deserialize,
            )
        return self._stubs["list_realms"]

    @property
    def get_realm(self) -> Callable[[realms.GetRealmRequest], realms.Realm]:
        r"""Return a callable for the get realm method over gRPC.

        Gets details of a single realm.

        Returns:
            Callable[[~.GetRealmRequest],
                    ~.Realm]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_realm" not in self._stubs:
            self._stubs["get_realm"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/GetRealm",
                request_serializer=realms.GetRealmRequest.serialize,
                response_deserializer=realms.Realm.deserialize,
            )
        return self._stubs["get_realm"]

    @property
    def create_realm(
        self,
    ) -> Callable[[realms.CreateRealmRequest], operations.Operation]:
        r"""Return a callable for the create realm method over gRPC.

        Creates a new realm in a given project and location.

        Returns:
            Callable[[~.CreateRealmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_realm" not in self._stubs:
            self._stubs["create_realm"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/CreateRealm",
                request_serializer=realms.CreateRealmRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_realm"]

    @property
    def delete_realm(
        self,
    ) -> Callable[[realms.DeleteRealmRequest], operations.Operation]:
        r"""Return a callable for the delete realm method over gRPC.

        Deletes a single realm.

        Returns:
            Callable[[~.DeleteRealmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_realm" not in self._stubs:
            self._stubs["delete_realm"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/DeleteRealm",
                request_serializer=realms.DeleteRealmRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_realm"]

    @property
    def update_realm(
        self,
    ) -> Callable[[realms.UpdateRealmRequest], operations.Operation]:
        r"""Return a callable for the update realm method over gRPC.

        Patches a single realm.

        Returns:
            Callable[[~.UpdateRealmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_realm" not in self._stubs:
            self._stubs["update_realm"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/UpdateRealm",
                request_serializer=realms.UpdateRealmRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["update_realm"]

    @property
    def preview_realm_update(
        self,
    ) -> Callable[
        [realms.PreviewRealmUpdateRequest], realms.PreviewRealmUpdateResponse
    ]:
        r"""Return a callable for the preview realm update method over gRPC.

        Previews patches to a single realm.

        Returns:
            Callable[[~.PreviewRealmUpdateRequest],
                    ~.PreviewRealmUpdateResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_realm_update" not in self._stubs:
            self._stubs["preview_realm_update"] = self.grpc_channel.unary_unary(
                "/google.cloud.gaming.v1beta.RealmsService/PreviewRealmUpdate",
                request_serializer=realms.PreviewRealmUpdateRequest.serialize,
                response_deserializer=realms.PreviewRealmUpdateResponse.deserialize,
            )
        return self._stubs["preview_realm_update"]


__all__ = ("RealmsServiceGrpcTransport",)
