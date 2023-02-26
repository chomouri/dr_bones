"""Configuration Script for Discord Bot"""
__lver__ = '1.0.1'

# Built-in Imports
from configparser import ConfigParser
from datetime import datetime
import os
from typing import Any, Dict

def config(filename: str = './conf.ini', section: str = 'general'
    ) -> Dict[str, str]:
    """Use conf.ini section to build dictionary of parameters.

    Parameters
    ----------
    filename : str, optional (default: './conf.ini')
        Path
    section : str, optional (default: 'general')
        The section of `filename` to use for parameter dictionary.

    Raises
    ------
    Exception
        `filename` not found.
        `section` not found.

    Returns
    -------
    dict
        [`filename` `section`]{**kwargs}
    """

    parser = ConfigParser()
    parser.read(filename)
    if not os.path.isfile(filename):
        path = os.getcwd()
        raise Exception('{0} not found in {1}'.format(filename, path))
    if parser.has_section(section):
        params = dict(parser.items(section))
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return params
