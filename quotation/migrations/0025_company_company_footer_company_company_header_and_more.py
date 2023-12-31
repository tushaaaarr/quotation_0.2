# Generated by Django 4.2.2 on 2023-06-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0024_remove_company_username_remove_hotel_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Company_footer',
            field=models.ImageField(default='default_logo.jpg', upload_to='Company_footer'),
        ),
        migrations.AddField(
            model_name='company',
            name='Company_header',
            field=models.ImageField(default='default_logo.jpg', upload_to='Company_header'),
        ),
        migrations.AddField(
            model_name='company',
            name='Company_logo',
            field=models.ImageField(default='default_logo.jpg', upload_to='Company_logo'),
        ),
        migrations.AddField(
            model_name='company',
            name='Company_logo_watermark',
            field=models.ImageField(default='default_logo.jpg', upload_to='Company_logo'),
        ),
    ]
