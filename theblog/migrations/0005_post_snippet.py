# Generated by Django 3.2.7 on 2021-10-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click to read the post', max_length=255),
        ),
    ]
