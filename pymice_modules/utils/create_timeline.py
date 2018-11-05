#!/usr/bin/env python3
# -*- coding: utf-8 -*

#    This file is part of pymice-modules.
#    Copyright (C) 2018  Emir Turkes
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
#    Emir Turkes can be contacted at eturkes@bu.edu

"""Creates timeline INI file."""


import configparser as cp
import os


def create_timeline(start, end, tzinfo, proj_path):
    """Creates timeline INI file."""
    conf = cp.ConfigParser()
    conf.add_section("Phase 1")
    conf["Phase 1"]["start"] = start
    conf["Phase 1"]["end"] = end
    conf["Phase 1"]["tzinfo"] = tzinfo
    with open(
        os.path.join(proj_path, "pipeline", "timeline", "timeline.ini"), "w"
    ) as file:
        conf.write(file)
