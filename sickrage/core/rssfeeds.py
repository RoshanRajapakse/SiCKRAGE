# Author: echel0n <echel0n@sickrage.ca>
# URL: https://git.sickrage.ca/SiCKRAGE/sickrage/
#
# This file is part of SickRage.
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import random

import feedparser
import sickrage
from feedparser import FeedParserDict
from sickrage.core.webclient import USER_AGENTS


def getFeed(url, params=None, request_headers=None, handlers=None):
    try:
        data = sickrage.srCore.srWebSession.get(url, params=params).text

        return feedparser.parse(
            data,
            agent=random.choice(USER_AGENTS),
            etag=False,
            modified=False,
            request_headers=request_headers,
            handlers=handlers
        )
    except Exception as e:
        return FeedParserDict()
