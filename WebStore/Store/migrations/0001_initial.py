# Generated by Django 3.2.9 on 2021-12-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kontakt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=1200)),
            ],
        ),
    ]
