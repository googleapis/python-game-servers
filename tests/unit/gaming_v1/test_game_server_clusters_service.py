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

from unittest import mock

import grpc
import math
import pytest

from google import auth
from google.api_core import client_options
from google.api_core import future
from google.api_core import operations_v1
from google.auth import credentials
from google.cloud.gaming_v1.services.game_server_clusters_service import (
    GameServerClustersServiceClient,
)
from google.cloud.gaming_v1.services.game_server_clusters_service import pagers
from google.cloud.gaming_v1.services.game_server_clusters_service import transports
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import game_server_clusters
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


def test_game_server_clusters_service_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = GameServerClustersServiceClient.from_service_account_file(
            "dummy/file/path.json"
        )
        assert client._transport._credentials == creds

        client = GameServerClustersServiceClient.from_service_account_json(
            "dummy/file/path.json"
        )
        assert client._transport._credentials == creds

        assert client._transport._host == "gameservices.googleapis.com:443"


def test_game_server_clusters_service_client_client_options():
    # Check the default options have their expected values.
    assert (
        GameServerClustersServiceClient.DEFAULT_OPTIONS.api_endpoint
        == "gameservices.googleapis.com"
    )

    # Check that options can be customized.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.GameServerClustersServiceClient.get_transport_class"
    ) as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = GameServerClustersServiceClient(client_options=options)
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_game_server_clusters_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.gaming_v1.services.game_server_clusters_service.GameServerClustersServiceClient.get_transport_class"
    ) as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = GameServerClustersServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_list_game_server_clusters(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.ListGameServerClustersRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.ListGameServerClustersResponse(
            next_page_token="next_page_token_value", unreachable=["unreachable_value"]
        )

        response = client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListGameServerClustersPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_game_server_clusters_field_headers():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.ListGameServerClustersRequest(parent="parent/value")

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_clusters), "__call__"
    ) as call:
        call.return_value = game_server_clusters.ListGameServerClustersResponse()
        client.list_game_server_clusters(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


def test_list_game_server_clusters_flattened():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_clusters), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.ListGameServerClustersResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.list_game_server_clusters(parent="parent_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"


def test_list_game_server_clusters_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_game_server_clusters(
            game_server_clusters.ListGameServerClustersRequest(), parent="parent_value"
        )


def test_list_game_server_clusters_pager():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_clusters), "__call__"
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
                game_server_clusters=[], next_page_token="def"
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster()],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ]
            ),
            RuntimeError,
        )
        results = [i for i in client.list_game_server_clusters(request={})]
        assert len(results) == 6
        assert all(
            isinstance(i, game_server_clusters.GameServerCluster) for i in results
        )


def test_list_game_server_clusters_pages():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.list_game_server_clusters), "__call__"
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
                game_server_clusters=[], next_page_token="def"
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[game_server_clusters.GameServerCluster()],
                next_page_token="ghi",
            ),
            game_server_clusters.ListGameServerClustersResponse(
                game_server_clusters=[
                    game_server_clusters.GameServerCluster(),
                    game_server_clusters.GameServerCluster(),
                ]
            ),
            RuntimeError,
        )
        pages = list(client.list_game_server_clusters(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_get_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.GetGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.GameServerCluster(
            name="name_value", etag="etag_value", description="description_value"
        )

        response = client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, game_server_clusters.GameServerCluster)
    assert response.name == "name_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


def test_get_game_server_cluster_field_headers():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = game_server_clusters.GetGameServerClusterRequest(name="name/value")

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_cluster), "__call__"
    ) as call:
        call.return_value = game_server_clusters.GameServerCluster()
        client.get_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_get_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.get_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.GameServerCluster()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.get_game_server_cluster(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_get_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_game_server_cluster(
            game_server_clusters.GetGameServerClusterRequest(), name="name_value"
        )


def test_create_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.CreateGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.create_game_server_cluster(
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
        assert args[0].parent == "parent_value"
        assert args[0].game_server_cluster == game_server_clusters.GameServerCluster(
            name="name_value"
        )
        assert args[0].game_server_cluster_id == "game_server_cluster_id_value"


def test_create_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
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


def test_preview_create_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.PreviewCreateGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_create_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewCreateGameServerClusterResponse(
            etag="etag_value"
        )

        response = client.preview_create_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewCreateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_delete_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.DeleteGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.delete_game_server_cluster(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_delete_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_game_server_cluster(
            game_server_clusters.DeleteGameServerClusterRequest(), name="name_value"
        )


def test_preview_delete_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.PreviewDeleteGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_delete_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewDeleteGameServerClusterResponse(
            etag="etag_value"
        )

        response = client.preview_delete_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewDeleteGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_update_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.UpdateGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_game_server_cluster_flattened():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.update_game_server_cluster(
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].game_server_cluster == game_server_clusters.GameServerCluster(
            name="name_value"
        )
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_game_server_cluster_flattened_error():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_game_server_cluster(
            game_server_clusters.UpdateGameServerClusterRequest(),
            game_server_cluster=game_server_clusters.GameServerCluster(
                name="name_value"
            ),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_preview_update_game_server_cluster(transport: str = "grpc"):
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = game_server_clusters.PreviewUpdateGameServerClusterRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_update_game_server_cluster), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = game_server_clusters.PreviewUpdateGameServerClusterResponse(
            etag="etag_value"
        )

        response = client.preview_update_game_server_cluster(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, game_server_clusters.PreviewUpdateGameServerClusterResponse
    )
    assert response.etag == "etag_value"


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    with pytest.raises(ValueError):
        client = GameServerClustersServiceClient(
            credentials=credentials.AnonymousCredentials(), transport=transport
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GameServerClustersServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    client = GameServerClustersServiceClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials()
    )
    assert isinstance(
        client._transport, transports.GameServerClustersServiceGrpcTransport
    )


def test_game_server_clusters_service_base_transport():
    # Instantiate the base transport.
    transport = transports.GameServerClustersServiceTransport(
        credentials=credentials.AnonymousCredentials()
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

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_game_server_clusters_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        GameServerClustersServiceClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",)
        )


def test_game_server_clusters_service_host_no_port():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com"
        ),
        transport="grpc",
    )
    assert client._transport._host == "gameservices.googleapis.com:443"


def test_game_server_clusters_service_host_with_port():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com:8000"
        ),
        transport="grpc",
    )
    assert client._transport._host == "gameservices.googleapis.com:8000"


def test_game_server_clusters_service_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")
    transport = transports.GameServerClustersServiceGrpcTransport(channel=channel)
    assert transport.grpc_channel is channel


def test_game_server_clusters_service_grpc_lro_client():
    client = GameServerClustersServiceClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc"
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_game_server_cluster_path():
    project = "squid"
    location = "clam"
    realm = "whelk"
    cluster = "octopus"

    expected = "projects/{project}/locations/{location}/realms/{realm}/gameServerClusters/{cluster}".format(
        project=project, location=location, realm=realm, cluster=cluster
    )
    actual = GameServerClustersServiceClient.game_server_cluster_path(
        project, location, realm, cluster
    )
    assert expected == actual
