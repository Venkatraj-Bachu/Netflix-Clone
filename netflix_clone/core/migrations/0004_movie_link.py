# Generated by Django 5.0.1 on 2024-02-09 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_topratedmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.TextField(default=''),
        ),
    ]