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
import math
import pytest

from google import auth
from google.api_core import client_options
from google.api_core import future
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import operation_async
from google.api_core import operations_v1
from google.auth import credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.gaming_v1.services.game_server_deployments_service import (
    GameServerDeploymentsServiceAsyncClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service import (
    GameServerDeploymentsServiceClient,
)
from google.cloud.gaming_v1.services.game_server_deployments_service import pagers
from google.cloud.gaming_v1.services.game_server_deployments_service import transports
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import game_server_deployments
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


def test__get_default_mtls_endpoint():
    api_endpoint = "example.googleapis.com"
    api_mtls_endpoint = "example.mtls.googleapis.com"
    sandbox_endpoint = "example.sandbox.googleapis.com"
    sandbox_mtls_endpoint = "example.mtls.sandbox.googleapis.com"
    non_googleapi = "api.example.com"

    assert GameServerDeploymentsServiceClient._get_default_mtls_endpoint(None) is None
    assert (
        GameServerDeploymentsServiceClient._get_default_mtls_endpoint(api_endpoint)
        == api_mtls_endpoint
    )
    assert (
        GameServerDeploymentsServiceClient._get_default_mtls_endpoint(api_mtls_endpoint)
        == api_mtls_endpoint
    )
    assert (
        GameServerDeploymentsServiceClient._get_default_mtls_endpoint(sandbox_endpoint)
        == sandbox_mtls_endpoint
    )
    assert (
        GameServerDeploymentsServiceClient._get_default_mtls_endpoint(
            sandbox_mtls_endpoint
        )
        == sandbox_mtls_endpoint
    )
    assert (
        GameServerDeploymentsServiceClient._get_default_mtls_endpoint(non_googleapi)
        == non_googleapi
    )


@pytest.mark.parametrize(
    "client_class",
    [GameServerDeploymentsServiceClient, GameServerDeploymentsServiceAsyncClient],
)
def test_game_server_deployments_service_client_from_service_account_file(client_class):
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = client_class.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == "gameservices.googleapis.com:443"


def test_game_server_deployments_service_client_get_transport_class():
    transport = GameServerDeploymentsServiceClient.get_transport_class()
    assert transport == transports.GameServerDeploymentsServiceGrpcTransport

    transport = GameServerDeploymentsServiceClient.get_transport_class("grpc")
    assert transport == transports.GameServerDeploymentsServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            GameServerDeploymentsServiceClient,
            transports.GameServerDeploymentsServiceGrpcTransport,
            "grpc",
        ),
        (
            GameServerDeploymentsServiceAsyncClient,
            transports.GameServerDeploymentsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_game_server_deployments_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        GameServerDeploymentsServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        GameServerDeploymentsServiceClient, "get_transport_class"
    ) as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            api_mtls_endpoint="squid.clam.whelk",
            client_cert_source=None,
            credentials=None,
            host="squid.clam.whelk",
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS is
    # "never".
    os.environ["GOOGLE_API_USE_MTLS"] = "never"
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class()
        patched.assert_called_once_with(
            api_mtls_endpoint=client.DEFAULT_ENDPOINT,
            client_cert_source=None,
            credentials=None,
            host=client.DEFAULT_ENDPOINT,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS is
    # "always".
    os.environ["GOOGLE_API_USE_MTLS"] = "always"
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class()
        patched.assert_called_once_with(
            api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
            client_cert_source=None,
            credentials=None,
            host=client.DEFAULT_MTLS_ENDPOINT,
        )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", and client_cert_source is provided.
    os.environ["GOOGLE_API_USE_MTLS"] = "auto"
    options = client_options.ClientOptions(
        client_cert_source=client_cert_source_callback
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options)
        patched.assert_called_once_with(
            api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
            client_cert_source=client_cert_source_callback,
            credentials=None,
            host=client.DEFAULT_MTLS_ENDPOINT,
        )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", and default_client_cert_source is provided.
    os.environ["GOOGLE_API_USE_MTLS"] = "auto"
    with mock.patch.object(transport_class, "__init__") as patched:
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                api_mtls_endpoint=client.DEFAULT_MTLS_ENDPOINT,
                client_cert_source=None,
                credentials=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
            )

    # Check the case api_endpoint is not provided, GOOGLE_API_USE_MTLS is
    # "auto", but client_cert_source and default_client_cert_source are None.
    os.environ["GOOGLE_API_USE_MTLS"] = "auto"
    with mock.patch.object(transport_class, "__init__") as patched:
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            patched.return_value = None
            client = client_class()
            patched.assert_called_once_with(
                api_mtls_endpoint=client.DEFAULT_ENDPOINT,
                client_cert_source=None,
                credentials=None,
                host=client.DEFAULT_ENDPOINT,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS has
    # unsupported value.
    os.environ["GOOGLE_API_USE_MTLS"] = "Unsupported"
    with pytest.raises(MutualTLSChannelError):
        client = client_class()

    del os.environ["GOOGLE_API_USE_MTLS"]


def test_game_server_deployments_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.gaming_v1.services.game_server_deployments_service.transports.GameServerDeploymentsServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = GameServerDeploymentsServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        grpc_transport.assert_called_once_with(
            api_mtls_endpoint="squid.clam.whelk",
            client_cert_source=None,
            credentials=None,
            host="squid.clam.whelk",
        )


def test_list_game_server_deployments(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.ListGameServerDeploymentsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.ListGameServerDeploymentsResponse(
            next_page_token="next_page_token_value", unreachable=["unreachable_value"]
        )

        response = client.list_game_server_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListGameServerDeploymentsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


@pytest.mark.asyncio
async def test_list_game_server_deployments_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.ListGameServerDeploymentsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.ListGameServerDeploymentsResponse(
                next_page_token="next_page_token_value",
                unreachable=["unreachable_value"],
            )
        )

        response = await client.list_game_server_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListGameServerDeploymentsAsyncPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_game_server_deployments_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.ListGameServerDeploymentsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_deployments), "__call__"
    ) as call:
        call.return_value = game_server_deployments.ListGameServerDeploymentsResponse()

        client.list_game_server_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_list_game_server_deployments_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.ListGameServerDeploymentsRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_game_server_deployments), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.ListGameServerDeploymentsResponse()
        )

        await client.list_game_server_deployments(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


def test_list_game_server_deployments_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.ListGameServerDeploymentsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_game_server_deployments(parent="parent_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"


def test_list_game_server_deployments_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_game_server_deployments(
            game_server_deployments.ListGameServerDeploymentsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_game_server_deployments_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.ListGameServerDeploymentsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.ListGameServerDeploymentsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_game_server_deployments(parent="parent_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"


@pytest.mark.asyncio
async def test_list_game_server_deployments_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_game_server_deployments(
            game_server_deployments.ListGameServerDeploymentsRequest(),
            parent="parent_value",
        )


def test_list_game_server_deployments_pager():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ],
                next_page_token="abc",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[], next_page_token="def"
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment()
                ],
                next_page_token="ghi",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ]
            ),
            RuntimeError,
        )
        results = [i for i in client.list_game_server_deployments(request={})]
        assert len(results) == 6
        assert all(
            isinstance(i, game_server_deployments.GameServerDeployment) for i in results
        )


def test_list_game_server_deployments_pages():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_deployments), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ],
                next_page_token="abc",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[], next_page_token="def"
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment()
                ],
                next_page_token="ghi",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ]
            ),
            RuntimeError,
        )
        pages = list(client.list_game_server_deployments(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_game_server_deployments_async_pager():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_game_server_deployments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ],
                next_page_token="abc",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[], next_page_token="def"
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment()
                ],
                next_page_token="ghi",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ]
            ),
            RuntimeError,
        )
        async_pager = await client.list_game_server_deployments(request={})
        assert async_pager.next_page_token == "abc"
        responses = []
        async for response in async_pager:
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, game_server_deployments.GameServerDeployment)
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_game_server_deployments_async_pages():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.list_game_server_deployments),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ],
                next_page_token="abc",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[], next_page_token="def"
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment()
                ],
                next_page_token="ghi",
            ),
            game_server_deployments.ListGameServerDeploymentsResponse(
                game_server_deployments=[
                    game_server_deployments.GameServerDeployment(),
                    game_server_deployments.GameServerDeployment(),
                ]
            ),
            RuntimeError,
        )
        pages = []
        async for page in (await client.list_game_server_deployments(request={})).pages:
            pages.append(page)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_get_game_server_deployment(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.GetGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeployment(
            name="name_value", etag="etag_value", description="description_value"
        )

        response = client.get_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.GameServerDeployment)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


@pytest.mark.asyncio
async def test_get_game_server_deployment_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.GetGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeployment(
                name="name_value", etag="etag_value", description="description_value"
            )
        )

        response = await client.get_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.GameServerDeployment)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


def test_get_game_server_deployment_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.GetGameServerDeploymentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment), "__call__"
    ) as call:
        call.return_value = game_server_deployments.GameServerDeployment()

        client.get_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_get_game_server_deployment_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.GetGameServerDeploymentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeployment()
        )

        await client.get_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_get_game_server_deployment_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeployment()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_game_server_deployment(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_get_game_server_deployment_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_game_server_deployment(
            game_server_deployments.GetGameServerDeploymentRequest(), name="name_value"
        )


@pytest.mark.asyncio
async def test_get_game_server_deployment_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeployment()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeployment()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_game_server_deployment(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_game_server_deployment_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_game_server_deployment(
            game_server_deployments.GetGameServerDeploymentRequest(), name="name_value"
        )


def test_create_game_server_deployment(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.CreateGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.create_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.create_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_create_game_server_deployment_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.CreateGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.create_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_game_server_deployment_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.CreateGameServerDeploymentRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.create_game_server_deployment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.create_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_create_game_server_deployment_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.CreateGameServerDeploymentRequest()
    request.parent = "parent/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_game_server_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.create_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


def test_create_game_server_deployment_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.create_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_game_server_deployment(
            parent="parent_value",
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"
        assert args[
            0
        ].game_server_deployment == game_server_deployments.GameServerDeployment(
            name="name_value"
        )


def test_create_game_server_deployment_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_game_server_deployment(
            game_server_deployments.CreateGameServerDeploymentRequest(),
            parent="parent_value",
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
        )


@pytest.mark.asyncio
async def test_create_game_server_deployment_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.create_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_game_server_deployment(
            parent="parent_value",
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"
        assert args[
            0
        ].game_server_deployment == game_server_deployments.GameServerDeployment(
            name="name_value"
        )


@pytest.mark.asyncio
async def test_create_game_server_deployment_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_game_server_deployment(
            game_server_deployments.CreateGameServerDeploymentRequest(),
            parent="parent_value",
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
        )


def test_delete_game_server_deployment(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.DeleteGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.delete_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_delete_game_server_deployment_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.DeleteGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.delete_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_game_server_deployment_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.DeleteGameServerDeploymentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.delete_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_game_server_deployment_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.DeleteGameServerDeploymentRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.delete_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_delete_game_server_deployment_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_game_server_deployment(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_delete_game_server_deployment_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_game_server_deployment(
            game_server_deployments.DeleteGameServerDeploymentRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_game_server_deployment_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.delete_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_game_server_deployment(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_delete_game_server_deployment_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_game_server_deployment(
            game_server_deployments.DeleteGameServerDeploymentRequest(),
            name="name_value",
        )


def test_update_game_server_deployment(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.UpdateGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.update_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_game_server_deployment_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.UpdateGameServerDeploymentRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.update_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_game_server_deployment_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.UpdateGameServerDeploymentRequest()
    request.game_server_deployment.name = "game_server_deployment.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.update_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_deployment.name=game_server_deployment.name/value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_game_server_deployment_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.UpdateGameServerDeploymentRequest()
    request.game_server_deployment.name = "game_server_deployment.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.update_game_server_deployment(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "game_server_deployment.name=game_server_deployment.name/value",
    ) in kw["metadata"]


def test_update_game_server_deployment_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_game_server_deployment(
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[
            0
        ].game_server_deployment == game_server_deployments.GameServerDeployment(
            name="name_value"
        )
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_game_server_deployment_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_game_server_deployment(
            game_server_deployments.UpdateGameServerDeploymentRequest(),
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_game_server_deployment_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_game_server_deployment(
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[
            0
        ].game_server_deployment == game_server_deployments.GameServerDeployment(
            name="name_value"
        )
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


@pytest.mark.asyncio
async def test_update_game_server_deployment_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_game_server_deployment(
            game_server_deployments.UpdateGameServerDeploymentRequest(),
            game_server_deployment=game_server_deployments.GameServerDeployment(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_get_game_server_deployment_rollout(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.GetGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeploymentRollout(
            name="name_value",
            default_game_server_config="default_game_server_config_value",
            etag="etag_value",
        )

        response = client.get_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.GameServerDeploymentRollout)
    assert response.name == "name_value"
    assert response.default_game_server_config == "default_game_server_config_value"
    assert response.etag == "etag_value"


@pytest.mark.asyncio
async def test_get_game_server_deployment_rollout_async(
    transport: str = "grpc_asyncio"
):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.GetGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeploymentRollout(
                name="name_value",
                default_game_server_config="default_game_server_config_value",
                etag="etag_value",
            )
        )

        response = await client.get_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.GameServerDeploymentRollout)
    assert response.name == "name_value"
    assert response.default_game_server_config == "default_game_server_config_value"
    assert response.etag == "etag_value"


def test_get_game_server_deployment_rollout_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.GetGameServerDeploymentRolloutRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        call.return_value = game_server_deployments.GameServerDeploymentRollout()

        client.get_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_get_game_server_deployment_rollout_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.GetGameServerDeploymentRolloutRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeploymentRollout()
        )

        await client.get_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_get_game_server_deployment_rollout_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeploymentRollout()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_game_server_deployment_rollout(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_get_game_server_deployment_rollout_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_game_server_deployment_rollout(
            game_server_deployments.GetGameServerDeploymentRolloutRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_game_server_deployment_rollout_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.get_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.GameServerDeploymentRollout()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.GameServerDeploymentRollout()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_game_server_deployment_rollout(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


@pytest.mark.asyncio
async def test_get_game_server_deployment_rollout_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_game_server_deployment_rollout(
            game_server_deployments.GetGameServerDeploymentRolloutRequest(),
            name="name_value",
        )


def test_update_game_server_deployment_rollout(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.UpdateGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.update_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


@pytest.mark.asyncio
async def test_update_game_server_deployment_rollout_async(
    transport: str = "grpc_asyncio"
):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.UpdateGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment_rollout),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )

        response = await client.update_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_game_server_deployment_rollout_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.UpdateGameServerDeploymentRolloutRequest()
    request.rollout.name = "rollout.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment_rollout), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")

        client.update_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "rollout.name=rollout.name/value") in kw[
        "metadata"
    ]


@pytest.mark.asyncio
async def test_update_game_server_deployment_rollout_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.UpdateGameServerDeploymentRolloutRequest()
    request.rollout.name = "rollout.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment_rollout),
        "__call__",
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )

        await client.update_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "rollout.name=rollout.name/value") in kw[
        "metadata"
    ]


def test_update_game_server_deployment_rollout_flattened():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_game_server_deployment_rollout(
            rollout=game_server_deployments.GameServerDeploymentRollout(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].rollout == game_server_deployments.GameServerDeploymentRollout(
            name="name_value"
        )
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_game_server_deployment_rollout_flattened_error():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_game_server_deployment_rollout(
            game_server_deployments.UpdateGameServerDeploymentRolloutRequest(),
            rollout=game_server_deployments.GameServerDeploymentRollout(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_game_server_deployment_rollout_flattened_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.update_game_server_deployment_rollout),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_game_server_deployment_rollout(
            rollout=game_server_deployments.GameServerDeploymentRollout(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0].rollout == game_server_deployments.GameServerDeploymentRollout(
            name="name_value"
        )
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


@pytest.mark.asyncio
async def test_update_game_server_deployment_rollout_flattened_error_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_game_server_deployment_rollout(
            game_server_deployments.UpdateGameServerDeploymentRolloutRequest(),
            rollout=game_server_deployments.GameServerDeploymentRollout(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_preview_game_server_deployment_rollout(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.PreviewGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_game_server_deployment_rollout), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.PreviewGameServerDeploymentRolloutResponse(
            unavailable=["unavailable_value"], etag="etag_value"
        )

        response = client.preview_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_deployments.PreviewGameServerDeploymentRolloutResponse
    )
    assert response.unavailable == ["unavailable_value"]
    assert response.etag == "etag_value"


@pytest.mark.asyncio
async def test_preview_game_server_deployment_rollout_async(
    transport: str = "grpc_asyncio"
):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.PreviewGameServerDeploymentRolloutRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.preview_game_server_deployment_rollout),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.PreviewGameServerDeploymentRolloutResponse(
                unavailable=["unavailable_value"], etag="etag_value"
            )
        )

        response = await client.preview_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_deployments.PreviewGameServerDeploymentRolloutResponse
    )
    assert response.unavailable == ["unavailable_value"]
    assert response.etag == "etag_value"


def test_preview_game_server_deployment_rollout_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.PreviewGameServerDeploymentRolloutRequest()
    request.rollout.name = "rollout.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_game_server_deployment_rollout), "__call__"
    ) as call:
        call.return_value = (
            game_server_deployments.PreviewGameServerDeploymentRolloutResponse()
        )

        client.preview_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "rollout.name=rollout.name/value") in kw[
        "metadata"
    ]


@pytest.mark.asyncio
async def test_preview_game_server_deployment_rollout_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.PreviewGameServerDeploymentRolloutRequest()
    request.rollout.name = "rollout.name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.preview_game_server_deployment_rollout),
        "__call__",
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.PreviewGameServerDeploymentRolloutResponse()
        )

        await client.preview_game_server_deployment_rollout(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "rollout.name=rollout.name/value") in kw[
        "metadata"
    ]


def test_fetch_deployment_state(transport: str = "grpc"):
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.FetchDeploymentStateRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.fetch_deployment_state), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_deployments.FetchDeploymentStateResponse(
            unavailable=["unavailable_value"]
        )

        response = client.fetch_deployment_state(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.FetchDeploymentStateResponse)
    assert response.unavailable == ["unavailable_value"]


@pytest.mark.asyncio
async def test_fetch_deployment_state_async(transport: str = "grpc_asyncio"):
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_deployments.FetchDeploymentStateRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.fetch_deployment_state), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.FetchDeploymentStateResponse(
                unavailable=["unavailable_value"]
            )
        )

        response = await client.fetch_deployment_state(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_deployments.FetchDeploymentStateResponse)
    assert response.unavailable == ["unavailable_value"]


def test_fetch_deployment_state_field_headers():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.FetchDeploymentStateRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.fetch_deployment_state), "__call__"
    ) as call:
        call.return_value = game_server_deployments.FetchDeploymentStateResponse()

        client.fetch_deployment_state(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


@pytest.mark.asyncio
async def test_fetch_deployment_state_field_headers_async():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_deployments.FetchDeploymentStateRequest()
    request.name = "name/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._client._transport.fetch_deployment_state), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            game_server_deployments.FetchDeploymentStateResponse()
        )

        await client.fetch_deployment_state(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.GameServerDeploymentsServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    with pytest.raises(ValueError):
        client = GameServerDeploymentsServiceClient(
            credentials=credentials.AnonymousCredentials(), transport=transport
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GameServerDeploymentsServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    client = GameServerDeploymentsServiceClient(transport=transport)
    assert client._transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GameServerDeploymentsServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.GameServerDeploymentsServiceGrpcAsyncIOTransport(
        credentials=credentials.AnonymousCredentials()
    )
    channel = transport.grpc_channel
    assert channel


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials()
    )
    assert isinstance(
        client._transport, transports.GameServerDeploymentsServiceGrpcTransport
    )


def test_game_server_deployments_service_base_transport():
    # Instantiate the base transport.
    transport = transports.GameServerDeploymentsServiceTransport(
        credentials=credentials.AnonymousCredentials()
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_game_server_deployments",
        "get_game_server_deployment",
        "create_game_server_deployment",
        "delete_game_server_deployment",
        "update_game_server_deployment",
        "get_game_server_deployment_rollout",
        "update_game_server_deployment_rollout",
        "preview_game_server_deployment_rollout",
        "fetch_deployment_state",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_game_server_deployments_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        GameServerDeploymentsServiceClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",)
        )


def test_game_server_deployments_service_transport_auth_adc():
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        transports.GameServerDeploymentsServiceGrpcTransport(host="squid.clam.whelk")
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",)
        )


def test_game_server_deployments_service_host_no_port():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com"
        ),
    )
    assert client._transport._host == "gameservices.googleapis.com:443"


def test_game_server_deployments_service_host_with_port():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com:8000"
        ),
    )
    assert client._transport._host == "gameservices.googleapis.com:8000"


def test_game_server_deployments_service_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")

    # Check that if channel is provided, mtls endpoint and client_cert_source
    # won't be used.
    callback = mock.MagicMock()
    transport = transports.GameServerDeploymentsServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=callback,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert not callback.called


def test_game_server_deployments_service_grpc_asyncio_transport_channel():
    channel = aio.insecure_channel("http://localhost/")

    # Check that if channel is provided, mtls endpoint and client_cert_source
    # won't be used.
    callback = mock.MagicMock()
    transport = transports.GameServerDeploymentsServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=callback,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert not callback.called


@mock.patch("grpc.ssl_channel_credentials", autospec=True)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_game_server_deployments_service_grpc_transport_channel_mtls_with_client_cert_source(
    grpc_create_channel, grpc_ssl_channel_cred
):
    # Check that if channel is None, but api_mtls_endpoint and client_cert_source
    # are provided, then a mTLS channel will be created.
    mock_cred = mock.Mock()

    mock_ssl_cred = mock.Mock()
    grpc_ssl_channel_cred.return_value = mock_ssl_cred

    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    transport = transports.GameServerDeploymentsServiceGrpcTransport(
        host="squid.clam.whelk",
        credentials=mock_cred,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=client_cert_source_callback,
    )
    grpc_ssl_channel_cred.assert_called_once_with(
        certificate_chain=b"cert bytes", private_key=b"key bytes"
    )
    grpc_create_channel.assert_called_once_with(
        "mtls.squid.clam.whelk:443",
        credentials=mock_cred,
        ssl_credentials=mock_ssl_cred,
        scopes=("https://www.googleapis.com/auth/cloud-platform",),
    )
    assert transport.grpc_channel == mock_grpc_channel


@mock.patch("grpc.ssl_channel_credentials", autospec=True)
@mock.patch("google.api_core.grpc_helpers_async.create_channel", autospec=True)
def test_game_server_deployments_service_grpc_asyncio_transport_channel_mtls_with_client_cert_source(
    grpc_create_channel, grpc_ssl_channel_cred
):
    # Check that if channel is None, but api_mtls_endpoint and client_cert_source
    # are provided, then a mTLS channel will be created.
    mock_cred = mock.Mock()

    mock_ssl_cred = mock.Mock()
    grpc_ssl_channel_cred.return_value = mock_ssl_cred

    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    transport = transports.GameServerDeploymentsServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        credentials=mock_cred,
        api_mtls_endpoint="mtls.squid.clam.whelk",
        client_cert_source=client_cert_source_callback,
    )
    grpc_ssl_channel_cred.assert_called_once_with(
        certificate_chain=b"cert bytes", private_key=b"key bytes"
    )
    grpc_create_channel.assert_called_once_with(
        "mtls.squid.clam.whelk:443",
        credentials=mock_cred,
        ssl_credentials=mock_ssl_cred,
        scopes=("https://www.googleapis.com/auth/cloud-platform",),
    )
    assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "api_mtls_endpoint", ["mtls.squid.clam.whelk", "mtls.squid.clam.whelk:443"]
)
@mock.patch("google.api_core.grpc_helpers.create_channel", autospec=True)
def test_game_server_deployments_service_grpc_transport_channel_mtls_with_adc(
    grpc_create_channel, api_mtls_endpoint
):
    # Check that if channel and client_cert_source are None, but api_mtls_endpoint
    # is provided, then a mTLS channel will be created with SSL ADC.
    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    # Mock google.auth.transport.grpc.SslCredentials class.
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        mock_cred = mock.Mock()
        transport = transports.GameServerDeploymentsServiceGrpcTransport(
            host="squid.clam.whelk",
            credentials=mock_cred,
            api_mtls_endpoint=api_mtls_endpoint,
            client_cert_source=None,
        )
        grpc_create_channel.assert_called_once_with(
            "mtls.squid.clam.whelk:443",
            credentials=mock_cred,
            ssl_credentials=mock_ssl_cred,
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
        )
        assert transport.grpc_channel == mock_grpc_channel


@pytest.mark.parametrize(
    "api_mtls_endpoint", ["mtls.squid.clam.whelk", "mtls.squid.clam.whelk:443"]
)
@mock.patch("google.api_core.grpc_helpers_async.create_channel", autospec=True)
def test_game_server_deployments_service_grpc_asyncio_transport_channel_mtls_with_adc(
    grpc_create_channel, api_mtls_endpoint
):
    # Check that if channel and client_cert_source are None, but api_mtls_endpoint
    # is provided, then a mTLS channel will be created with SSL ADC.
    mock_grpc_channel = mock.Mock()
    grpc_create_channel.return_value = mock_grpc_channel

    # Mock google.auth.transport.grpc.SslCredentials class.
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        mock_cred = mock.Mock()
        transport = transports.GameServerDeploymentsServiceGrpcAsyncIOTransport(
            host="squid.clam.whelk",
            credentials=mock_cred,
            api_mtls_endpoint=api_mtls_endpoint,
            client_cert_source=None,
        )
        grpc_create_channel.assert_called_once_with(
            "mtls.squid.clam.whelk:443",
            credentials=mock_cred,
            ssl_credentials=mock_ssl_cred,
            scopes=("https://www.googleapis.com/auth/cloud-platform",),
        )
        assert transport.grpc_channel == mock_grpc_channel


def test_game_server_deployments_service_grpc_lro_client():
    client = GameServerDeploymentsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc"
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_game_server_deployments_service_grpc_lro_async_client():
    client = GameServerDeploymentsServiceAsyncClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc_asyncio"
    )
    transport = client._client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsAsyncClient)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_game_server_deployment_path():
    project = "squid"
    location = "clam"
    deployment = "whelk"

    expected = "projects/{project}/locations/{location}/gameServerDeployments/{deployment}".format(
        project=project, location=location, deployment=deployment
    )
    actual = GameServerDeploymentsServiceClient.game_server_deployment_path(
        project, location, deployment
    )
    assert expected == actual


def test_parse_game_server_deployment_path():
    expected = {"project": "octopus", "location": "oyster", "deployment": "nudibranch"}
    path = GameServerDeploymentsServiceClient.game_server_deployment_path(**expected)

    # Check that the path construction is reversible.
    actual = GameServerDeploymentsServiceClient.parse_game_server_deployment_path(path)
    assert expected == actual


def test_game_server_deployment_rollout_path():
    project = "squid"
    location = "clam"
    deployment = "whelk"

    expected = "projects/{project}/locations/{location}/gameServerDeployments/{deployment}/rollout".format(
        project=project, location=location, deployment=deployment
    )
    actual = GameServerDeploymentsServiceClient.game_server_deployment_rollout_path(
        project, location, deployment
    )
    assert expected == actual


def test_parse_game_server_deployment_rollout_path():
    expected = {"project": "octopus", "location": "oyster", "deployment": "nudibranch"}
    path = GameServerDeploymentsServiceClient.game_server_deployment_rollout_path(
        **expected
    )

    # Check that the path construction is reversible.
    actual = GameServerDeploymentsServiceClient.parse_game_server_deployment_rollout_path(
        path
    )
    assert expected == actual
