# Generated by Django 4.1 on 2022-09-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dream_back', '0012_remove_valeur_idtypemesure'),
    ]

    operations = [
        migrations.AddField(
            model_name='valeur',
            name='idTypeMesure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dream_back.typemesure'),
        ),
    ]