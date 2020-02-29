"""A python app to (automatically) tag comic archives"""

# Copyright 2012-2014 Anthony Beville

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import signal
import traceback
import platform

from .settings import ComicTaggerSettings
# Need to load setting before anything else
SETTINGS = ComicTaggerSettings()

from . import utils
from . import cli
from .options import Options
from .comicvinetalker import ComicVineTalker

def ctmain():
    opts = Options()
    opts.parseCmdLineArgs()

    # manage the CV API key
    if opts.cv_api_key:
        if opts.cv_api_key != SETTINGS.cv_api_key:
            SETTINGS.cv_api_key = opts.cv_api_key
            SETTINGS.save()
    if opts.only_set_key:
        print("Key set")
        return

    ComicVineTalker.api_key = SETTINGS.cv_api_key

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    opts.no_gui = True

    cli.cli_mode(opts, SETTINGS)
