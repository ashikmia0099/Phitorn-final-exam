# Generated by Django 4.2.11 on 2024-09-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0004_card_model_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card_model',
            name='rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
