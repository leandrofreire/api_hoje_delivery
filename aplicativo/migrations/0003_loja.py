# Generated by Django 2.2.12 on 2020-06-09 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativo', '0002_auto_20200609_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=300)),
                ('categoria_loja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lojas', to='aplicativo.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]