# Generated by Django 4.2.1 on 2023-06-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0021_quotationroomrequest_no_of_adults_single'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationroomrequest',
            name='no_of_adults_single',
        ),
    ]
