# Generated by Django 3.1 on 2020-09-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0002_commodity_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemid', models.IntegerField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemid', models.IntegerField()),
                ('imgurl', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='commodity',
            name='stock',
            field=models.IntegerField(default=128),
            preserve_default=False,
        ),
    ]