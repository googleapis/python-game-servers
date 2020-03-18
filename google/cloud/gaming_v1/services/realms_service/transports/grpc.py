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

from google.cloud.gaming_v1.types import realms
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import RealmsServiceTransport


class RealmsServiceGrpcTransport(RealmsServiceTransport):
    """gRPC backend transport for RealmsService.

    A Realm is a grouping of Game Server Clusters that are
    considered interchangeable.

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
    def list_realms(
        self
    ) -> Callable[[realms.ListRealmsRequest], realms.ListRealmsResponse]:
        r"""Return a callable for the list realms method over gRPC.

        Lists Realms in a given project and Location.

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

        Gets details of a single Realm.

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
        self
    ) -> Callable[[realms.CreateRealmRequest], operations.Operation]:
        r"""Return a callable for the create realm method over gRPC.

        Creates a new Realm in a given project and Location.

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
        self
    ) -> Callable[[realms.DeleteRealmRequest], operations.Operation]:
        r"""Return a callable for the delete realm method over gRPC.

        Deletes a single Realm.

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
        self
    ) -> Callable[[realms.UpdateRealmRequest], operations.Operation]:
        r"""Return a callable for the update realm method over gRPC.

        Patches a single Realm.

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
        self
    ) -> Callable[
        [realms.PreviewRealmUpdateRequest], realms.PreviewRealmUpdateResponse
    ]:
        r"""Return a callable for the preview realm update method over gRPC.

        Previews patches to a single Realm.

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
