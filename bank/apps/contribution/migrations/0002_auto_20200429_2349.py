# Generated by Django 3.0.2 on 2020-04-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
