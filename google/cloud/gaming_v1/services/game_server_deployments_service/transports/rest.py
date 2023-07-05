# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

import dataclasses
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import (
    gapic_v1,
    operations_v1,
    path_template,
    rest_helpers,
    rest_streaming,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
import grpc  # type: ignore
from requests import __version__ as requests_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.longrunning import operations_pb2  # type: ignore

from google.cloud.gaming_v1.types import game_server_deployments

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .base import GameServerDeploymentsServiceTransport

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class GameServerDeploymentsServiceRestInterceptor:
    """Interceptor for GameServerDeploymentsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GameServerDeploymentsServiceRestTransport.

    .. code-block:: python
        class MyCustomGameServerDeploymentsServiceInterceptor(GameServerDeploymentsServiceRestInterceptor):
            def pre_create_game_server_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_game_server_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_game_server_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_game_server_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_deployment_state(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_deployment_state(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_game_server_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_game_server_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_game_server_deployment_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_game_server_deployment_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_game_server_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_game_server_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_preview_game_server_deployment_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_preview_game_server_deployment_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_game_server_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_game_server_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_game_server_deployment_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_game_server_deployment_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GameServerDeploymentsServiceRestTransport(interceptor=MyCustomGameServerDeploymentsServiceInterceptor())
        client = GameServerDeploymentsServiceClient(transport=transport)


    """

    def pre_create_game_server_deployment(
        self,
        request: game_server_deployments.CreateGameServerDeploymentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.CreateGameServerDeploymentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for create_game_server_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_create_game_server_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_game_server_deployment

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_game_server_deployment(
        self,
        request: game_server_deployments.DeleteGameServerDeploymentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.DeleteGameServerDeploymentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for delete_game_server_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_delete_game_server_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_game_server_deployment

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_fetch_deployment_state(
        self,
        request: game_server_deployments.FetchDeploymentStateRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.FetchDeploymentStateRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for fetch_deployment_state

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_fetch_deployment_state(
        self, response: game_server_deployments.FetchDeploymentStateResponse
    ) -> game_server_deployments.FetchDeploymentStateResponse:
        """Post-rpc interceptor for fetch_deployment_state

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_get_game_server_deployment(
        self,
        request: game_server_deployments.GetGameServerDeploymentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.GetGameServerDeploymentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for get_game_server_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_get_game_server_deployment(
        self, response: game_server_deployments.GameServerDeployment
    ) -> game_server_deployments.GameServerDeployment:
        """Post-rpc interceptor for get_game_server_deployment

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_get_game_server_deployment_rollout(
        self,
        request: game_server_deployments.GetGameServerDeploymentRolloutRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.GetGameServerDeploymentRolloutRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for get_game_server_deployment_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_get_game_server_deployment_rollout(
        self, response: game_server_deployments.GameServerDeploymentRollout
    ) -> game_server_deployments.GameServerDeploymentRollout:
        """Post-rpc interceptor for get_game_server_deployment_rollout

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_list_game_server_deployments(
        self,
        request: game_server_deployments.ListGameServerDeploymentsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.ListGameServerDeploymentsRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for list_game_server_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_list_game_server_deployments(
        self, response: game_server_deployments.ListGameServerDeploymentsResponse
    ) -> game_server_deployments.ListGameServerDeploymentsResponse:
        """Post-rpc interceptor for list_game_server_deployments

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_preview_game_server_deployment_rollout(
        self,
        request: game_server_deployments.PreviewGameServerDeploymentRolloutRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.PreviewGameServerDeploymentRolloutRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for preview_game_server_deployment_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_preview_game_server_deployment_rollout(
        self,
        response: game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
    ) -> game_server_deployments.PreviewGameServerDeploymentRolloutResponse:
        """Post-rpc interceptor for preview_game_server_deployment_rollout

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_update_game_server_deployment(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.UpdateGameServerDeploymentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for update_game_server_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_update_game_server_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_game_server_deployment

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response

    def pre_update_game_server_deployment_rollout(
        self,
        request: game_server_deployments.UpdateGameServerDeploymentRolloutRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        game_server_deployments.UpdateGameServerDeploymentRolloutRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for update_game_server_deployment_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GameServerDeploymentsService server.
        """
        return request, metadata

    def post_update_game_server_deployment_rollout(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_game_server_deployment_rollout

        Override in a subclass to manipulate the response
        after it is returned by the GameServerDeploymentsService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class GameServerDeploymentsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: GameServerDeploymentsServiceRestInterceptor


class GameServerDeploymentsServiceRestTransport(GameServerDeploymentsServiceTransport):
    """REST backend transport for GameServerDeploymentsService.

    The game server deployment is used to control the deployment
    of Agones fleets.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(
        self,
        *,
        host: str = "gameservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[GameServerDeploymentsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or GameServerDeploymentsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateGameServerDeployment(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("CreateGameServerDeployment")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "deploymentId": "",
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.CreateGameServerDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create game server
            deployment method over HTTP.

                Args:
                    request (~.game_server_deployments.CreateGameServerDeploymentRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.CreateGameServerDeployment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*}/gameServerDeployments",
                    "body": "game_server_deployment",
                },
            ]
            request, metadata = self._interceptor.pre_create_game_server_deployment(
                request, metadata
            )
            pb_request = game_server_deployments.CreateGameServerDeploymentRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_game_server_deployment(resp)
            return resp

    class _DeleteGameServerDeployment(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("DeleteGameServerDeployment")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.DeleteGameServerDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete game server
            deployment method over HTTP.

                Args:
                    request (~.game_server_deployments.DeleteGameServerDeploymentRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.DeleteGameServerDeployment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/gameServerDeployments/*}",
                },
            ]
            request, metadata = self._interceptor.pre_delete_game_server_deployment(
                request, metadata
            )
            pb_request = game_server_deployments.DeleteGameServerDeploymentRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_game_server_deployment(resp)
            return resp

    class _FetchDeploymentState(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("FetchDeploymentState")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.FetchDeploymentStateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> game_server_deployments.FetchDeploymentStateResponse:
            r"""Call the fetch deployment state method over HTTP.

            Args:
                request (~.game_server_deployments.FetchDeploymentStateRequest):
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

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/gameServerDeployments/*}:fetchDeploymentState",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_fetch_deployment_state(
                request, metadata
            )
            pb_request = game_server_deployments.FetchDeploymentStateRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = game_server_deployments.FetchDeploymentStateResponse()
            pb_resp = game_server_deployments.FetchDeploymentStateResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fetch_deployment_state(resp)
            return resp

    class _GetGameServerDeployment(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("GetGameServerDeployment")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.GetGameServerDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> game_server_deployments.GameServerDeployment:
            r"""Call the get game server
            deployment method over HTTP.

                Args:
                    request (~.game_server_deployments.GetGameServerDeploymentRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.GetGameServerDeployment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.game_server_deployments.GameServerDeployment:
                        A game server deployment resource.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/gameServerDeployments/*}",
                },
            ]
            request, metadata = self._interceptor.pre_get_game_server_deployment(
                request, metadata
            )
            pb_request = game_server_deployments.GetGameServerDeploymentRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = game_server_deployments.GameServerDeployment()
            pb_resp = game_server_deployments.GameServerDeployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_game_server_deployment(resp)
            return resp

    class _GetGameServerDeploymentRollout(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("GetGameServerDeploymentRollout")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.GetGameServerDeploymentRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> game_server_deployments.GameServerDeploymentRollout:
            r"""Call the get game server
            deployment rollout method over HTTP.

                Args:
                    request (~.game_server_deployments.GetGameServerDeploymentRolloutRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.GetGameServerDeploymentRollout.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.game_server_deployments.GameServerDeploymentRollout:
                        The game server deployment rollout
                    which represents the desired rollout
                    state.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/gameServerDeployments/*}/rollout",
                },
            ]
            (
                request,
                metadata,
            ) = self._interceptor.pre_get_game_server_deployment_rollout(
                request, metadata
            )
            pb_request = (
                game_server_deployments.GetGameServerDeploymentRolloutRequest.pb(
                    request
                )
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = game_server_deployments.GameServerDeploymentRollout()
            pb_resp = game_server_deployments.GameServerDeploymentRollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_game_server_deployment_rollout(resp)
            return resp

    class _ListGameServerDeployments(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("ListGameServerDeployments")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.ListGameServerDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> game_server_deployments.ListGameServerDeploymentsResponse:
            r"""Call the list game server
            deployments method over HTTP.

                Args:
                    request (~.game_server_deployments.ListGameServerDeploymentsRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.ListGameServerDeployments.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.game_server_deployments.ListGameServerDeploymentsResponse:
                        Response message for
                    GameServerDeploymentsService.ListGameServerDeployments.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/gameServerDeployments",
                },
            ]
            request, metadata = self._interceptor.pre_list_game_server_deployments(
                request, metadata
            )
            pb_request = game_server_deployments.ListGameServerDeploymentsRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = game_server_deployments.ListGameServerDeploymentsResponse()
            pb_resp = game_server_deployments.ListGameServerDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_game_server_deployments(resp)
            return resp

    class _PreviewGameServerDeploymentRollout(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("PreviewGameServerDeploymentRollout")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.PreviewGameServerDeploymentRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> game_server_deployments.PreviewGameServerDeploymentRolloutResponse:
            r"""Call the preview game server
            deployment rollout method over HTTP.

                Args:
                    request (~.game_server_deployments.PreviewGameServerDeploymentRolloutRequest):
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

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout:preview",
                    "body": "rollout",
                },
            ]
            (
                request,
                metadata,
            ) = self._interceptor.pre_preview_game_server_deployment_rollout(
                request, metadata
            )
            pb_request = (
                game_server_deployments.PreviewGameServerDeploymentRolloutRequest.pb(
                    request
                )
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = game_server_deployments.PreviewGameServerDeploymentRolloutResponse()
            pb_resp = (
                game_server_deployments.PreviewGameServerDeploymentRolloutResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_preview_game_server_deployment_rollout(resp)
            return resp

    class _UpdateGameServerDeployment(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("UpdateGameServerDeployment")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "updateMask": {},
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.UpdateGameServerDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update game server
            deployment method over HTTP.

                Args:
                    request (~.game_server_deployments.UpdateGameServerDeploymentRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.UpdateGameServerDeployment.
                    Only allows updates for labels.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{game_server_deployment.name=projects/*/locations/*/gameServerDeployments/*}",
                    "body": "game_server_deployment",
                },
            ]
            request, metadata = self._interceptor.pre_update_game_server_deployment(
                request, metadata
            )
            pb_request = game_server_deployments.UpdateGameServerDeploymentRequest.pb(
                request
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_game_server_deployment(resp)
            return resp

    class _UpdateGameServerDeploymentRollout(GameServerDeploymentsServiceRestStub):
        def __hash__(self):
            return hash("UpdateGameServerDeploymentRollout")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "updateMask": {},
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: game_server_deployments.UpdateGameServerDeploymentRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update game server
            deployment rollout method over HTTP.

                Args:
                    request (~.game_server_deployments.UpdateGameServerDeploymentRolloutRequest):
                        The request object. Request message for
                    GameServerDeploymentsService.UpdateGameServerRolloutDeployment.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout",
                    "body": "rollout",
                },
            ]
            (
                request,
                metadata,
            ) = self._interceptor.pre_update_game_server_deployment_rollout(
                request, metadata
            )
            pb_request = (
                game_server_deployments.UpdateGameServerDeploymentRolloutRequest.pb(
                    request
                )
            )
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    including_default_value_fields=False,
                    use_integers_for_enums=True,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_game_server_deployment_rollout(resp)
            return resp

    @property
    def create_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.CreateGameServerDeploymentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGameServerDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.DeleteGameServerDeploymentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGameServerDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_deployment_state(
        self,
    ) -> Callable[
        [game_server_deployments.FetchDeploymentStateRequest],
        game_server_deployments.FetchDeploymentStateResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchDeploymentState(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRequest],
        game_server_deployments.GameServerDeployment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGameServerDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRolloutRequest],
        game_server_deployments.GameServerDeploymentRollout,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGameServerDeploymentRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_game_server_deployments(
        self,
    ) -> Callable[
        [game_server_deployments.ListGameServerDeploymentsRequest],
        game_server_deployments.ListGameServerDeploymentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGameServerDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def preview_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.PreviewGameServerDeploymentRolloutRequest],
        game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PreviewGameServerDeploymentRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGameServerDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRolloutRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGameServerDeploymentRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("GameServerDeploymentsServiceRestTransport",)