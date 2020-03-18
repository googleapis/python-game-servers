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
from google.cloud.gaming_v1.services.realms_service import RealmsServiceClient
from google.cloud.gaming_v1.services.realms_service import pagers
from google.cloud.gaming_v1.services.realms_service import transports
from google.cloud.gaming_v1.types import common
from google.cloud.gaming_v1.types import realms
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


def test_realms_service_client_from_service_account_file():
    creds = credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = RealmsServiceClient.from_service_account_file("dummy/file/path.json")
        assert client._transport._credentials == creds

        client = RealmsServiceClient.from_service_account_json("dummy/file/path.json")
        assert client._transport._credentials == creds

        assert client._transport._host == "gameservices.googleapis.com:443"


def test_realms_service_client_client_options():
    # Check the default options have their expected values.
    assert (
        RealmsServiceClient.DEFAULT_OPTIONS.api_endpoint
        == "gameservices.googleapis.com"
    )

    # Check that options can be customized.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch(
        "google.cloud.gaming_v1.services.realms_service.RealmsServiceClient.get_transport_class"
    ) as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = RealmsServiceClient(client_options=options)
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_realms_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.gaming_v1.services.realms_service.RealmsServiceClient.get_transport_class"
    ) as gtc:
        transport = gtc.return_value = mock.MagicMock()
        client = RealmsServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
        )
        transport.assert_called_once_with(credentials=None, host="squid.clam.whelk")


def test_list_realms(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.ListRealmsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_realms), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = realms.ListRealmsResponse(
            next_page_token="next_page_token_value", unreachable=["unreachable_value"]
        )

        response = client.list_realms(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListRealmsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.unreachable == ["unreachable_value"]


def test_list_realms_field_headers():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = realms.ListRealmsRequest(parent="parent/value")

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_realms), "__call__") as call:
        call.return_value = realms.ListRealmsResponse()
        client.list_realms(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "parent=parent/value") in kw["metadata"]


def test_list_realms_flattened():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_realms), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = realms.ListRealmsResponse()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.list_realms(parent="parent_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"


def test_list_realms_flattened_error():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_realms(realms.ListRealmsRequest(), parent="parent_value")


def test_list_realms_pager():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_realms), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            realms.ListRealmsResponse(
                realms=[realms.Realm(), realms.Realm(), realms.Realm()],
                next_page_token="abc",
            ),
            realms.ListRealmsResponse(realms=[], next_page_token="def"),
            realms.ListRealmsResponse(realms=[realms.Realm()], next_page_token="ghi"),
            realms.ListRealmsResponse(realms=[realms.Realm(), realms.Realm()]),
            RuntimeError,
        )
        results = [i for i in client.list_realms(request={})]
        assert len(results) == 6
        assert all(isinstance(i, realms.Realm) for i in results)


def test_list_realms_pages():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials)

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.list_realms), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            realms.ListRealmsResponse(
                realms=[realms.Realm(), realms.Realm(), realms.Realm()],
                next_page_token="abc",
            ),
            realms.ListRealmsResponse(realms=[], next_page_token="def"),
            realms.ListRealmsResponse(realms=[realms.Realm()], next_page_token="ghi"),
            realms.ListRealmsResponse(realms=[realms.Realm(), realms.Realm()]),
            RuntimeError,
        )
        pages = list(client.list_realms(request={}).pages)
        for page, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page.raw_page.next_page_token == token


def test_get_realm(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.GetRealmRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = realms.Realm(
            name="name_value",
            time_zone="time_zone_value",
            etag="etag_value",
            description="description_value",
        )

        response = client.get_realm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, realms.Realm)
    assert response.name == "name_value"
    assert response.time_zone == "time_zone_value"
    assert response.etag == "etag_value"
    assert response.description == "description_value"


def test_get_realm_field_headers():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = realms.GetRealmRequest(name="name/value")

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_realm), "__call__") as call:
        call.return_value = realms.Realm()
        client.get_realm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=name/value") in kw["metadata"]


def test_get_realm_flattened():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.get_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = realms.Realm()

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.get_realm(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_get_realm_flattened_error():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_realm(realms.GetRealmRequest(), name="name_value")


def test_create_realm(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.CreateRealmRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.create_realm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_realm_flattened():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.create_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.create_realm(
            parent="parent_value",
            realm=realms.Realm(name="name_value"),
            realm_id="realm_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].parent == "parent_value"
        assert args[0].realm == realms.Realm(name="name_value")
        assert args[0].realm_id == "realm_id_value"


def test_create_realm_flattened_error():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_realm(
            realms.CreateRealmRequest(),
            parent="parent_value",
            realm=realms.Realm(name="name_value"),
            realm_id="realm_id_value",
        )


def test_delete_realm(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.DeleteRealmRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.delete_realm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_realm_flattened():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.delete_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.delete_realm(name="name_value")

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].name == "name_value"


def test_delete_realm_flattened_error():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_realm(realms.DeleteRealmRequest(), name="name_value")


def test_update_realm(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.UpdateRealmRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")

        response = client.update_realm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_realm_flattened():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client._transport.update_realm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = client.update_realm(
            realm=realms.Realm(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0].realm == realms.Realm(name="name_value")
        assert args[0].update_mask == field_mask.FieldMask(paths=["paths_value"])


def test_update_realm_flattened_error():
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_realm(
            realms.UpdateRealmRequest(),
            realm=realms.Realm(name="name_value"),
            update_mask=field_mask.FieldMask(paths=["paths_value"]),
        )


def test_preview_realm_update(transport: str = "grpc"):
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport=transport
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = realms.PreviewRealmUpdateRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client._transport.preview_realm_update), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = realms.PreviewRealmUpdateResponse(etag="etag_value")

        response = client.preview_realm_update(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, realms.PreviewRealmUpdateResponse)
    assert response.etag == "etag_value"


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.RealmsServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    with pytest.raises(ValueError):
        client = RealmsServiceClient(
            credentials=credentials.AnonymousCredentials(), transport=transport
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.RealmsServiceGrpcTransport(
        credentials=credentials.AnonymousCredentials()
    )
    client = RealmsServiceClient(transport=transport)
    assert client._transport is transport


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = RealmsServiceClient(credentials=credentials.AnonymousCredentials())
    assert isinstance(client._transport, transports.RealmsServiceGrpcTransport)


def test_realms_service_base_transport():
    # Instantiate the base transport.
    transport = transports.RealmsServiceTransport(
        credentials=credentials.AnonymousCredentials()
    )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "list_realms",
        "get_realm",
        "create_realm",
        "delete_realm",
        "update_realm",
        "preview_realm_update",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client


def test_realms_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(auth, "default") as adc:
        adc.return_value = (credentials.AnonymousCredentials(), None)
        RealmsServiceClient()
        adc.assert_called_once_with(
            scopes=("https://www.googleapis.com/auth/cloud-platform",)
        )


def test_realms_service_host_no_port():
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com"
        ),
        transport="grpc",
    )
    assert client._transport._host == "gameservices.googleapis.com:443"


def test_realms_service_host_with_port():
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gameservices.googleapis.com:8000"
        ),
        transport="grpc",
    )
    assert client._transport._host == "gameservices.googleapis.com:8000"


def test_realms_service_grpc_transport_channel():
    channel = grpc.insecure_channel("http://localhost/")
    transport = transports.RealmsServiceGrpcTransport(channel=channel)
    assert transport.grpc_channel is channel


def test_realms_service_grpc_lro_client():
    client = RealmsServiceClient(
        credentials=credentials.AnonymousCredentials(), transport="grpc"
    )
    transport = client._transport

    # Ensure that we have a api-core operations client.
    assert isinstance(transport.operations_client, operations_v1.OperationsClient)

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_realm_path():
    project = "squid"
    location = "clam"
    realm = "whelk"

    expected = "projects/{project}/locations/{location}/realms/{realm}".format(
        project=project, location=location, realm=realm
    )
    actual = RealmsServiceClient.realm_path(project, location, realm)
    assert expected == actual
