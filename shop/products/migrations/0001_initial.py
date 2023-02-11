# Generated by Django 4.0.1 on 2023-02-10 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Тип гри',
                'verbose_name_plural': 'Тип гри',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Видання',
                'verbose_name_plural': 'Видання',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='../media/picture_game/png-transparent-yahtzee-starcraft-the-board-game-dixit-games-game-text-logo_ps91FUD.png', upload_to='picture_game/')),
                ('slug', models.SlugField()),
                ('language', models.CharField(choices=[('ukr', 'Українська'), ('rus', 'Російська'), ('eng', 'Англійська')], default='ukr', max_length=50)),
                ('time', models.CharField(choices=[('small', 'до 20 хв'), ('medium', '20-60 хв'), ('long', 'більше 60 хв')], default='small', max_length=20)),
                ('max_players', models.PositiveSmallIntegerField(default=2)),
                ('min_players', models.PositiveSmallIntegerField(default=1)),
                ('min_age_player', models.PositiveSmallIntegerField(default=3)),
                ('publishing_house', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='products.publishinghouse')),
                ('type', models.ManyToManyField(to='products.GameType')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]