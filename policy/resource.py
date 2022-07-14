from import_export import fields
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget

from .models import Customer, FuelType, IncomeGroup, Policy, VehicleSegment

# Upload customer data from csv
class CustomerResource(ModelResource):
    income_group = fields.Field(widget=ForeignKeyWidget(IncomeGroup, 'name'), attribute='income_group')

    def before_import_row(self, row, row_number=None, **kwargs):
        if row['income_group']:
            income_group_object, income_group = IncomeGroup.objects.get_or_create(
                name=row['income_group']
            )

    class Meta:
        model = Customer
        skip_unchanged = True
        report_skipped = True
        fields = ['id', 'income_group', 'gender',
                'region', 'marital_status', 'username']


# Resource to upload data from the csv file
class PolicyResource(ModelResource):
    customer = fields.Field(widget=ForeignKeyWidget(Customer), attribute='customer')
    vehicle_segment = fields.Field(widget=ForeignKeyWidget(VehicleSegment, 'vehicle_segment'), attribute='vehicle_segment')
    fuel = fields.Field(widget=ForeignKeyWidget(FuelType, 'fuel_type'), attribute='fuel')

    def before_import_row(self, row, row_number=None, **kwargs):
        if row['vehicle_segment']:
            vehicle_segment_object, vehicle_segment = VehicleSegment.objects.get_or_create(
                vehicle_segment=row['vehicle_segment']
            )
        
        if row['fuel']:
            fuel_object, fuel = FuelType.objects.get_or_create(
                fuel_type=row['fuel']
            )

    class Meta:
        model = Policy
        skip_unchanged = True
        report_skipped = True
        fields = ['id', 'customer', 'vehicle_segment',
                  'fuel', 'date_of_purchase', 'premium',
                  'bodily_injury_liability', 'personal_injury_protection',
                  'property_damage_liability', 'collision', 'comprehensive']
