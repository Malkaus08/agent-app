# Generated by Django 4.0.4 on 2022-05-16 08:48

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')], max_length=8, null=True, verbose_name='Gender')),
                ('region', models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=8, null=True, verbose_name='Region')),
                ('marital_status', models.BooleanField(null=True, verbose_name='Marital Status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'db_table': 'customer',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=250, verbose_name='Fuel Type')),
            ],
            options={
                'db_table': 'fuel_type',
            },
        ),
        migrations.CreateModel(
            name='IncomeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Income Group Range')),
            ],
            options={
                'db_table': 'income_group',
            },
        ),
        migrations.CreateModel(
            name='VehicleSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_segment', models.CharField(max_length=250, verbose_name='Vehicle Segment')),
            ],
            options={
                'db_table': 'vehicle_segment',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateField(editable=False)),
                ('premium', models.FloatField(validators=[django.core.validators.MaxValueValidator(1000000)], verbose_name='Premium')),
                ('bodily_injury_liability', models.BooleanField(verbose_name='Bodily Injury Liability')),
                ('personal_injury_protection', models.BooleanField(verbose_name='Personal Injury Protection')),
                ('property_damage_liability', models.BooleanField(verbose_name='Property Damage Liability')),
                ('collision', models.BooleanField(verbose_name='Collision')),
                ('comprehensive', models.BooleanField(verbose_name='Comprehensive')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='policy.fueltype', verbose_name='Fuel')),
                ('vehicle_segment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='policy.vehiclesegment', verbose_name='Vehicle Segment')),
            ],
            options={
                'db_table': 'policy',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='income_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='policy.incomegroup', verbose_name='Income Group'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
