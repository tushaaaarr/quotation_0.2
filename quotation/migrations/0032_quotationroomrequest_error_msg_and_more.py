# Generated by Django 4.2.1 on 2023-06-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0031_rename_company_footer_company_company_footer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationroomrequest',
            name='error_msg',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='quotationroomrequest',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs'),
        ),
        migrations.AddField(
            model_name='quotationroomrequest',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('G', 'Generating'), ('R', 'Ready'), ('E', 'Error')], default='P', max_length=2),
        ),
        migrations.AddField(
            model_name='quotationroomrequest',
            name='url',
            field=models.CharField(default='NA', max_length=128),
            preserve_default=False,
        ),
    ]
