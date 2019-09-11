# Generated by Django 2.2.3 on 2019-07-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversor', '0009_auto_20190707_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='idioma_do_texto',
            field=models.CharField(choices=[('de', 'Alemão'), ('ca', 'Catalão'), ('zn-cn', 'Chinês'), ('ko', 'Coreano'), ('es-es', 'Espanhol'), ('fr-fr', 'Francês'), ('en-ca', 'Inglês (Canadá)'), ('en-us', 'Inglês (EUA)'), ('en-uk', 'Inglês (Reino Unido)'), ('ja', 'Japonês'), ('la', 'Latim'), ('pt-br', 'Português (BR)'), ('pt-pt', 'Português (PT)'), ('ru', 'Russo')], default=('pt-br', 'Português'), max_length=15),
        ),
    ]