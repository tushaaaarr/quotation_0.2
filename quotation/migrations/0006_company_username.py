# Generated by Django 4.2.1 on 2023-06-02 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0005_alter_hotel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='quotation.employee'),
        ),
    ]
