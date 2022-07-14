from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from insurance_agent.constant import male, female, trans, north, south, east, west

class IncomeGroup(models.Model):

    name = models.CharField(verbose_name='Income Group Range', null=False, blank=False, max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'income_group'

class Customer(AbstractUser):

    gender_choices = (
        (male, 'Male'),
        (female, 'Female'),
        (trans, 'Trans'),
    )

    region_choices = (
        (north, 'North'),
        (south, 'South'),
        (east, 'East'),
        (west, 'West'),
    )

    gender = models.CharField(verbose_name='Gender', max_length=8, null=True, blank=False, choices=gender_choices)
    income_group = models.ForeignKey(to=IncomeGroup, verbose_name='Income Group', null=True, blank=False, on_delete=models.DO_NOTHING)
    region = models.CharField(verbose_name='Region', max_length=8, null=True, blank=False, choices=region_choices)
    marital_status = models.BooleanField(verbose_name='Marital Status', null=True, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'customer'


class FuelType(models.Model):

    fuel_type = models.CharField(verbose_name='Fuel Type', blank=False, null=False, max_length=250)

    def __str__(self):
        return self.fuel_type

    class Meta:
        db_table = 'fuel_type'


class VehicleSegment(models.Model):

    vehicle_segment = models.CharField(verbose_name='Vehicle Segment', blank=False, null=False, max_length=250)

    def __str__(self):
        return self.vehicle_segment

    class Meta:
        db_table = 'vehicle_segment'


class Policy(models.Model):

    customer = models.ForeignKey(to=Customer, verbose_name='Customer', null=False, blank=False, on_delete=models.DO_NOTHING)
    vehicle_segment = models.ForeignKey(to=VehicleSegment, verbose_name='Vehicle Segment', null=False, blank=False, on_delete=models.DO_NOTHING)
    fuel = models.ForeignKey(to=FuelType, verbose_name='Fuel', null=False, blank=False, on_delete=models.DO_NOTHING)
    date_of_purchase = models.DateField(editable=False)
    premium = models.FloatField(verbose_name='Premium', null=False, blank=False, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    bodily_injury_liability = models.BooleanField(verbose_name='Bodily Injury Liability', null=False, blank=False)
    personal_injury_protection = models.BooleanField(verbose_name='Personal Injury Protection', null=False, blank=False)
    property_damage_liability = models.BooleanField(verbose_name='Property Damage Liability', null=False, blank=False)
    collision = models.BooleanField(verbose_name='Collision', null=False, blank=False)
    comprehensive = models.BooleanField(verbose_name='Comprehensive', null=False, blank=False)

    def __str__(self):
        return str(self.id)
    

    class Meta:
         db_table = 'policy'