#!/usr/bin/env python3
# ##############################################################################
#  Author: echel0n <echel0n@sickrage.ca>
#  URL: https://sickrage.ca/
#  Git: https://git.sickrage.ca/SiCKRAGE/sickrage.git
#  -
#  This file is part of SiCKRAGE.
#  -
#  SiCKRAGE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  -
#  SiCKRAGE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  -
#  You should have received a copy of the GNU General Public License
#  along with SiCKRAGE.  If not, see <http://www.gnu.org/licenses/>.
# ##############################################################################


import unittest

import sickrage
import tests
from sickrage.core.tv.episode import TVEpisode
from sickrage.core.tv.show import TVShow


class TVShowTests(tests.SiCKRAGETestDBCase):
    def test_init_indexer_id(self):
        show = TVShow(0o001, 1)
        self.assertEqual(show.series_id, 0o001)

    def test_change_indexer_id(self):
        show = TVShow(0o001, 1)
        show.name = "show name"
        show.network = "cbs"
        show.genre = "crime"
        show.runtime = 40
        show.status = "Ended"
        show.default_ep_status = "5"
        show.airs = "monday"
        show.startyear = 1987
        show.series_id = 0o002
        self.assertEqual(show.series_id, 0o002)

    def test_set_name(self):
        show = TVShow(0o001, 1)
        show.name = "newName"
        self.assertEqual(show.name, "newName")


class TVEpisodeTests(tests.SiCKRAGETestDBCase):
    def test_init_empty_db(self):
        show = TVShow(0o001, 1)
        ep = TVEpisode(show, 1, 1, 1)
        ep.name = "asdasdasdajkaj"
        ep.save()
        self.assertEqual(ep.name, "asdasdasdajkaj")


class TVTests(tests.SiCKRAGETestDBCase):
    def test_getEpisode(self):
        show = TVShow(0o001, 1)
        show.name = "show name"
        show.network = "cbs"
        show.genre = "crime"
        show.runtime = 40
        show.status = "Ended"
        show.default_ep_status = "5"
        show.airs = "monday"
        show.startyear = 1987
        sickrage.app.showlist = [show]


if __name__ == '__main__':
    print("==================")
    print("STARTING - TV TESTS")
    print("==================")
    print("######################################################################")
    unittest.main()
