# Generated by Django 4.2.11 on 2024-09-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_alter_selectfavorite_cloth_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_model',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
