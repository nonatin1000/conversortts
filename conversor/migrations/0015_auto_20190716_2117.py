# Generated by Django 2.2.3 on 2019-07-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0014_auto_20190716_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='nome',
        ),
        migrations.AddField(
            model_name='audio',
            name='nome_do_arquivo',
            field=models.CharField(default='', help_text='Não utilize acento no nome do arquivo.', max_length=255),
            preserve_default=False,
        ),
    ]