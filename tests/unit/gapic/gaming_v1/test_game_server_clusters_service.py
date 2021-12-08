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
import os
import mock

import grpc
from grpc.experimental import aio
import json
import math
import pytest
from proto.marshal.rules.dates import DurationRule, TimestampRule


from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import future
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation
from google.api_core import operation_async  # type: ignore
from google.api_core import operations_v1
from google.api_core import path_template
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.gaming_v1.services.game_server_clusters_service import (
    GameServerClustersServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_clusters_service import (
    GameServerClustersServiceClient,
)
from google.cloud.gaming_v1.services.game_server_clusters_service import pagers
from google.cloud.gaming_v1.services.game_server_clusters_service import transports
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import game_server_clusters
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import json_format
from google.protobuf import timestamp_pb2  # type: ignore
import google.auth


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert GameServerClustersServiceClient._get_default_mtls_endpoint(None) is None
    assert (
        GameServerClustersServiceClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        GameServerClustersServiceClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        GameServerClustersServiceClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        GameServerClustersServiceClient._get_default_mtls_endpoint(
            sandbox_mtls_endpoint
        )
        == sandbox_mtls_endpoint
    )
    assert (
        GameServerClustersServiceClient._get_default_mtls_endpoint(non_googleapi)
        == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class",
    [GameServerClustersServiceClient, GameServerClustersServiceAsyncClient,],
)
def test_game_server_clusters_service_client_from_service_account_info(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "gameservices.googleapis.com:443"


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.GameServerClustersServiceGrpcTransport, "grpc"),
        (transports.GameServerClustersServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_game_server_clusters_service_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class",
    [GameServerClustersServiceClient, GameServerClustersServiceAsyncClient,],
)
def test_game_server_clusters_service_client_from_service_account_file(client_class):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == "gameservices.googleapis.com:443"


def test_game_server_clusters_service_client_get_transport_class():
    transport = GameServerClustersServiceClient.get_transport_class()
    available_transports = [
        transports.GameServerClustersServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = GameServerClustersServiceClient.get_transport_class("grpc")
    assert transport == transports.GameServerClustersServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            GameServerClustersServiceClient,
            transports.GameServerClustersServiceGrpcTransport,
            "grpc",
        ),
        (
            GameServerClustersServiceAsyncClient,
            transports.GameServerClustersServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
@mock.patch.object(
    GameServerClustersServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GameServerClustersServiceClient),
)
@mock.patch.object(
    GameServerClustersServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GameServerClustersServiceAsyncClient),
)
def test_game_server_clusters_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        GameServerClustersServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        GameServerClustersServiceClient, "get_transport_class"
    ) as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError):
            client = client_class()

    # Check the case GOOGLE_API_USE_CLIENT_CERTIFICATE has unsupported value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        with pytest.raises(ValueError):
            client = client_class()

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            GameServerClustersServiceClient,
            transports.GameServerClustersServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            GameServerClustersServiceAsyncClient,
            transports.GameServerClustersServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            GameServerClustersServiceClient,
            transports.GameServerClustersServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            GameServerClustersServiceAsyncClient,
            transports.GameServerClustersServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    GameServerClustersServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GameServerClustersServiceClient),
)
@mock.patch.object(
    GameServerClustersServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GameServerClustersServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_game_server_clusters_service_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name, client_options=options)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client.DEFAULT_ENDPOINT
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client.DEFAULT_ENDPOINT
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client.DEFAULT_ENDPOINT,
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            GameServerClustersServiceClient,
            transports.GameServerClustersServiceGrpcTransport,
            "grpc",
        ),
        (
            GameServerClustersServiceAsyncClient,
            transports.GameServerClustersServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_game_server_clusters_service_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(scopes=["1", "2"],)
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client.DEFAULT_ENDPOINT,
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            GameServerClustersServiceClient,
            transports.GameServerClustersServiceGrpcTransport,
            "grpc",
        ),
        (
            GameServerClustersServiceAsyncClient,
            transports.GameServerClustersServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_game_server_clusters_service_client_client_options_credentials_file(
    client_class, transport_class, transport_name
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client.DEFAULT_ENDPOINT,
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


def test_game_server_clusters_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.transports.GameServerClustersServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = GameServerClustersServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
        )


def test_list_game_server_clusters(
    transport: str = "grpc",
    request_type=game_server_clusters.ListGameServerClustersRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.ListGameServerClustersResponse(
            next_page_token="next_page_token_value", unreachable=["unreachable_value"],
        )
        response = client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.ListGameServerClustersRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListGameServerClustersPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_game_server_clusters_from_dict():
    test_list_game_server_clusters(request_type=dict)


def test_list_game_server_clusters_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        client.list_game_server_clusters()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.ListGameServerClustersRequest()


@pytest.mark.asyncio
async def test_list_game_server_clusters_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.ListGameServerClustersRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.ListGameServerClustersResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )
        response = await client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.ListGameServerClustersRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListGameServerClustersAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_game_server_clusters_async_from_dict():
    await test_list_game_server_clusters_async(request_type=dict)


def test_list_game_server_clusters_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.ListGameServerClustersRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        call.return_value = game_server_clusters.ListGameServerClustersResponse()
        client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_game_server_clusters_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.ListGameServerClustersRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.ListGameServerClustersResponse()
        )
        await client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_list_game_server_clusters_flattened():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.ListGameServerClustersResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_game_server_clusters(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_game_server_clusters_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_game_server_clusters(
            game_server_clusters.ListGameServerClustersRequest(), parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_game_server_clusters_flattened_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.ListGameServerClustersResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.ListGameServerClustersResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_game_server_clusters(parent="parent_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_game_server_clusters_flattened_error_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_game_server_clusters(
            game_server_clusters.ListGameServerClustersRequest(), parent="parent_value",
        )


def test_list_game_server_clusters_pager():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
                next_page_token="abc",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[], next_page_token="def",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster(),],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
            ),
            RuntimeError,
        )

        metadata = ()
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_game_server_clusters(request={})

        assert pager._metadata == metadata

        results = [i for i in pager]
        assert len(results) == 6
        assert all(
            isinstance(i, game_server_clusters.GameServerCluster) for i in results
        )


def test_list_game_server_clusters_pages():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
                next_page_token="abc",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[], next_page_token="def",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster(),],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_game_server_clusters(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_game_server_clusters_async_pager():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
                next_page_token="abc",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[], next_page_token="def",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster(),],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_game_server_clusters(request={},)
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, game_server_clusters.GameServerCluster) for i in responses
        )


@pytest.mark.asyncio
async def test_list_game_server_clusters_async_pages():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_game_server_clusters),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
                next_page_token="abc",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[], next_page_token="def",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster(),],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_game_server_clusters(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.GetGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.GameServerCluster(
            name="name_value", etag="etag_value", description="description_value",
        )
        response = client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.GetGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_clusters.GameServerCluster)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


def test_get_game_server_cluster_from_dict():
    test_get_game_server_cluster(request_type=dict)


def test_get_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        client.get_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.GetGameServerClusterRequest()


@pytest.mark.asyncio
async def test_get_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.GetGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.GameServerCluster(
                name="name_value", etag="etag_value", description="description_value",
            )
        )
        response = await client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.GetGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_clusters.GameServerCluster)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


@pytest.mark.asyncio
async def test_get_game_server_cluster_async_from_dict():
    await test_get_game_server_cluster_async(request_type=dict)


def test_get_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.GetGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        call.return_value = game_server_clusters.GameServerCluster()
        client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.GetGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.GameServerCluster()
        )
        await client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_get_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.GameServerCluster()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_game_server_cluster(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_game_server_cluster(
            game_server_clusters.GetGameServerClusterRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_get_game_server_cluster_flattened_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.GameServerCluster()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.GameServerCluster()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_game_server_cluster(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_game_server_cluster_flattened_error_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_game_server_cluster(
            game_server_clusters.GetGameServerClusterRequest(), name="name_value",
        )


def test_create_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.CreateGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.CreateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_game_server_cluster_from_dict():
    test_create_game_server_cluster(request_type=dict)


def test_create_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        client.create_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.CreateGameServerClusterRequest()


@pytest.mark.asyncio
async def test_create_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.CreateGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.CreateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_game_server_cluster_async_from_dict():
    await test_create_game_server_cluster_async(request_type=dict)


def test_create_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.CreateGameServerClusterRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.CreateGameServerClusterRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_create_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_game_server_cluster(
            parent="parent_value",
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            game_server_cluster_id="game_server_cluster_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].game_server_cluster
        mock_val = game_server_clusters.GameServerCluster(name="name_value")
        assert arg == mock_val
        arg = args[0].game_server_cluster_id
        mock_val = "game_server_cluster_id_value"
        assert arg == mock_val


def test_create_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_game_server_cluster(
            game_server_clusters.CreateGameServerClusterRequest(),
            parent="parent_value",
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            game_server_cluster_id="game_server_cluster_id_value",
        )


@pytest.mark.asyncio
async def test_create_game_server_cluster_flattened_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_game_server_cluster(
            parent="parent_value",
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            game_server_cluster_id="game_server_cluster_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].game_server_cluster
        mock_val = game_server_clusters.GameServerCluster(name="name_value")
        assert arg == mock_val
        arg = args[0].game_server_cluster_id
        mock_val = "game_server_cluster_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_game_server_cluster_flattened_error_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_game_server_cluster(
            game_server_clusters.CreateGameServerClusterRequest(),
            parent="parent_value",
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            game_server_cluster_id="game_server_cluster_id_value",
        )


def test_preview_create_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.PreviewCreateGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewCreateGameServerClusterResponse(
            etag="etag_value",
        )
        response = client.preview_create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewCreateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewCreateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_preview_create_game_server_cluster_from_dict():
    test_preview_create_game_server_cluster(request_type=dict)


def test_preview_create_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        client.preview_create_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewCreateGameServerClusterRequest()


@pytest.mark.asyncio
async def test_preview_create_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.PreviewCreateGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewCreateGameServerClusterResponse(
                etag="etag_value",
            )
        )
        response = await client.preview_create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewCreateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewCreateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


@pytest.mark.asyncio
async def test_preview_create_game_server_cluster_async_from_dict():
    await test_preview_create_game_server_cluster_async(request_type=dict)


def test_preview_create_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewCreateGameServerClusterRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        call.return_value = (
            game_server_clusters.PreviewCreateGameServerClusterResponse()
        )
        client.preview_create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_preview_create_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewCreateGameServerClusterRequest()

    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewCreateGameServerClusterResponse()
        )
        await client.preview_create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value",) in kw["metadata"]


def test_delete_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.DeleteGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.DeleteGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_game_server_cluster_from_dict():
    test_delete_game_server_cluster(request_type=dict)


def test_delete_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        client.delete_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.DeleteGameServerClusterRequest()


@pytest.mark.asyncio
async def test_delete_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.DeleteGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.DeleteGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_game_server_cluster_async_from_dict():
    await test_delete_game_server_cluster_async(request_type=dict)


def test_delete_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.DeleteGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.DeleteGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_delete_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_game_server_cluster(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_game_server_cluster(
            game_server_clusters.DeleteGameServerClusterRequest(), name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_game_server_cluster_flattened_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_game_server_cluster(name="name_value",)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_game_server_cluster_flattened_error_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_game_server_cluster(
            game_server_clusters.DeleteGameServerClusterRequest(), name="name_value",
        )


def test_preview_delete_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.PreviewDeleteGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewDeleteGameServerClusterResponse(
            etag="etag_value",
        )
        response = client.preview_delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewDeleteGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewDeleteGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_preview_delete_game_server_cluster_from_dict():
    test_preview_delete_game_server_cluster(request_type=dict)


def test_preview_delete_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        client.preview_delete_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewDeleteGameServerClusterRequest()


@pytest.mark.asyncio
async def test_preview_delete_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.PreviewDeleteGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewDeleteGameServerClusterResponse(
                etag="etag_value",
            )
        )
        response = await client.preview_delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewDeleteGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewDeleteGameServerClusterResponse
    )
    assert response.etag == "etag_value"


@pytest.mark.asyncio
async def test_preview_delete_game_server_cluster_async_from_dict():
    await test_preview_delete_game_server_cluster_async(request_type=dict)


def test_preview_delete_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewDeleteGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        call.return_value = (
            game_server_clusters.PreviewDeleteGameServerClusterResponse()
        )
        client.preview_delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_preview_delete_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewDeleteGameServerClusterRequest()

    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewDeleteGameServerClusterResponse()
        )
        await client.preview_delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value",) in kw["metadata"]


def test_update_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.UpdateGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.UpdateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_game_server_cluster_from_dict():
    test_update_game_server_cluster(request_type=dict)


def test_update_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        client.update_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.UpdateGameServerClusterRequest()


@pytest.mark.asyncio
async def test_update_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.UpdateGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.UpdateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_game_server_cluster_async_from_dict():
    await test_update_game_server_cluster_async(request_type=dict)


def test_update_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.UpdateGameServerClusterRequest()

    request.game_server_cluster.name = "game_server_cluster.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_cluster.name=game_server_cluster.name/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.UpdateGameServerClusterRequest()

    request.game_server_cluster.name = "game_server_cluster.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_cluster.name=game_server_cluster.name/value",
    ) in kw["metadata"]


def test_update_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_game_server_cluster(
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].game_server_cluster
        mock_val = game_server_clusters.GameServerCluster(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_game_server_cluster(
            game_server_clusters.UpdateGameServerClusterRequest(),
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_game_server_cluster_flattened_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_game_server_cluster(
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].game_server_cluster
        mock_val = game_server_clusters.GameServerCluster(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_game_server_cluster_flattened_error_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_game_server_cluster(
            game_server_clusters.UpdateGameServerClusterRequest(),
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_preview_update_game_server_cluster(
    transport: str = "grpc",
    request_type=game_server_clusters.PreviewUpdateGameServerClusterRequest,
):
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewUpdateGameServerClusterResponse(
            etag="etag_value",
        )
        response = client.preview_update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewUpdateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewUpdateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_preview_update_game_server_cluster_from_dict():
    test_preview_update_game_server_cluster(request_type=dict)


def test_preview_update_game_server_cluster_empty_call():
    # This test is a coverage failsafe to make sure that totally empty calls,
    # i.e. request == None and no flattened fields passed, work.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        client.preview_update_game_server_cluster()
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewUpdateGameServerClusterRequest()


@pytest.mark.asyncio
async def test_preview_update_game_server_cluster_async(
    transport: str = "grpc_asyncio",
    request_type=game_server_clusters.PreviewUpdateGameServerClusterRequest,
):
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewUpdateGameServerClusterResponse(
                etag="etag_value",
            )
        )
        response = await client.preview_update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == game_server_clusters.PreviewUpdateGameServerClusterRequest()

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewUpdateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


@pytest.mark.asyncio
async def test_preview_update_game_server_cluster_async_from_dict():
    await test_preview_update_game_server_cluster_async(request_type=dict)


def test_preview_update_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewUpdateGameServerClusterRequest()

    request.game_server_cluster.name = "game_server_cluster.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        call.return_value = (
            game_server_clusters.PreviewUpdateGameServerClusterResponse()
        )
        client.preview_update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_cluster.name=game_server_cluster.name/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_preview_update_game_server_cluster_field_headers_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.PreviewUpdateGameServerClusterRequest()

    request.game_server_cluster.name = "game_server_cluster.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_clusters.PreviewUpdateGameServerClusterResponse()
        )
        await client.preview_update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_cluster.name=game_server_cluster.name/value",
    ) in kw["metadata"]


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GameServerClustersServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GameServerClustersServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GameServerClustersServiceClient(
            client_options={"scopes": ["1", "2"]}, transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = GameServerClustersServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.GameServerClustersServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GameServerClustersServiceGrpcTransport,
        transports.GameServerClustersServiceGrpcAsyncIOTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport, transports.GameServerClustersServiceGrpcTransport,
    )


def test_game_server_clusters_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.GameServerClustersServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_game_server_clusters_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.transports.GameServerClustersServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.GameServerClustersServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_game_server_clusters",
        "get_game_server_cluster",
        "create_game_server_cluster",
        "preview_create_game_server_cluster",
        "delete_game_server_cluster",
        "preview_delete_game_server_cluster",
        "update_game_server_cluster",
        "preview_update_game_server_cluster",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_game_server_clusters_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.transports.GameServerClustersServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GameServerClustersServiceTransport(
            credentials_file="credentials.json", quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_game_server_clusters_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.transports.GameServerClustersServiceTransport._prep_wrapped_messages"
    ) as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GameServerClustersServiceTransport()
        adc.assert_called_once()


def test_game_server_clusters_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        GameServerClustersServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GameServerClustersServiceGrpcTransport,
        transports.GameServerClustersServiceGrpcAsyncIOTransport,
    ],
)
def test_game_server_clusters_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.GameServerClustersServiceGrpcTransport, grpc_helpers),
        (transports.GameServerClustersServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_game_server_clusters_service_transport_create_channel(
    transport_class, grpc_helpers
):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "gameservices.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="gameservices.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GameServerClustersServiceGrpcTransport,
        transports.GameServerClustersServiceGrpcAsyncIOTransport,
    ],
)
def test_game_server_clusters_service_grpc_transport_client_cert_source_for_mtls(
    transport_class,
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_game_server_clusters_service_host_no_port():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com"
        ),
    )
    assert client.transport._host == "gameservices.googleapis.com:443"


def test_game_server_clusters_service_host_with_port():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com:8000"
        ),
    )
    assert client.transport._host == "gameservices.googleapis.com:8000"


def test_game_server_clusters_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GameServerClustersServiceGrpcTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_game_server_clusters_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GameServerClustersServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk", channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GameServerClustersServiceGrpcTransport,
        transports.GameServerClustersServiceGrpcAsyncIOTransport,
    ],
)
def test_game_server_clusters_service_transport_channel_mtls_with_client_cert_source(
    transport_class,
):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GameServerClustersServiceGrpcTransport,
        transports.GameServerClustersServiceGrpcAsyncIOTransport,
    ],
)
def test_game_server_clusters_service_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_game_server_clusters_service_grpc_lro_client():
    client = GameServerClustersServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_game_server_clusters_service_grpc_lro_async_client():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsAsyncClient,)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_game_server_cluster_path():
    project = "squid"
    location = "clam"
    realm = "whelk"
    cluster = "octopus"
    expected = "projects/{project}/locations/{location}/realms/{realm}/gameServerClusters/{cluster}".format(
        project=project, location=location, realm=realm, cluster=cluster,
    )
    actual = GameServerClustersServiceClient.game_server_cluster_path(
        project, location, realm, cluster
    )
    assert expected == actual


def test_parse_game_server_cluster_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "realm": "cuttlefish",
        "cluster": "mussel",
    }
    path = GameServerClustersServiceClient.game_server_cluster_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_game_server_cluster_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "winkle"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = GameServerClustersServiceClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "nautilus",
    }
    path = GameServerClustersServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "scallop"
    expected = "folders/{folder}".format(folder=folder,)
    actual = GameServerClustersServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "abalone",
    }
    path = GameServerClustersServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "squid"
    expected = "organizations/{organization}".format(organization=organization,)
    actual = GameServerClustersServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "clam",
    }
    path = GameServerClustersServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "whelk"
    expected = "projects/{project}".format(project=project,)
    actual = GameServerClustersServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "octopus",
    }
    path = GameServerClustersServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "oyster"
    location = "nudibranch"
    expected = "projects/{project}/locations/{location}".format(
        project=project, location=location,
    )
    actual = GameServerClustersServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
    }
    path = GameServerClustersServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerClustersServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_withDEFAULT_CLIENT_INFO():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.GameServerClustersServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = GameServerClustersServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.GameServerClustersServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = GameServerClustersServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


@pytest.mark.asyncio
async def test_transport_close_async():
    client = GameServerClustersServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
    )
    with mock.patch.object(
        type(getattr(client.transport, "grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close():
    transports = {
        "grpc": "_grpc_channel",
    }

    for transport, close_name in transports.items():
        client = GameServerClustersServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        with mock.patch.object(
            type(getattr(client.transport, close_name)), "close"
        ) as close:
            with client:
                close.assert_not_called()
            close.assert_called_once()


def test_client_ctx():
    transports = [
        "grpc",
    ]
    for transport in transports:
        client = GameServerClustersServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()
