# Generated by Django 4.2.1 on 2023-06-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0020_remove_quotationmainrequest_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationroomrequest',
            name='no_of_adults_single',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
