# Generated by Django 2.2.3 on 2019-07-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0004_audio_idioma_do_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='idioma_do_texto',
            field=models.CharField(choices=[('pt-br', 'Português'), ('en-us', 'English')], default=('pt-br', 'Português'), max_length=15),
        ),
    ]