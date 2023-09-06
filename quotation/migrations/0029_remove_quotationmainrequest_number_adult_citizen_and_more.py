# Generated by Django 4.2.1 on 2023-06-18 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0028_remove_company_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationmainrequest',
            name='number_adult_citizen',
        ),
        migrations.RemoveField(
            model_name='quotationmainrequest',
            name='number_child_citizen',
        ),
        migrations.AlterField(
            model_name='hotelrate',
            name='adult_rate',
            field=models.FloatField(blank=True, help_text='Rate for Adult only sharing (or Single, if RoomType = single)', null=True),
        ),
        migrations.AlterField(
            model_name='hotelrate',
            name='child_rate',
            field=models.FloatField(blank=True, help_text='Rate for child only sharing (or Single, if RoomType = single)', null=True),
        ),
        migrations.AlterField(
            model_name='hotelrate',
            name='traveller_type',
            field=models.CharField(blank=True, choices=[('Resident', 'Resident'), ('Non-Resident', 'Non-Resident')], max_length=200),
        ),
    ]
