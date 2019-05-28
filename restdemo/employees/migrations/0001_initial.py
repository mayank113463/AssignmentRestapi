# Generated by Django 2.2.1 on 2019-05-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(max_length=30)),
            ],
        ),
    ]
