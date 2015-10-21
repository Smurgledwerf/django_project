from django.db import models


class Platform(models.Model):
    """
    Object representing a gaming platform.
    """
    platform_name = models.CharField(max_length=100)
    family = models.CharField(max_length=100, default='')
    generation = models.IntegerField(default=0)
    release_date = models.DateTimeField('date released')

    def __str__(self):
        return self.platform_name

    def is_current_generation(self):
        """
        Check if this platform is the current generation for it's family.
        """
        max_generation = 0
        for platform in Platform.objects.all():
            if platform.family == self.family:
                max_generation = max(platform.generation, self.generation)

        return max_generation == self.generation
    is_current_generation.boolean = True
    is_current_generation.short_description = 'Current Generation?'


class Game(models.Model):
    """
    Object representing a game.
    """
    platform = models.ForeignKey(Platform)
    game_name = models.CharField(max_length=200)
    hours_played = models.IntegerField(default=0)

    def __str__(self):
        return self.game_name
