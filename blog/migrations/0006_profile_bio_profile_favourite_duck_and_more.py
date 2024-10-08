# Generated by Django 5.1.1 on 2024-09-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='no bio available', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='favourite_Duck',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
