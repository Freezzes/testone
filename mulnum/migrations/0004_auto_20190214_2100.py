# Generated by Django 2.1.4 on 2019-02-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mulnum', '0003_auto_20190214_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='numtext',
            field=models.CharField(max_length=20),
        ),
    ]
