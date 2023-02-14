from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse

AUTH_USER_MODEL = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='picture_game/',
        default='/media/picture_game/png-transparent-yahtzee-starcraft-the-board-game-dixit-games-game-text-logo.png',
    )
    slug = models.SlugField(max_length=50)

    UKRAINE = "ukr"
    RUSSIAN = "rus"
    ENGLISH = "eng"

    SELECT_LANGUAGE = (
        (UKRAINE, "Українська"),
        (RUSSIAN, "Російська"),
        (ENGLISH, "Англійська"),
    )

    language = models.CharField(max_length=50, choices=SELECT_LANGUAGE, default=UKRAINE)

    SMALL = 'small'
    MEDIUM = 'medium'
    LONG = 'long'

    GAME_TIME = (
        (SMALL, 'до 20 хв'),
        (MEDIUM, '20-60 хв'),
        (LONG, 'більше 60 хв'),
    )

    time = models.CharField(max_length=20, choices=GAME_TIME, default=SMALL)

    max_players = models.PositiveSmallIntegerField(default=2)
    min_players = models.PositiveSmallIntegerField(default=1)

    min_age_player = models.PositiveSmallIntegerField(default=3)

    publishing_house = models.ForeignKey(
        'products.PublishingHouse',
        on_delete=models.CASCADE,
        blank=True,
        related_name="games"
    )

    type = models.ManyToManyField(
        'products.GameType'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('products:product-view', args=[str(self.slug)])

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class PublishingHouseQuerySet(models.QuerySet):

    def annotate_games_count(self): # повертає QuarySet
        return self.annotate(games_count=models.Count('games'))

    def aggregate_games_count(self): # повертає якісь данні
        return self.aggregate(games_count=models.Count('games'))


class PublishingHouse(models.Model):
    name = models.CharField(max_length=150)

    slug = models.SlugField(max_length=50)

    owner = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    objects = PublishingHouseQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.slug)])

    class Meta:
        verbose_name = "Видання"
        verbose_name_plural = "Видання"


class GameType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип гри"
        verbose_name_plural = "Тип гри"
