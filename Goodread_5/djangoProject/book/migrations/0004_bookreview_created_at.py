# Generated by Django 4.1.1 on 2022-11-11 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_cover_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
