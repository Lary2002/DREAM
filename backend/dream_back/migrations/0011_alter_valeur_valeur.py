# Generated by Django 4.1 on 2022-09-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_back', '0010_alter_utilisateur_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valeur',
            name='valeur',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]