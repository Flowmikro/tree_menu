# Generated by Django 4.2.6 on 2023-10-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumodel',
            options={'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='name',
            field=models.CharField(help_text='Максимум 100 символов', max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='named_url',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
    ]
