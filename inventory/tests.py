from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Platform, Game


def create_platform(platform_name, family='', generation=1, release_date=None):
    if not release_date:
        release_date = timezone.now()
    return Platform.objects.create(platform_name=platform_name, family=family,
                                   generation=generation, release_date=release_date)


def create_game(game_name, hours_played=0, platform=None):
    if not platform:
        platform = create_platform('Platform')
    return Game.objects.create(game_name=game_name, hours_played=hours_played, platform=platform)


class PlatformMethodTests(TestCase):
    def test_platform_with_negative_generation(self):
        """
        Makes sure platforms with negative generation raises ValidationError.
        """
        self.assertRaises(ValidationError, lambda: create_platform('Platform', generation=-1))

    def test_platform_with_zero_generation(self):
        """
        Makes sure platforms with zero generation raises ValidationError.
        """
        self.assertRaises(ValidationError, lambda: create_platform('Platform', generation=0))

    def test_platform_with_duplicate_generation(self):
        """
        Makes sure platforms with duplicate generation raises ValidationError.
        """
        create_platform('Platform', 'Console', 1)
        self.assertRaises(ValidationError, lambda: create_platform('Platform 2', 'Console', 1))

    def test_is_current_generation_with_no_platforms(self):
        """
        Should be current if there are no others in it's family.
        """
        lone_platform = create_platform('Cool Platform')
        self.assertEqual(lone_platform.is_current_generation(), True)

    def test_is_current_generation_with_older_platform(self):
        """
        Higher generation should be current.
        """
        old_platform = create_platform('Cool Platform', 'Console', 1)
        new_platform = create_platform('Cool Platform 2', 'Console', 2)
        self.assertEqual(new_platform.is_current_generation(), True)

    def test_is_current_generation_with_newer_platform(self):
        """
        Lower generation should not be current.
        """
        old_platform = create_platform('Cool Platform', 'Console', 1)
        new_platform = create_platform('Cool Platform 2', 'Console', 2)
        self.assertEqual(old_platform.is_current_generation(), False)

    def test_is_current_generation_with_other_family(self):
        """
        Gen 1 should be current despite higher generation in other family.
        """
        first_platform = create_platform('Cool Platform', 'Console', 9)
        second_platform = create_platform('Other Platform', 'Handheld', 1)
        self.assertEqual(second_platform.is_current_generation(), True)


class GameMethodTests(TestCase):
    def test_game_with_negative_hours_played(self):
        """
        Makes sure the hours played is positive.
        """
        self.assertRaises(ValidationError, lambda: create_game('Cool Game', hours_played=-1))

    def test_hours_played_not_higher_than_zelda_oot(self):
        """
        Makes sure The Legend of Zelda: Ocarina of Time has the highest hours played.
        """
        zelda_oot = create_game('The Legend of Zelda: Ocarina of Time', hours_played=9999)
        self.assertRaises(ValidationError, lambda: create_game('Not as Cool Game', hours_played=10000))
