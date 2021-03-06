# Generated by Django 3.1 on 2020-08-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprador', models.CharField(blank=True, max_length=50, null=True)),
                ('descricao', models.CharField(blank=True, max_length=50, null=True)),
                ('precounitario', models.FloatField(blank=True, default=0.0, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=50, null=True)),
                ('fornecedor', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
