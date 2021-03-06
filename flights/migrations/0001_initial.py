# Generated by Django 3.0.7 on 2022-06-10 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')])),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('dob', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlightDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=40)),
                ('airlines', models.CharField(max_length=30)),
                ('dep_time', models.TimeField(max_length=30)),
                ('dep_date', models.DateField()),
                ('duration', models.TimeField()),
                ('ticket_type', models.CharField(choices=[('B', 'Business Class'), ('E', 'Economic Class')], max_length=30)),
                ('price', models.IntegerField()),
                ('dep_city', models.CharField(max_length=30)),
                ('des_city', models.CharField(max_length=30)),
                ('runway_no', models.IntegerField()),
                ('total_seats', models.IntegerField()),
                ('avail_seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=10)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField()),
                ('booking_date', models.DateTimeField()),
                ('des_city', models.CharField(max_length=30)),
                ('no_of_passengers', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.FlightDetails')),
                ('passenger', models.ManyToManyField(to='flights.Passenger')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
