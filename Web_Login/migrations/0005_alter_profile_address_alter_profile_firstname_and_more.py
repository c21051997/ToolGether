# Generated by Django 4.1.7 on 2023-04-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Login', '0004_remove_profile_city_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, default='000', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, default='John', max_length=264),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, default='Smith', max_length=264),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='000', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.CharField(blank=True, default='000', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='media\\pg.png', upload_to='media/profile_img/520858161'),
        ),
    ]