# Generated by Django 4.1 on 2022-09-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_back', '0002_utilisateur_pays'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='photo',
            field=models.FileField(default='', upload_to='photos'),
            preserve_default=False,
        ),
    ]