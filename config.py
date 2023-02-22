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

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    if not os.path.isfile(filename):
        path = os.getcwd()
        raise Exception('{0} not found in {1}'.format(filename, path))

    # get section, default to general
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
