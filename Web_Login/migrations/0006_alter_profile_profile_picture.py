# Generated by Django 4.1.7 on 2023-04-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Login', '0005_alter_profile_address_alter_profile_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media\\pg.png', upload_to='media/profile_img/281252038'),
        ),
    ]
