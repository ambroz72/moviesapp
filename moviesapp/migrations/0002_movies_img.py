# Generated by Django 4.2.8 on 2023-12-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]