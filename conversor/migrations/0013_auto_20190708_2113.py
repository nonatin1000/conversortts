# Generated by Django 2.2.3 on 2019-07-09 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0012_auto_20190708_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='idioma_do_texto',
            new_name='idioma',
        ),
    ]