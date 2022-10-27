# Generated by Django 4.1.2 on 2022-10-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_films_director_delete_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='films',
            name='director',
            field=models.ManyToManyField(blank=True, to='main.director'),
        ),
    ]