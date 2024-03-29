# Generated by Django 4.2.9 on 2024-02-19 20:41

import datetime
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
            name='ChildProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('X', 'No answer')], max_length=1)),
                ('dob', models.DateField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bloodtype', models.CharField(max_length=5)),
                ('address', models.TextField()),
                ('ismalnourished', models.BooleanField(default=False)),
                ('allergies', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dosage', models.CharField(max_length=50)),
                ('frequency', models.IntegerField()),
                ('intake_times', models.CharField(max_length=255)),
                ('childprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.childprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('X', 'No answer')], max_length=1)),
                ('is_volunteer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intake_time', models.DateTimeField(default=datetime.datetime.now)),
                ('is_taken', models.BooleanField(default=False)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.medication')),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.profile'),
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('health_status', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('childprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.childprofile')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.profile')),
            ],
        ),
        migrations.CreateModel(
            name='FollowUps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.TextField()),
                ('childprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.childprofile')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.profile')),
            ],
        ),
        migrations.CreateModel(
            name='DietaryRestriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('childprofile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.childprofile')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.profile')),
            ],
        ),
        migrations.AddField(
            model_name='childprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.profile'),
        ),
    ]
