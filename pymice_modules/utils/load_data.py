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

"""Loads the data and checks its validity."""


import configparser as cp
import os

import pymice as pm


def load_data(*args, **kwargs):
    """Loads the data and checks its validity."""
    # Merge the data.
    loaders = [pm.Loader(filename) for filename in args[0]]
    data = pm.Merger(*loaders)
    for mouse in sorted(data.getGroup()):
        print(mouse)

    # Update timeline.ini
    conf = cp.ConfigParser()
    conf.read("timeline/timeline.ini")
    conf["Phase 1"]["start"] = kwargs["start"]
    conf["Phase 1"]["end"] = kwargs["end"]
    with open(os.path.join("timeline/timeline.ini"), "w") as file:
        conf.write(file)

    # Read in period of analysis from timeline.ini.
    timeline = pm.Timeline("timeline/timeline.ini")
    start, end = timeline.getTimeBounds("Phase 1")

    # Check for any problems (indicated in the log) during the period of interest.
    data_validator = pm.DataValidator(pm.PresenceLogAnalyzer())
    validator_report = data_validator(data)
    no_presence_problems = pm.FailureInspector("Presence")
    if no_presence_problems(validator_report, (start, end)):
        pass
    else:
        print("Possible transponder problems")

    return data, start, end
