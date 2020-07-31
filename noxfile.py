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

import nox  # type: ignore


@nox.session(python=['3.6', '3.7'])
def unit(session):
    """Run the unit test suite."""
    default(session)


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def system(session):
    """Run the system test suite."""
    system_test_path = os.path.join("tests", "system.py")
    system_test_folder_path = os.path.join("tests", "system")

    # Check the value of `RUN_SYSTEM_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_SYSTEM_TESTS", "true") == "false":
        session.skip("RUN_SYSTEM_TESTS is set to false, skipping")
    # Sanity check: Only run tests if the environment variable is set.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""):
        session.skip("Credentials must be set via environment variable")

    session.install('coverage', 'pytest', 'pytest-cov', 'asyncmock', 'pytest-asyncio')
    session.install('-e', '.')

    session.run(
        'py.test',
        '--quiet',
        '--cov=google/cloud/gaming_v1beta/',
        '--cov-config=.coveragerc',
        '--cov-report=term',
        '--cov-report=html',
        os.path.join('tests', 'unit',)
    )


@nox.session(python=['3.6', '3.7'])
def mypy(session):
    """Run the type checker."""
    session.install('mypy')
    session.install('.')
    session.run(
        'mypy',
        'google',
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def docfx(session):
    """Build the docfx yaml files for this library."""

    session.install("-e", ".")
    session.install("sphinx", "alabaster", "recommonmark", "sphinx-docfx-yaml")

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-D",
        (
            "extensions=sphinx.ext.autodoc,"
            "sphinx.ext.autosummary,"
            "docfx_yaml.extension,"
            "sphinx.ext.intersphinx,"
            "sphinx.ext.coverage,"
            "sphinx.ext.napoleon,"
            "sphinx.ext.todo,"
            "sphinx.ext.viewcode,"
            "recommonmark"
        ),
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )
