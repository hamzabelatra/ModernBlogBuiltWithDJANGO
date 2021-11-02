# Generated by Django 3.2.7 on 2021-10-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ig_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tw_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]