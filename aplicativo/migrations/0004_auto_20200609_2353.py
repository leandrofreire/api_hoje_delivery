# Generated by Django 2.2.12 on 2020-06-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0003_loja'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loja',
            options={'ordering': ['nome'], 'verbose_name': 'Loja', 'verbose_name_plural': 'Lojas'},
        ),
        migrations.AddField(
            model_name='loja',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='aplicativo/imagens', verbose_name='Capa'),
        ),
    ]
