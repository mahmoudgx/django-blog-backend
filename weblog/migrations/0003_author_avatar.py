# Generated by Django 5.0.6 on 2024-07-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='author_avatars/'),
        ),
    ]
