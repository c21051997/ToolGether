# Generated by Django 4.1.7 on 2023-04-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_Main', '0012_alter_item_image_1_alter_item_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_1',
            field=models.ImageField(upload_to='media/item_img/229394789'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_2',
            field=models.ImageField(upload_to='media/item_img/229394789'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_3',
            field=models.ImageField(upload_to='media/item_img/229394789'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_4',
            field=models.ImageField(upload_to='media/item_img/229394789'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_5',
            field=models.ImageField(upload_to='media/item_img/229394789'),
        ),
    ]