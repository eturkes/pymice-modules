#!/usr/bin/env python3
# -*- coding: utf-8 -*

#    This file is part of pymice-modules.
#    Copyright (C) 2018-2019  Emir Turkes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Emir Turkes can be contacted at emir.turkes@eturkes.com

""" Imports all modules in path into the env."""


import os
import re
import sys


def import_all(path, env):
    """ Imports all modules in path into the env."""
    __module_file_regexp = "(.+)\.py(c?)$"

    def __get_module_names_in_dir(path):
        """ Returns a set of all module names within path."""
        result = set()
        # Looks for all python files in the dir (not recursively) and adds their name.
        for entry in os.listdir(path):
            if os.path.isfile(os.path.join(path, entry)):
                regexp_result = re.search(__module_file_regexp, entry)
                if regexp_result:
                    result.add(regexp_result.groups()[0])
        return result

    sys.path.append(path)  # Adds provided dir to list that can be imported from.
    for module_name in sorted(__get_module_names_in_dir(path)):
        env[module_name] = __import__(module_name)
