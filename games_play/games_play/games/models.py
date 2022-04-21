from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    age = models.IntegerField(validators=(MinValueValidator(12),))
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.URLField(blank=True)


class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CHOICES = (
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (PUZZLE, 'Puzzle'),
        (STRATEGY, 'Strategy'),
        (SPORTS, 'Sports'),
        (BOARD_CARD_GAME, 'Board/Card Game'),
        (OTHER, 'Other'),
    )
    title = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=15, choices=CHOICES)
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(validators=(MinValueValidator(1),))
    image_url = models.URLField()
    summary = models.TextField(blank=True)