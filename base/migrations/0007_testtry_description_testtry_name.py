# Generated by Django 4.1.7 on 2023-04-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_testtry'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtry',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testtry',
            name='name',
            field=models.CharField(default='Your Default Value', max_length=100),
        ),
    ]
