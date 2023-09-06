# Generated by Django 4.2.1 on 2023-06-02 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(blank=True, max_length=200, null=True)),
                ('CompanyDescription', models.CharField(blank=True, max_length=200, null=True)),
                ('CompanyId', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('DateAdded', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('LastUpdated', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('AddedBy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HotelName', models.CharField(blank=True, max_length=100, null=True)),
                ('AddressLine1', models.CharField(blank=True, max_length=100, null=True)),
                ('Area', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('HotelDescription', models.CharField(blank=True, max_length=1000, null=True)),
                ('BedroomPic', models.ImageField(default='default_logo.jpg', upload_to='hotel_pics')),
                ('DiningRoomPic', models.ImageField(default='default_logo.jpg', upload_to='hotel_pics')),
                ('ReceptionRoomPic', models.ImageField(default='default_logo.jpg', upload_to='hotel_pics')),
                ('DescriptionFirstDay', models.CharField(blank=True, max_length=1000, null=True)),
                ('DescriptionFullDay', models.CharField(blank=True, max_length=1000, null=True)),
                ('DescriptionLastDay', models.CharField(blank=True, max_length=1000, null=True)),
                ('HotelLogo', models.ImageField(default='default_logo.jpg', upload_to='hotel_logos')),
                ('HotelId', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('DateAdded', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('LastUpdated', models.DateTimeField(auto_now_add=True, max_length=200, null=True)),
                ('AddedBy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RateType', models.CharField(blank=True, max_length=200, null=True)),
                ('RateSeason', models.CharField(blank=True, choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium'), ('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn')], max_length=200)),
                ('PackageType', models.CharField(blank=True, choices=[('FB Accomodation Only', 'FB Accomodation Only'), ('Ground', 'Ground'), ('Air', 'Air'), ('Half Board', 'Half Board'), ('Bed & Breakfast', 'Bed & Breakfast')], max_length=200)),
                ('RoomType', models.CharField(blank=True, choices=[('Single', 'Single'), ('Double', 'Double'), ('Triple', 'Triple')], max_length=200)),
                ('RoomCategory', models.CharField(blank=True, choices=[('Standard', 'Standard'), ('Deluxe', 'Deluxe'), ('Superior', 'Superior')], max_length=200)),
                ('TravellerType', models.CharField(blank=True, choices=[('Citizen', 'Citizen'), ('Resident', 'Resident'), ('Non-Resident', 'Non-Resident')], max_length=200)),
                ('RateCurrency', models.CharField(blank=True, choices=[('KES', 'KES'), ('USD', 'USD')], max_length=200)),
                ('AdultRate', models.FloatField(blank=True, null=True)),
                ('ChildRate', models.FloatField(blank=True, null=True)),
                ('YoungChildSharingRate', models.FloatField(blank=True, null=True)),
                ('OldChildSharingRate', models.FloatField(blank=True, null=True)),
                ('DateApplicableFrom', models.DateField(blank=True, max_length=200, null=True)),
                ('DateApplicableTo', models.DateField(blank=True, max_length=200, null=True)),
                ('uniqueId', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('DateAdded', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('LastUpdated', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('Reference', models.CharField(blank=True, max_length=200, null=True)),
                ('AddedBy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('HotelName', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quotation.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyHotelRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyHotelRateId', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('DateAdded', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('LastUpdated', models.DateTimeField(blank=True, max_length=200, null=True)),
                ('AddedBy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quotation.company')),
                ('RateType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quotation.hotelrate')),
            ],
        ),
    ]
