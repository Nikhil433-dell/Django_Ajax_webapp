# Generated by Django 4.0.2 on 2022-02-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='avg_speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='temp',
            field=models.IntegerField(),
        ),
    ]