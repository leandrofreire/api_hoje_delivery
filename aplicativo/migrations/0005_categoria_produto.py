# Generated by Django 2.2.12 on 2020-06-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0004_auto_20200609_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Categoria_produto',
                'verbose_name_plural': 'Categoria_produtos',
            },
        ),
    ]