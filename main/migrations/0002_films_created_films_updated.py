# Generated by Django 4.1.2 on 2022-10-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='films',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
