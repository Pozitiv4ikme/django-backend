# Generated by Django 4.1.2 on 2022-10-04 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helicopter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('passengers', models.IntegerField()),
                ('maximum_speed', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
