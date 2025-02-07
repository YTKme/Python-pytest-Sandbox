"""
Configure Test
~~~~~~~~~~~~~~

This module implement main test configuration for the Sandbox.
"""

from itertools import product
import json
from pathlib import Path
import platform

import pytest
from pytest import (
    Config,
    ExitCode,
    Metafunc,
    Parser,
    PytestPluginManager,
    Session,
    Item,
    CallInfo,
    TestReport,
)

import tealogger

CURRENT_MODULE_PATH = Path(__file__).parent.expanduser().resolve()

# Configure conftest_logger
tealogger.configure(
    configuration=CURRENT_MODULE_PATH.parents[1]
    / "configuration/sandbox.logger.json"
)
conftest_logger = tealogger.get_logger(__name__)


def pytest_load_initial_conftests(
    early_config: Config,
    parser: Parser,
    args: list[str]
) -> None:
    """Load Initial Test Configuration

    Called to implement the loading of initial conftest file(s) ahead of
    command line option parsing.

    NOTE: Not called for conftest file(s)

    :param early_config: The pytest configuration object
    :type early_config: pytest.Config
    :param parser: The parser to add command line option(s)
    :type parser: pytest.Parser
    :param args: The list of argument(s) passed on the command line
    :type args: list[str]
    """
    conftest_logger.info("pytest Load Initial Configure Test")
    conftest_logger.debug(f"Early Configuration: {early_config}")
    conftest_logger.debug(f"Parser: {parser}")
    conftest_logger.debug(f"Argument: {args}")


def pytest_cmdline_parse(
    pluginmanager: PytestPluginManager,
    args: list[str]
) -> Config | None:
    """Parse Command Line

    Return an initialized configuration object, parsing the specified
    list of argument(s).

    NOTE: Not called for conftest file(s)

    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    :param args: The list of argument(s) passed on the command line
    :type args: list[str]

    :returns: The pytest configuration object
    :rtype: pytest.Config | None
    """
    conftest_logger.info("pytest Command Line Parse")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")
    conftest_logger.debug(f"Argument: {args}")


def pytest_addhooks(pluginmanager: PytestPluginManager):
    conftest_logger.info("pytest Add Hook")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager):
    """Register Command Line Option(s)

    Register argparse style options and ini style config values, called
    once at the beginning of a test run.

    :param parser: The parser to add command line option(s)
    :type parser: pytest.Parser
    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    conftest_logger.info("pytest Add Option")
    conftest_logger.debug(f"Parser: {parser}")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")


def pytest_cmdline_main(config: Config):
    conftest_logger.info("pytest Command Line Main")
    conftest_logger.debug(f"Config: {config}")


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration.

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Configure")
    conftest_logger.debug(f"Config: {config}")


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the Session object has been created and before
    performing collection and entering the run test loop.

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info("pytest Session Start")
    conftest_logger.debug(f"Session: {session}")


def pytest_generate_tests(metafunc: Metafunc):
    """Generate Test Hook

    Dynamically parametrize test(s) using test data from a JSON
    (JavaScript Object Notation) file. The data will align with the
    class and function name of the test(s).

    :param metafunc: Objects passed to the pytest_generate_tests hook
    :type metafunc: pytest.Metafunc
    """
    conftest_logger.info("pytest Generate Test")
    conftest_logger.debug(f"Metafunc: {metafunc}")
    conftest_logger.debug(f"Module Name: {metafunc.module.__name__}")
    conftest_logger.debug(f"Class Name: {metafunc.cls.__name__}")
    conftest_logger.debug(f"Function Name: {metafunc.function.__name__}")
    conftest_logger.debug(f"Fixture Names: {metafunc.fixturenames}")

    # Parse metafunc name
    module_name = metafunc.module.__name__.split(".")[-1]
    module_path = Path(metafunc.module.__file__).parent
    class_name = metafunc.cls.__name__
    function_name = metafunc.function.__name__


def pytest_sessionfinish(session: Session, exitstatus: int | ExitCode):
    """Finish Session

    Called after whole test run finished, right before returning the
    exit status to the system.

    NOTE: Run once

    :param session: The pytest session object
    :type session: pytest.Session
    :param exitstatus: The status which pytest will return to the system
    :type exitstatus: Union[int, pytest.ExitCode]
    """
    conftest_logger.info("pytest Session Finish")
    conftest_logger.debug(f"Session: {session}")
    conftest_logger.debug(f"Exit Status: {exitstatus}")


def pytest_unconfigure(config: Config):
    """Unconfigure Test

    Called before test process is exited.

    NOTE: Run once

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Unconfigure")
    conftest_logger.debug(f"Config: {config}")


def pytest_collection(session: Session):
    conftest_logger.info("pytest Collection")
    conftest_logger.debug(f"Session: {session}")


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport | None:
    """Run Test Make Report

    Called to create a pytest TestReport for each of the setup, call
    and teardown runtest phases of a test item.

    :param item: The pytest item object
    :type item: pytest.Item
    :param call: The pytest call information for the phase
    :type call: pytest.CallInfo[None]

    :returns: The pytest TestReport object
    :rtype: pytest.TestReport | None
    """
    conftest_logger.info("pytest Run Test Make Report")
    conftest_logger.debug(f"Item: {item}")
    conftest_logger.debug(f"Call: {call}")

    report = yield
    conftest_logger.debug(f"Report: {report}")

    return report
