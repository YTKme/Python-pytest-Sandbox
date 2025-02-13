"""
Configure Test
~~~~~~~~~~~~~~

This module implement main test configuration for the Sandbox.
"""

from itertools import product
import json
from pathlib import Path
import platform
from typing import Any

import pytest
from pytest import (
    Class,
    CollectReport,
    Collector,
    Config,
    ExitCode,
    Function,
    Metafunc,
    Module,
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


######################
# Bootstrapping Hook #
######################

def pytest_load_initial_conftests(
    early_config: Config,
    parser: Parser,
    args: list[str]
) -> None:
    """Load Initial Test Configuration Hook

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
    """Parse Command Line Hook

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


def pytest_cmdline_main(config: Config) -> ExitCode | int | None:
    """Command Line Main Hook

    Called for performing the main command line action.

    :param config: The pytest configuration object
    :type config: pytest.Config

    :returns: The exit code
    :rtype: pytest.ExitCode | int | None
    """
    conftest_logger.info("pytest Command Line Main")
    conftest_logger.debug(f"Config: {config}")


#######################
# Initialization Hook #
#######################

def pytest_addoption(
    parser: Parser,
    pluginmanager: PytestPluginManager
) -> None:
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


def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    """Add Hook(s)

    Called at plugin registration time to allow adding new hook(s).

    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    conftest_logger.info("pytest Add Hook")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow perform of initial configuration.

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Configure")
    conftest_logger.debug(f"Config: {config}")


def pytest_unconfigure(config: Config) -> None:
    """Unconfigure Test

    Called before test process is exited.

    NOTE: Run once

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Unconfigure")
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


def pytest_sessionfinish(
    session: Session,
    exitstatus: int | ExitCode
) -> None:
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


# def pytest_plugin_registered(
#     plugin: object,
#     plugin_name: str,
#     manager: PytestPluginManager
# ) -> None:
#     """Plugin Registered

#     A new pytest plugin got registered.

#     :param plugin: The plugin module or instance
#     :type plugin: object
#     :param plugin_name: The name by which the plugin is registered
#     :type plugin_name: str
#     :param manager: The pytest plugin manager
#     :type manager: pytest.PytestPluginManager
#     """
#     conftest_logger.info("pytest Plugin Registered")
#     conftest_logger.debug(f"Plugin: {plugin}")
#     conftest_logger.debug(f"Plugin Name: {plugin_name}")
#     conftest_logger.debug(f"Manager: {manager}")


####################
# Collection Hook #
####################

def pytest_collection(session: Session) -> object | None:
    """Collection Hook

    Perform the collection phase for the given session.

    The return value is not used, but only stops further processing.

    :param session: The pytest session object
    :type session: pytest.Session

    :returns: The pytest collection object
    :rtype: object | None
    """
    conftest_logger.info("pytest Collection")
    conftest_logger.debug(f"Session: {session}")


def pytest_ignore_collect(
    collection_path: Path,
    # path: LEGACY_PATH,
    config: Config
) -> bool | None:
    """Ignore Collect Hook

    Determine whether a path should be ignored for collection.

    Return True to ignore this path for collection.

    Return None to let other plugins ignore the path for collection.

    Returning False will forcefully not ignore this path for collection,
        without giving a chance for other plugins to ignore this path.

    :param collection_path: The path to analyze
    :type collection_path: Path
    :param path: The path to analyze (deprecated)
    :type path: LEGACY_PATH
    :param config: The pytest configuration object
    :type config: pytest.Config

    :returns: Whether to ignore the collection
    :rtype: bool
    """
    conftest_logger.info("pytest Ignore Collect")
    conftest_logger.debug(f"Collection Path: {collection_path}")
    conftest_logger.debug(f"Config: {config}")


def pytest_collect_directory(
    path: Path,
    parent: Collector
) -> Collector | None:
    """Collect Directory Hook

    Create a Collector for the given directory, or None if not relevant.

    :param path: The path to analyze
    :type path: Path
    :param parent: The parent collector object
    :type parent: pytest.Collector

    :returns: The collector for the given directory
    :rtype: pytest.Collector | None
    """
    conftest_logger.info("pytest Collect Directory")
    conftest_logger.debug(f"Path: {path}")
    conftest_logger.debug(f"Parent: {parent}")


def pytest_collect_file(
    file_path: Path,
    # path: LEGACY_PATH,
    parent: Collector
) -> Collector | None:
    """Collect File Hook

    Create a Collector for the given path, or None if not relevant.

    :param file_path: The path to analyze
    :type file_path: Path
    :param path: The path to collect (deprecated)
    :type path: LEGACY_PATH
    :param parent: The parent collector object
    :type parent: pytest.Collector

    :returns: The collector for the given path
    :rtype: pytest.Collector | None
    """
    conftest_logger.info("pytest Collect File")
    conftest_logger.debug(f"File Path: {file_path}")
    conftest_logger.debug(f"Parent: {parent}")


def pytest_pycollect_makemodule(
    module_path: Path,
    # path: LEGACY_PATH,
    parent: Collector
) -> Module | None:
    """Make Module Hook

    Create a Collector for the given path, or None if not relevant.

    :param module_path: The path of the module to collect
    :type module_path: Path
    :param path: The path of the module to collect (deprecated)
    :type path: LEGACY_PATH
    :param parent: The parent collector object
    :type parent: pytest.Collector

    :returns: The pytest.Module collector
    :rtype: pytest.Module | None
    """
    conftest_logger.info("pytest pycollect Make Module")
    conftest_logger.debug(f"Module Path: {module_path}")
    conftest_logger.debug(f"Parent: {parent}")


def pytest_pycollect_makeitem(
    collector: Module | Class,
    name: str,
    obj: object
) -> None | Item | Collector | list[Item | Collector]:
    """Make Item Hook

    Create an Item for the given path, or None if not relevant.

    :param collector: The module/class collector
    :type collector: pytest.Module | pytest.Class
    :param name: The name of the object in the module/class
    :type name: str
    :param obj: The object
    :type obj: object

    :returns: The created items/collectors
    :rtype: None | pytest.Item | pytest.Collector | list[pytest.Item | pytest.Collector]
    """
    conftest_logger.info("pytest pycollect Make Item")
    conftest_logger.debug(f"Collector: {collector}")
    conftest_logger.debug(f"Name: {name}")
    conftest_logger.debug(f"Object: {obj}")


def pytest_generate_tests(metafunc: Metafunc) -> None:
    """Generate Test Hook

    Dynamically parametrize test(s) using test data from a JSON
    (JavaScript Object Notation) file. The data will align with the
    class and function name of the test(s).

    :param metafunc: The Metafunc helper for the test function
    :type metafunc: pytest.Metafunc
    """
    conftest_logger.info("pytest Generate Test")
    conftest_logger.debug(f"Metafunc: {metafunc}")
    conftest_logger.debug(f"Module Name: {metafunc.module.__name__}")
    conftest_logger.debug(f"Class Name: {metafunc.cls.__name__}")
    conftest_logger.debug(f"Function Name: {metafunc.function.__name__}")
    conftest_logger.debug(f"Fixture Names: {metafunc.fixturenames}")


def pytest_make_parametrize_id(
    config: Config,
    val: object,
    argname: str
) -> str | None:
    """Make Parametrize ID Hook

    Return a user friendly string representation of the given value that
    will be used by @pytest.mark.parametrize calls, or None if the hook
    doesn't know about the value.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param val: The parametrized value
    :type val: object
    :param argname: The automatic parameter name produced by pytest
    :type argname: str

    :returns: The user friendly string representation of the given value
    :rtype: str
    """
    conftest_logger.info("pytest Make Parametrize ID")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Value: {val}")
    conftest_logger.debug(f"Argument Name: {argname}")


def pytest_markeval_namespace(config: Config) -> dict[str, Any]:
    """Mark Evaluate Namespace Hook

    Called when constructing the globals dictionary used for evaluating
    string conditions in xfail/skipif markers.

    :param config: The pytest configuration object
    :type config: pytest.Config

    :returns: A dictionary of additional globals to add
    :rtype: dict[str, Any]
    """
    conftest_logger.info("pytest Mark Evaluate Namespace")
    conftest_logger.debug(f"Configuration: {config}")


def pytest_collection_modifyitems(
    session: Session,
    config: Config,
    items: list[Item]
) -> None:
    """Collection Modify Items Hook

    Called after collection has been performed. May filter or re-order
    the items in-place.

    :param session: The pytest session object
    :type session: pytest.Session
    :param config: The pytest configuration object
    :type config: pytest.Config
    :param items: List of item objects
    :type items: list[pytest.Item]
    """
    conftest_logger.info("pytest Collection Modify Item")
    conftest_logger.debug(f"Session: {session}")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Item List: {items}")


def pytest_collection_finish(session: Session) -> None:
    """Collection Finish Hook

    Called after collection has been performed and modified.

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info("pytest Collection Finish")
    conftest_logger.debug(f"Session: {session}")


#####################
# Test Running Hook #
#####################

def pytest_runtestloop(session: Session) -> object | None:
    """Run Test Loop Hook

    Perform the main runtest loop (after collection finished)

    The return value is not used, but only stops further processing.

    :param session: The pytest session object
    :type session: pytest.Session

    :returns: The pytest runtestloop object
    :rtype: pytest.object | None
    """
    conftest_logger.info("pytest Run Test Loop")
    conftest_logger.debug(f"Session: {session}")


def pytest_runtest_protocol(
    item: Item,
    nextitem: Item | None
) -> object | None:
    """Run Test Protocol Hook

    Perform the runtest protocol for a single test item.

    The return value is not used, but only stops further processing.

    :param item: Test item for which the runtest protocol is performed
    :type item: pytest.Item
    :param nextitem:  The scheduled to be next test item (or None if
        this is the end my friend)
    :type nextitem: pytest.Item | None

    :returns: The pytest runtest protocol object
    :rtype: pytest.object | None
    """
    conftest_logger.info("pytest Run Test Protocol")
    conftest_logger.debug(f"Item: {item}")
    conftest_logger.debug(f"Next Item: {nextitem}")


def pytest_runtest_logstart(
    nodeid: str,
    location: tuple[str, int | None, str]
) -> None:
    """Run Test Log Start Hook

    Called at the start of running the runtest protocol for a single
    item.

    :param nodeid: Full node ID of the item
    :type nodeid: str
    :param location: A tuple of (filename, lineno, testname) where
        filename is a file path relative to config.rootpath and lineno
        is 0-based
    :type location: tuple[str, int | None, str]
    """
    conftest_logger.info("pytest Run Test Log Start")
    conftest_logger.debug(f"Node Identifier: {nodeid}")
    conftest_logger.debug(f"Location: {location}")


def pytest_runtest_logfinish(
    nodeid: str,
    location: tuple[str, int | None, str]
) -> None:
    """Run Test Log Finish Hook

    Called at the end of running the runtest protocol for a single item.

    :param nodeid: Full node ID of the item
    :type nodeid: str
    :param location: A tuple of (filename, lineno, testname) where
        filename is a file path relative to config.rootpath and lineno
        is 0-based
    :type location: tuple[str, int | None, str]
    """
    conftest_logger.info("pytest Run Test Log Finish")
    conftest_logger.debug(f"Node Identifier: {nodeid}")
    conftest_logger.debug(f"Location: {location}")


def pytest_runtest_setup(item: Item) -> None:
    """Run Test Setup Hook

    Called to perform the setup phase for a test item.

    :param item: The item
    :type item: pytest.Item
    """
    conftest_logger.info("pytest Run Test Setup")
    conftest_logger.debug(f"Item: {item}")


def pytest_runtest_call(item: Item) -> None:
    """Run Test Call Hook

    Called to run the test for test item (the call phase).

    :param item: The item
    :type item: pytest.Item
    """
    conftest_logger.info("pytest Run Test Call")
    conftest_logger.debug(f"Item: {item}")


def pytest_runtest_teardown(item: Item, nextitem: Item | None) -> None:
    """Run Test Teardown Hook

    Called to perform the teardown phase for a test item.

    :param item: The item
    :type item: pytest.Item
    :param nextitem: The scheduled to be next test item (None if no
        further test item is scheduled). This argument is used to
        perform exact teardowns, i.e. calling just enough finalizers so
        that nextitem only needs to call setup functions
    :type nextitem: pytest.Item | None
    """
    conftest_logger.info("pytest Run Test Teardown")
    conftest_logger.debug(f"Item: {item}")
    conftest_logger.debug(f"Next Item: {nextitem}")


def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> TestReport | None:
    """Run Test Make Report

    Called to create a pytest TestReport for each of the setup, call
    and teardown runtest phases of a test item.

    :param item: The item
    :type item: pytest.Item
    :param call: The CallInfo for the phase
    :type call: pytest.CallInfo[None]

    :returns: The pytest TestReport object
    :rtype: pytest.TestReport | None
    """
    conftest_logger.info("pytest Run Test Make Report")
    conftest_logger.debug(f"Item: {item}")
    conftest_logger.debug(f"Call: {call}")


def pytest_pyfunc_call(pyfuncitem: Function) -> None:
    """Pyfunc Call Hook

    Call underlying test function.

    :param pyfuncitem: The function item
    :type pyfuncitem: pytest.Function
    """
    conftest_logger.info("pytest Python Function Call")
    conftest_logger.debug(f"Python Function Item: {pyfuncitem}")


##################
# Reporting Hook #
##################

def pytest_collectstart(collector: Collector) -> None:
    """Collect Start Hook

    Collector starts collecting.

    :param collector: The collector
    :type collector: pytest.Collector
    """
    conftest_logger.info("pytest Collect Start")
    conftest_logger.debug(f"Collector: {collector}")

def pytest_make_collect_report(
    collector: Collector
) -> CollectReport | None:
    """Make Collect Report Hook

    Perform collector.collect() and return a CollectReport.

    :param collector: The collector
    :type collector: pytest.Collector

    :returns: The pytest CollectReport object
    :rtype: pytest.CollectReport | None
    """
    conftest_logger.info("pytest Make Collect Report")
    conftest_logger.debug(f"Collector: {collector}")
