from django.db import models
from django.core.exceptions import ValidationError


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

    def clean(self):
        """
        Check some fields to make sure they are valid.
        """
        if self.generation < 1:
            raise ValidationError("Generation must be greater than 0.")

        for platform in Platform.objects.filter(family=self.family):
            if platform == self:
                continue
            if platform.generation == self.generation:
                raise ValidationError("Cannot have duplicate generations in family.")

        super(Platform, self).clean()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Check some fields to make sure they are valid.
        """
        if self.generation < 1:
            raise ValidationError("Generation must be greater than 0.")

        for platform in Platform.objects.filter(family=self.family):
            if platform == self:
                continue
            if platform.generation == self.generation:
                raise ValidationError("Cannot have duplicate generations in family.")

        super(Platform, self).save(force_insert, force_update, using, update_fields)

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

    def clean(self):
        """
        Check some fields to make sure they are valid.
        """
        if self.hours_played < 0:
            raise ValidationError("Hours played cannot be negative.")

        zelda_oot = Game.objects.filter(game_name='The Legend of Zelda: Ocarina of Time')
        if zelda_oot:
            zelda_oot = zelda_oot[0]
            if self != zelda_oot and self.hours_played > zelda_oot.hours_played:
                raise ValidationError("Liar.")

        super(Game, self).clean()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Check some fields to make sure they are valid.
        """
        if self.hours_played < 0:
            raise ValidationError("Hours played cannot be negative.")

        zelda_oot = Game.objects.filter(game_name='The Legend of Zelda: Ocarina of Time')
        if zelda_oot:
            zelda_oot = zelda_oot[0]
            if self != zelda_oot and self.hours_played > zelda_oot.hours_played:
                raise ValidationError("Liar.")

        super(Game, self).save(force_insert, force_update, using, update_fields)
