"""
Configure Test
~~~~~~~~~~~~~~

This module implement main test configuration for the Sandbox.

pytest Hooks Reference: `Link <https://docs.pytest.org/en/stable/reference/reference.html#hooks>`_
"""

import json
import pdb
import platform
import warnings
from itertools import product
from pathlib import Path
from typing import Any, Literal, Mapping, Sequence

import pytest
import tealogger
from _pytest._code.code import ExceptionInfo, ExceptionRepr
from _pytest.config import Config, ExitCode, PytestPluginManager
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureDef, SubRequest
from _pytest.main import Session
from _pytest.nodes import Collector, Item
from _pytest.outcomes import Exit
from _pytest.python import Class, Function, Metafunc, Module
from _pytest.reports import CollectReport, TestReport
from _pytest.runner import CallInfo
from _pytest.terminal import TerminalReporter, TestShortLogReport
from pluggy import Result

# from _pytest.compat import LEGACY_PATH
# from _pytest.config import _PluggyPlugin
# from _pytest._code.code import ExceptionRepr
# from _pytest.fixtures import SubRequest
# from _pytest.outcomes import Exit
# from _pytest.terminal import TerminalReporter
# from pytest import (
#     Class,
#     CollectReport,
#     Collector,
#     Config,
#     ExitCode,
#     ExceptionInfo,
#     FixtureDef,
#     Function,
#     Metafunc,
#     Module,
#     Parser,
#     PytestPluginManager,
#     Session,
#     Item,
#     CallInfo,
#     TestReport,
#     TestShortLogReport,
# )

CURRENT_MODULE_PATH = Path(__file__).parent.expanduser().resolve()

# Configure conftest_logger
tealogger.configure(
    configuration=CURRENT_MODULE_PATH.parents[1] / "configuration/sandbox.logger.json"
)
conftest_logger = tealogger.get_logger(__name__)


######################
# Bootstrapping Hook #
######################


def pytest_load_initial_conftests(
    early_config: Config,
    parser: Parser,
    args: list[str],
) -> None:
    """Load Initial Test Configuration Hook

    Called to implement the loading of initial conftest file(s) ahead of
    command line option parsing.

    conftest: Not called for conftest file(s)

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
    args: list[str],
) -> Config | None:
    """Parse Command Line Hook

    Return an initialized Config, parsing the specified args.

    Stops at first non-None result.

    conftest: Not called for conftest file(s)

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

    The default implementation will invoke the configure hooks and
    pytest_runtestloop.

    Stops at first non-None result.

    conftest: This hook is only called for initial conftest(s).

    :param config: The pytest configuration object
    :type config: pytest.Config

    :returns: The exit code
    :rtype: pytest.ExitCode | int | None
    """
    conftest_logger.info("pytest Command Line Main")
    conftest_logger.debug(f"Configuration: {config}")


#######################
# Initialization Hook #
#######################


def pytest_addoption(
    parser: Parser,
    pluginmanager: PytestPluginManager,
) -> None:
    """Register Command Line Option(s)

    Register argparse-style options and ini-style config values, called
    once at the beginning of a test run.

    conftest: If a conftest plugin implements this hook, it will be
        called immediately when the conftest is registered.
    conftest: This hook is only called for initial conftest(s).

    :param parser: To add command line option(s)
    :type parser: pytest.Parser
    :param pluginmanager: The pytest plugin manager, which can be used
        to install hookspec()'s or hookimpl()'s and allow one plugin to
        call another plugin's hooks to change how command line options
        are added
    :type pluginmanager: pytest.PytestPluginManager
    """
    conftest_logger.info("pytest Add Option")
    conftest_logger.debug(f"Parser: {parser}")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")


def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    """Add Hook(s)

    Called at plugin registration time to allow adding new hook(s) via a
    call to pluginmanager.add_hookspecs(module_or_class, prefix).

    conftest: If a conftest plugin implements this hook, it will be
        called immediately when the conftest is registered.

    :param pluginmanager: The pytest plugin manager
    :type pluginmanager: pytest.PytestPluginManager
    """
    conftest_logger.info("pytest Add Hook")
    conftest_logger.debug(f"Plugin Manager: {pluginmanager}")


def pytest_configure(config: Config) -> None:
    """Configure Test

    Allow plugins and conftest files to perform initial configuration.

    conftest: This hook is called for every initial conftest file after
        command line options have been parsed. After that, the hook is
        called for other conftest files as they are registered.

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Configure")
    conftest_logger.debug(f"Configuration: {config}")


def pytest_unconfigure(config: Config) -> None:
    """Unconfigure Test

    Called before test process is exited.

    conftest: Any conftest file can implement this hook.

    NOTE: Run once

    :param config: The pytest config object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Unconfigure")
    conftest_logger.debug(f"Configuration: {config}")


def pytest_sessionstart(session: Session) -> None:
    """Start Session

    Called after the Session object has been created and before
    performing collection and entering the run test loop.

    conftest: This hook is only called for initial conftest(s).

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info("pytest Session Start")
    conftest_logger.debug(f"Session: {session}")

    # Platform Information
    # https://docs.python.org/3/library/platform.html
    conftest_logger.debug("Platform Information")
    # Cross Platform
    conftest_logger.debug("Cross Platform Information")
    conftest_logger.debug(f"Architecture: {platform.architecture()}")
    conftest_logger.debug(f"Machine: {platform.machine()}")
    conftest_logger.debug(f"Node: {platform.node()}")
    conftest_logger.debug(f"Platform: {platform.platform()}")
    conftest_logger.debug(f"Processor: {platform.processor()}")
    conftest_logger.debug(f"Python Build: {platform.python_build()}")
    conftest_logger.debug(f"Python Compiler: {platform.python_compiler()}")
    conftest_logger.debug(f"Python Branch: {platform.python_branch()}")
    conftest_logger.debug(f"Python Implementation: {platform.python_implementation()}")
    conftest_logger.debug(f"Python Revision: {platform.python_revision()}")
    conftest_logger.debug(f"Python Version: {platform.python_version()}")
    conftest_logger.debug(f"Python Version Tuple: {platform.python_version_tuple()}")
    conftest_logger.debug(f"Release: {platform.release()}")
    conftest_logger.debug(f"System: {platform.system()}")
    conftest_logger.debug(f"Version: {platform.version()}")
    conftest_logger.debug(f"Unix Name: {platform.uname()}")
    # Java Platform
    conftest_logger.debug("Java Platform Information")
    conftest_logger.debug(f"Java Version: {platform.java_ver()}")
    # Windows Platform
    conftest_logger.debug("Windows Platform Information")
    conftest_logger.debug(f"Windows Version: {platform.win32_ver()}")
    conftest_logger.debug(f"Windows Edition: {platform.win32_edition()}")
    conftest_logger.debug(f"Windows IoT: {platform.win32_is_iot()}")
    # macOS Platform
    conftest_logger.debug("macOS Platform Information")
    conftest_logger.debug(f"macOS Version: {platform.mac_ver()}")
    # iOS Platform
    # conftest_logger.debug("iOS Platform Information")
    # conftest_logger.debug(f"iOS Version: {platform.ios_ver()}")
    # Unix Platform
    conftest_logger.debug("Unix Platform Information")
    conftest_logger.debug(f"Unix libc Version: {platform.libc_ver()}")
    # Linux Platform
    # conftest_logger.debug("Linux Platform Information")
    # conftest_logger.debug(f"Linux OS Release: {platform.freedesktop_os_release()}")
    # Android Platform
    # conftest_logger.debug("Android Platform Information")
    # conftest_logger.debug(f"Android Version: {platform.android_ver()}")


def pytest_sessionfinish(
    session: Session,
    exitstatus: int | ExitCode,
) -> None:
    """Finish Session

    Called after whole test run finished, right before returning the
    exit status to the system.

    conftest: Any conftest file can implement this hook.

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

#     conftest: If a conftest plugin implements this hook, it will be
#         called immediately when the conftest is registered, once for
#         each plugin registered thus far (including itself!), and for all
#         plugins thereafter when they are registered.

#     NOTE: There are a lot of Plugin(s), disable to reduce logging.

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


###################
# Collection Hook #
###################


def pytest_collection(session: Session) -> object | None:
    """Collection Hook

    Perform the collection phase for the given session.

    Stops at first non-None result. The return value is not used, but
    only stops further processing.

    You can implement this hook to only perform some action before
    collection, for example the terminal plugin uses it to start
    displaying the collection counter (and returns None).

    conftest: This hook is only called for initial conftest(s).

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
    config: Config,
) -> bool | None:
    """Ignore Collect Hook

    Determine whether a path should be ignored for collection.

    Return True to ignore this path for collection.

    Return None to let other plugins ignore the path for collection.

    Returning False will forcefully not ignore this path for collection,
        without giving a chance for other plugins to ignore this path.

    This hook is consulted for all files and directories prior to
    calling more specific hooks.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        collection path, only conftest files in parent directories of
        the collection path are consulted (if the path is a directory,
        its own conftest file is not consulted - a directory cannot
        ignore itself!).

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
    conftest_logger.debug(f"Configuration: {config}")


def pytest_collect_directory(
    path: Path,
    parent: Collector,
) -> Collector | None:
    """Collect Directory Hook

    Create a Collector for the given directory, or None if not relevant.

    For best results, the returned collector should be a subclass of
    Directory, but this is not required.

    The new node needs to have the specified parent as a parent.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        collection path, only conftest files in parent directories of
        the collection path are consulted (if the path is a directory,
        its own conftest file is not consulted - a directory cannot
        collect itself!).

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
    parent: Collector,
) -> Collector | None:
    """Collect File Hook

    Create a Collector for the given path, or None if not relevant.

    For best results, the returned collector should be a subclass of
    File, but this is not required.

    The new node needs to have the specified parent as a parent.

    conftest: Any conftest file can implement this hook. For a given
        file path, only conftest files in parent directories of the file
        path are consulted.

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
    parent: Collector,
) -> Module | None:
    """Make Module Hook

    Return a pytest.Module collector or None for the given path.

    This hook will be called for each matching test module path. The
    pytest_collect_file hook needs to be used if you want to create test
    modules for files that do not match as a test module.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        parent collector, only conftest files in the collector's
        directory and its parent directories are consulted.

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
    obj: object,
) -> None | Item | Collector | list[Item | Collector]:
    """Make Item Hook

    Return a custom item/collector for a Python object in a module, or
    None.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        collector, only conftest files in the collector's directory and
        its parent directories are consulted.

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


def pytest_generate_tests(metafunc: Metafunc):
    """Generate Test Hook

    Generate (multiple) parametrized calls to a test function.

    Dynamically parametrize test(s) using test data from a JSON
    (JavaScript Object Notation) file. The data will align with the
    class and function name of the test(s).

    conftest: Any conftest file can implement this hook. For a given
        function definition, only conftest files in the functions's
        directory and its parent directories are consulted.

    Example Class:
        {
            "module_name":
                "ClassName": {
                    "function_name": {
                        "parameter": [
                            "expression",
                            ...
                        ],
                        ...
                    },
                    ...
                },
                ...
            },
            ...
        }

    Example Function:
        {
            "module_name":
                "function_name": {
                    "parameter": [
                        "expression",
                        ...
                    ],
                    ...
                },
                ...
            },
            ...
        }

    :param metafunc: The Metafunc helper for the test function
    :type metafunc: pytest.Metafunc
    """
    conftest_logger.info("pytest Generate Test")
    conftest_logger.debug(f"Metafunc: {metafunc}")
    # conftest_logger.debug(f"Metafunc Dictionary: {metafunc.__dict__}")
    # conftest_logger.debug(f"Module Name: {metafunc.module.__name__}")
    # conftest_logger.debug(f"Class Name: {metafunc.cls.__name__}")
    # conftest_logger.debug(f"Function Name: {metafunc.function.__name__}")
    # conftest_logger.debug(f"Fixture Names: {metafunc.fixturenames}")

    # Parse metafunc module
    module_name = metafunc.module.__name__
    module_path = Path(metafunc.module.__file__).parent

    # Load the test data
    test_data_path = None
    if (module_path / f"{module_name}.json").exists():
        test_data_path = module_path / f"{module_name}.json"
    elif (module_path / "data.json").exists():
        test_data_path = module_path / "data.json"
    conftest_logger.debug(f"Test Data Path: {test_data_path}")

    # Inject the test data
    if test_data_path:
        try:
            with open(test_data_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError as error:
            conftest_logger.warning(f"No Test Data Found: {module_name}")
            conftest_logger.error(f"Error: {error}")
            pytest.skip(f"Skip No Test Data Found: {module_name}")
        except TypeError as error:
            conftest_logger.warning(f"No Test Data Path Set: {module_name}")
            conftest_logger.error(f"Error: {error}")
            pytest.skip(f"Skip No Test Data Path Set: {module_name}")

        class_condition = [
            module_name in data,
            # Part of a class
            # The class name is in the test data
            metafunc.cls.__name__ in data[module_name] if metafunc.cls else False,
            # Part of a function (should always be true)
            # The function name is in the test data
            metafunc.function.__name__ in data[module_name][metafunc.cls.__name__]
            if metafunc.cls and metafunc.function
            else False,
        ]

        ####################
        # Class Level Test #
        ####################
        if all(class_condition):
            conftest_logger.debug("Generate Class Test")
            class_name = metafunc.cls.__name__
            function_name = metafunc.function.__name__
            function_data = data[module_name][class_name][function_name]
            test_data = function_data["data"]
            # conftest_logger.debug(f"Test Data: {test_data}")

            argument_name_list = test_data.keys()
            argument_value_list = test_data.values()
            id_list = None
            # id_list = []

            strategy = function_data["strategy"]
            # conftest_logger.debug(f"Strategy: {strategy}")

            match strategy:
                case "product":
                    # Create the cartesian product of the argument value to test
                    argument_value_list = list(product(*argument_value_list))
                case _:
                    # Create a zip of the argument value to test
                    argument_value_list = list(zip(*argument_value_list))

            # NOTE: Default
            # for argument_value_tuple in argument_value_list:
            #     id_list.append("-".join(map(str, argument_value_tuple)))

            # NOTE: There maybe a better way for this?
            # if "name" in function_data:
            #     id_list.extend(
            #         [function_data["name"]] * len(argument_value_list)
            #     )

            # Exclude
            if (
                "exclude" in function_data
                and "strategy" in function_data["exclude"]
                and "data" in function_data["exclude"]
            ):
                exclude_strategy = function_data["exclude"]["strategy"]
                exclude_data = function_data["exclude"]["data"]
                # conftest_logger.debug(f"Exclude Strategy: {exclude_strategy}")
                # conftest_logger.debug(f"Exclude Data: {exclude_data}")

                match exclude_strategy:
                    case "product":
                        # Create the cartesian product of the exclude data
                        exclude_value_list = list(product(*exclude_data.values()))
                    case _:
                        # Default
                        exclude_value_list = list(product(*exclude_data.values()))

                # conftest_logger.debug(f"Exclude Value List: {exclude_value_list}")

                # Remove the exclude value from the argument value
                # NOTE: Not sure if this is best implementation?
                argument_value_list = [
                    argument_value
                    for argument_value in argument_value_list
                    if not any(
                        set(exclude_value).issubset(set(argument_value))
                        for exclude_value in exclude_value_list
                    )
                ]

            # conftest_logger.debug(f"Argument Name List: {argument_name_list}")
            # conftest_logger.debug(f"Argument Value List: {argument_value_list}")

            # Parametrize the test(s), only if test_data is available
            metafunc.parametrize(
                argnames=argument_name_list,
                argvalues=argument_value_list,
                ids=id_list,
            )


def pytest_make_parametrize_id(
    config: Config,
    val: object,
    argname: str,
) -> str | None:
    """Make Parametrize ID Hook

    Return a user friendly string representation of the given value that
    will be used by @pytest.mark.parametrize calls, or None if the hook
    doesn't know about the value.

    The parameter name is available as argname, if required.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook.

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

    This is useful when the condition for a marker requires objects that
    are expensive or impossible to obtain during collection time, which
    is required by normal boolean conditions.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in parent directories of the item are
        consulted.

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
    items: list[Item],
) -> None:
    """Collection Modify Items Hook

    Called after collection has been performed. May filter or re-order
    the items in-place.

    When items are deselected (filtered out from items), the hook
    pytest_deselected must be called explicitly with the deselected
    items to properly notify other plugins, e.g. with
    config.hook.pytest_deselected(deselected_items).

    conftest: Any conftest plugin can implement this hook.

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

    conftest: Any conftest plugin can implement this hook.

    :param session: The pytest session object
    :type session: pytest.Session
    """
    conftest_logger.info("pytest Collection Finish")
    conftest_logger.debug(f"Session: {session}")


###############################
# Test Running (runtest) Hook #
###############################


def pytest_runtestloop(session: Session) -> object | None:
    """Run Test Loop Hook

    Perform the main runtest loop (after collection finished).

    The default hook implementation performs the runtest protocol for
    all items collected in the session (session.items), unless the
    collection failed or the collectonly pytest option is set.

    If at any point pytest.exit() is called, the loop is terminated
    immediately.

    If at any point session.shouldfail or session.shouldstop are set,
    the loop is terminated after the runtest protocol for the current
    item is finished.

    Stops at first non-None result. The return value is not used, but
    only stops further processing.

    conftest: Any conftest file can implement this hook.

    :param session: The pytest session object
    :type session: pytest.Session

    :returns: The pytest runtestloop object
    :rtype: pytest.object | None
    """
    conftest_logger.info("pytest Run Test Loop")
    conftest_logger.debug(f"Session: {session}")


def pytest_runtest_protocol(
    item: Item,
    nextitem: Item | None,
) -> object | None:
    """Run Test Protocol Hook

    Perform the runtest protocol for a single test item.

    Stops at first non-None result. The return value is not used, but
    only stops further processing.

    conftest: Any conftest file can implement this hook.

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
    location: tuple[str, int | None, str],
) -> None:
    """Run Test Log Start Hook

    Called at the start of running the runtest protocol for a single
    item.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

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
    location: tuple[str, int | None, str],
) -> None:
    """Run Test Log Finish Hook

    Called at the end of running the runtest protocol for a single item.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

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

    The default implementation runs setup() on item and all of its
    parents (which haven't been setup yet). This includes obtaining the
    values of fixtures required by the item (which haven't been obtained
    yet).

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

    :param item: The item
    :type item: pytest.Item
    """
    conftest_logger.info("pytest Run Test Setup")
    conftest_logger.debug(f"Item: {item}")


def pytest_runtest_call(item: Item) -> None:
    """Run Test Call Hook

    Called to run the test for test item (the call phase).

    The default implementation calls item.runtest().

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item’s directory and its parent
        directories are consulted.

    :param item: The item
    :type item: pytest.Item
    """
    conftest_logger.info("pytest Run Test Call")
    conftest_logger.debug(f"Item: {item}")


def pytest_runtest_teardown(
    item: Item,
    nextitem: Item | None,
) -> None:
    """Run Test Teardown Hook

    Called to perform the teardown phase for a test item.

    The default implementation runs the finalizers and calls teardown()
    on item and all of its parents (which need to be torn down). This
    includes running the teardown phase of fixtures required by the item
    (if they go out of scope).

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: Item,
    call: CallInfo[None],
) -> TestReport | None:
    """Run Test Make Report

    Called to create a pytest TestReport for each of the setup, call
    and teardown runtest phases of a test item.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

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

    outcome: Result = yield
    result: TestReport = outcome.get_result()
    if result.when == "call":
        conftest_logger.debug(f"Item Name: {item.name}")
        conftest_logger.debug(f"Result Outcome: {result.outcome}")


def pytest_pyfunc_call(pyfuncitem: Function) -> None:
    """Pyfunc Call Hook

    Call underlying test function.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

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

    conftest: Any conftest file can implement this hook. For a given
        collector, only conftest files in the collector's directory and
        its parent directories are consulted.

    :param collector: The collector
    :type collector: pytest.Collector
    """
    conftest_logger.info("pytest Collect Start")
    conftest_logger.debug(f"Collector: {collector}")


def pytest_make_collect_report(
    collector: Collector,
) -> CollectReport | None:
    """Make Collect Report Hook

    Perform collector.collect() and return a CollectReport.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        collector, only conftest files in the collector's directory and
        its parent directories are consulted.

    :param collector: The collector
    :type collector: pytest.Collector

    :returns: The pytest CollectReport object
    :rtype: pytest.CollectReport | None
    """
    conftest_logger.info("pytest Make Collect Report")
    conftest_logger.debug(f"Collector: {collector}")


def pytest_itemcollected(item: Item) -> None:
    """Item Collected Hook

    We just collected a test item.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

    :param item: The item
    :type item: pytest.Item
    """
    conftest_logger.info("pytest Item Collected")
    conftest_logger.debug(f"Item: {item}")


def pytest_collectreport(report: CollectReport) -> None:
    """Collect Report Hook

    Collector finished collecting.

    conftest: Any conftest file can implement this hook. For a given
        collector, only conftest files in the collector's directory and
        its parent directories are consulted.

    :param report: The collect report
    :type report: pytest.CollectReport
    """
    conftest_logger.info("pytest Collect Report")
    conftest_logger.debug(f"Report: {report}")


def pytest_deselected(items: Sequence[Item]) -> None:
    """Deselected Hook

    Called for deselected test items, e.g. by keyword.

    May be called multiple times.

    conftest: Any conftest file can implement this hook.

    :param items: The items
    :type items: Sequence[pytest.Item]
    """
    conftest_logger.info("pytest Deselected")
    conftest_logger.debug(f"Items: {items}")


def pytest_report_header(
    config: Config,
    start_path: Path,
    # startdir: LEGACY_PATH
) -> str | list[str]:
    """Report Header Hook

    Return a string or list of strings to be displayed as header info
    for terminal reporting.

    conftest: This hook is only called for initial conftest(s).

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param start_path: The starting directory
    :type start_path: Path
    :param startdir: The starting directory (deprecated)
    :type startdir: LEGACY_PATH

    :returns: The header information
    :rtype: str | list[str]
    """
    conftest_logger.info("pytest Report Header")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Start Path: {start_path}")


def pytest_report_collectionfinish(
    config: Config,
    start_path: Path,
    # startdir: LEGACY_PATH,
    items: Sequence[Item],
) -> str | list[str]:
    """Report Collection Finish Hook

    Return a string or list of strings to be displayed after collection
    has finished successfully.

    These strings will be displayed after the standard “collected X
    items” message.

    conftest: Any conftest plugin can implement this hook.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param start_path: The starting directory
    :type start_path: Path
    :param startdir: The starting directory (deprecated)
    :type startdir: LEGACY_PATH
    :param items: List of pytest items that are going to be executed;
        this list should not be modified
    :type items: Sequence[pytest.Item]

    :returns: The collection finish information
    :rtype: str | list[str]
    """
    conftest_logger.info("pytest Report Collection Finish")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Start Path: {start_path}")
    conftest_logger.debug(f"Items: {items}")


def pytest_report_teststatus(
    report: CollectReport | TestReport,
    config: Config,
) -> TestShortLogReport | tuple[str, str, str | tuple[str, Mapping[str, bool]]]:
    """Report Test Status Hook

    Return result-category, shortletter and verbose word for status
    reporting.

    The result-category is a category in which to count the result, for
    example “passed”, “skipped”, “error” or the empty string.

    The shortletter is shown as testing progresses, for example “.”,
    “s”, “E” or the empty string.

    The verbose word is shown as testing progresses in verbose mode, for
    example “PASSED”, “SKIPPED”, “ERROR” or the empty string.

    pytest may style these implicitly according to the report outcome.
    To provide explicit styling, return a tuple for the verbose word,
    for example "rerun", "R", ("RERUN", {"yellow": True}).

    Stops at first non-None result.

    conftest: Any conftest plugin can implement this hook.

    :param report: The report object whose status is to be returned
    :type report: pytest.CollectReport | pytest.TestReport
    :param config: The pytest configuration object
    :type config: pytest.Config

    :returns: The test status
    :rtype: pytest.TestShortLogReport | tuple[str, str, str | tuple[str, Mapping[str, bool]]]
    """
    conftest_logger.info("pytest Report Test Status")
    conftest_logger.debug(f"Report: {report}")
    conftest_logger.debug(f"Configuration: {config}")


def pytest_report_to_serializable(
    config: Config,
    report: CollectReport | TestReport,
) -> dict[str, Any] | None:
    """Report to Serializable Hook

    Serialize the given report object into a data structure suitable for
    sending over the wire, e.g. converted to JSON.

    conftest: Any conftest file can implement this hook. The exact
        details may depend on the plugin which calls the hook.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param report: The report
    :type report: pytest.CollectReport | pytest.TestReport

    :returns: The serializable object
    :rtype: dict[str, Any] | None
    """
    conftest_logger.info("pytest Report to Serializable")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Report: {report}")


def pytest_report_from_serializable(
    config: Config,
    data: dict[str, Any],
) -> CollectReport | TestReport | None:
    """Report from Serializable Hook

    Restore a report object previously serialized with
    pytest_report_to_serializable.

    conftest: Any conftest file can implement this hook. The exact
        details may depend on the plugin which calls the hook.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param data: The serializable data
    :type data: dict[str, Any]

    :returns: The report object
    :rtype: pytest.CollectReport | pytest.TestReport | None
    """
    conftest_logger.info("pytest Report from Serializable")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Data: {data}")


def pytest_terminal_summary(
    terminalreporter: TerminalReporter,
    exitstatus: ExitCode,
    config: Config,
) -> None:
    """Terminal Summary Hook

    Add a section to terminal summary reporting.

    conftest: Any conftest plugin can implement this hook.

    :param terminalreporter: The internal terminal reporter object
    :type terminalreporter: _pytest.terminal.TerminalReporter
    :param exitstatus: The exit status
    :type exitstatus: pytest.ExitCode
    :param config: The pytest configuration object
    :type config: pytest.Config
    """
    conftest_logger.info("pytest Terminal Summary")
    conftest_logger.debug(f"Terminal Reporter: {terminalreporter}")
    conftest_logger.debug(f"Exit Status: {exitstatus}")
    conftest_logger.debug(f"Configuration: {config}")

    status_passed = len(terminalreporter.stats.get("passed", []))
    status_failed = len(terminalreporter.stats.get("failed", []))
    conftest_logger.debug(f"Terminal Report Status Passed: {status_passed}")
    conftest_logger.debug(f"Terminal Report Status Failed: {status_failed}")


def pytest_fixture_setup(
    fixturedef: FixtureDef[Any],
    request: SubRequest,
) -> object | None:
    """Fixture Setup Hook

    Perform fixture setup execution.

    Stops at first non-None result.

    conftest: Any conftest file can implement this hook. For a given
        fixture, only conftest files in the fixture scope’s directory
        and its parent directories are consulted.

    :param fixturedef: The fixture definition object
    :type fixturedef: pytest.FixtureDef
    :param request: The fixture request object
    :type request: pytest.SubRequest

    :returns: The return value of the call to the fixture function
    :rtype: object | None
    """
    conftest_logger.info("pytest Fixture Setup")
    conftest_logger.debug(f"Fixture Definition: {fixturedef}")
    conftest_logger.debug(f"Request: {request}")


def pytest_fixture_post_finalizer(
    fixturedef: FixtureDef[Any],
    request: SubRequest,
) -> None:
    """Fixture Post Finalizer Hook

    Called after fixture teardown, but before the cache is cleared, so
    the fixture result fixturedef.cached_result is still available (not
    None).

    conftest: Any conftest file can implement this hook. For a given
        fixture, only conftest files in the fixture scope's directory
        and its parent directories are consulted.

    :param fixturedef: The fixture definition object
    :type fixturedef: pytest.FixtureDef
    :param request: The fixture request object
    :type request: pytest.SubRequest
    """
    conftest_logger.info("pytest Fixture Post Finalizer")
    conftest_logger.debug(f"Fixture Definition: {fixturedef}")
    conftest_logger.debug(f"Request: {request}")


def pytest_warning_recorded(
    warning_message: warnings.WarningMessage,
    when: Literal["config", "collect", "runtest"],
    nodeid: str,
    location: tuple[str, int, str] | None,
) -> None:
    """Warning Recorded Hook

    Process a warning captured by the internal pytest warnings plugin.

    conftest: Any conftest file can implement this hook. If the warning
        is specific to a particular node, only conftest files in parent
        directories of the node are consulted.

    :param warning_message: The captured warning
    :type warning_message: warnings.WarningMessage
    :param when: Indicates when the warning was captured
    :type when: Literal["config", "collect", "runtest"]
    :param nodeid: Full ID of the item
    :type nodeid: str
    :param location: When available, holds information about the
        execution context of the captured warning (filename, linenumber,
        function)
    :type location: tuple[str, int, str] | None
    """
    conftest_logger.info("pytest Warning Recorded")
    conftest_logger.debug(f"Warning Message: {warning_message}")
    conftest_logger.debug(f"When: {when}")
    conftest_logger.debug(f"Node IDentifier: {nodeid}")
    conftest_logger.debug(f"Location: {location}")


def pytest_runtest_logreport(report: TestReport) -> None:
    """Run Test Log Report Hook

    Process the TestReport produced for each of the setup, call and
    teardown runtest phases of an item.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

    :param report: The test report
    :type report: pytest.TestReport
    """
    conftest_logger.info("pytest Run Test Log Report")
    conftest_logger.debug(f"Report: {report}")


def pytest_assertrepr_compare(
    config: Config,
    op: str,
    left: object,
    right: object,
) -> list[str] | None:
    """Assert Representation Compare Hook

    Return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list of
    strings. The strings will be joined by newlines but any newlines in
    a string will be escaped. Note that all but the first line will be
    indented slightly, the intention is for the first line to be a
    summary.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item's directory and its parent
        directories are consulted.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param op: The operator, e.g. "==", "!=", "not in".
    :type op: str
    :param left: The left operand
    :type left: object
    :param right: The right operand
    :type right: object

    :returns: The explanation for the comparison
    :rtype: list[str] | None
    """
    conftest_logger.info("pytest Assert Representation Compare")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Operator: {op}")
    conftest_logger.debug(f"Left Operand: {left}")
    conftest_logger.debug(f"Right Operand: {right}")


def pytest_assertion_pass(
    item: Item,
    lineno: int,
    orig: str,
    expl: str,
) -> None:
    """Assertion Pass Hook

    Called whenever an assertion passes.

    Use this hook to do some processing after a passing assertion. The
    original assertion information is available in the orig string and
    the pytest introspected assertion information is available in the
    expl string.

    This hook must be explicitly enabled by the
    enable_assertion_pass_hook ini-file option.

    You need to clean the .pyc files in your project directory and
    interpreter libraries when enabling this option, as assertions will
    require to be re-written.

    conftest: Any conftest file can implement this hook. For a given
        item, only conftest files in the item’s directory and its parent
        directories are consulted.

    :param item: The pytest item object of current test
    :type item: pytest.Item
    :param lineno: Line number of the assert statement
    :type lineno: int
    :param orig: String with the original assertion
    :type orig: str
    :param expl: String with the assert explanation
    :type expl: str
    """
    conftest_logger.info("pytest Assertion Pass")
    conftest_logger.debug(f"Item: {item}")
    conftest_logger.debug(f"Line Number: {lineno}")
    conftest_logger.debug(f"Original Assertion: {orig}")
    conftest_logger.debug(f"Explanation: {expl}")


##############################
# Debugging/Interaction Hook #
##############################


def pytest_internalerror(
    excrepr: ExceptionRepr,
    excinfo: ExceptionInfo[BaseException],
) -> bool | None:
    """Internal Error Hook

    Called for internal errors.

    Return True to suppress the fallback handling of printing an
    INTERNALERROR message directly to sys.stderr.

    conftest: Any conftest plugin can implement this hook.

    :param excrepr: The exception representation object
    :type excrepr: pytest.ExceptionRepr
    :param excinfo: The exception information
    :type excinfo: pytest.ExceptionInfo[BaseException]

    :returns: Whether to suppress the fallback handling
    :rtype: bool | None
    """
    conftest_logger.info("pytest Internal Error")
    conftest_logger.debug(f"Exception Representation: {excrepr}")
    conftest_logger.debug(f"Exception Information: {excinfo}")


def pytest_keyboard_interrupt(
    excinfo: ExceptionInfo[KeyboardInterrupt | Exit],
) -> None:
    """Keyboard Interrupt Hook

    Called for keyboard interrupt.

    conftest: Any conftest plugin can implement this hook.

    :param excinfo: The exception information
    :type excinfo: pytest.ExceptionInfo[KeyboardInterrupt | pytest.Exit]
    """
    conftest_logger.info("pytest Keyboard Interrupt")
    conftest_logger.debug(f"Exception Information: {excinfo}")


def pytest_exception_interact(
    node: Item | Collector,
    call: CallInfo[Any],
    report: CollectReport | TestReport,
) -> None:
    """Exception Interaction Hook

    Called when an exception was raised which can potentially be
    interactively handled.

    May be called during collection, in which case report is a
    CollectReport.

    May be called during runtest of an item, in which case report is a
    TestReport.

    This hook is not called if the exception that was raised is an
    internal exception like skip.Exception.

    conftest: Any conftest file can implement this hook. For a given
        node, only conftest files in parent directories of the node are
        consulted.

    :param node: The item or collector
    :type node: pytest.Item | pytest.Collector
    :param call: The call information (contains the exception)
    :type call: pytest.CallInfo[Any]
    :param report: The collection or test report
    :type report: pytest.CollectReport | pytest.TestReport
    """
    conftest_logger.info("pytest Exception Interaction")
    conftest_logger.debug(f"Node: {node}")
    conftest_logger.debug(f"Call: {call}")
    conftest_logger.debug(f"Report: {report}")


def pytest_enter_pdb(
    config: Config,
    pdb: pdb.Pdb,
) -> None:
    """Enter Python Debugger (PDB) Hook

    Called upon pdb.set_trace().

    Can be used by plugins to take special action just before the python
    debugger enters interactive mode.

    conftest: Any conftest plugin can implement this hook.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param pdb: The pdb instance
    :type pdb: pdb.Pdb
    """
    conftest_logger.info("pytest Enter Python Debugger (PDB)")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Python Debugger: {pdb}")


def pytest_leave_pdb(
    config: Config,
    pdb: pdb.Pdb,
) -> None:
    """Leave Python Debugger (PDB) Hook

    Called when leaving pdb (e.g. with continue after pdb.set_trace()).

    Can be used by plugins to take special action just after the python
    debugger leaves interactive mode.

    conftest: Any conftest plugin can implement this hook.

    :param config: The pytest configuration object
    :type config: pytest.Config
    :param pdb: The pdb instance
    :type pdb: pdb.Pdb
    """
    conftest_logger.info("pytest Leave Python Debugger (PDB)")
    conftest_logger.debug(f"Configuration: {config}")
    conftest_logger.debug(f"Python Debugger: {pdb}")
