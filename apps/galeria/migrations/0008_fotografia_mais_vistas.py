# Generated by Django 5.0.3 on 2024-03-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='mais_vistas',
            field=models.IntegerField(default=0),
        ),
    ]
