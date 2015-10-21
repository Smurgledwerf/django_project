from django.db import models


class Platform(models.Model):
    """

    """
    platform_name = models.CharField(max_length=100)
    release_date = models.DateTimeField('date released')

    def __str__(self):
        return self.platform_name


class Game(models.Model):
    """

    """
    platform = models.ForeignKey(Platform)
    game_name = models.CharField(max_length=200)
    hours_played = models.IntegerField(default=0)

    def __str__(self):
        return self.game_name
