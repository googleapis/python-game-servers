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
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.gaming_v1beta.types import game_server_configs


class ListGameServerConfigsPager:
    """A pager for iterating through ``list_game_server_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``game_server_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListGameServerConfigs`` requests and continue to iterate
    through the ``game_server_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., game_server_configs.ListGameServerConfigsResponse],
        request: game_server_configs.ListGameServerConfigsRequest,
        response: game_server_configs.ListGameServerConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gaming_v1beta.types.ListGameServerConfigsRequest):
                The initial request object.
            response (google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = game_server_configs.ListGameServerConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[game_server_configs.ListGameServerConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[game_server_configs.GameServerConfig]:
        for page in self.pages:
            yield from page.game_server_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListGameServerConfigsAsyncPager:
    """A pager for iterating through ``list_game_server_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``game_server_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListGameServerConfigs`` requests and continue to iterate
    through the ``game_server_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[game_server_configs.ListGameServerConfigsResponse]
        ],
        request: game_server_configs.ListGameServerConfigsRequest,
        response: game_server_configs.ListGameServerConfigsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gaming_v1beta.types.ListGameServerConfigsRequest):
                The initial request object.
            response (google.cloud.gaming_v1beta.types.ListGameServerConfigsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = game_server_configs.ListGameServerConfigsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterable[game_server_configs.ListGameServerConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[game_server_configs.GameServerConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.game_server_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
