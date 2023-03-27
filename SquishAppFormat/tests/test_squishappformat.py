import unittest
from typing import List, Dict

from squishappformat import __version__
from squishappformat.SquishAppFormatDemo import SquishAppManager


class TestBasic(unittest.TestCase):
    def test_version(self):
        assert __version__ == '1.0.0'

    def test_simple(self):
        manager = SquishAppManager('./teamAlphaDemo')
        manager.load_squish_app_directory('git@github.com:HenryFBP/TeamAlpha-SquishAppDirectory.git')

        allTeamMembers: List[Dict]
        allTeamMembers = manager.squish_applications.get_all_team_members()

        self.assertNotEqual(allTeamMembers, [])
        self.assertEqual(len(allTeamMembers), 4)
