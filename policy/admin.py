from django.contrib import admin, auth
from import_export.admin import ImportExportActionModelAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, ChoiceDropdownFilter
from rangefilter.filter import DateRangeFilter

from .resource import PolicyResource, CustomerResource
from .models import IncomeGroup, Customer, FuelType, VehicleSegment, Policy

admin.site.site_header = 'Policy Agent'
admin.site.site_title = 'Policy Agent'
admin.site.index_title = 'Policy Agent Admin panel'
admin.site.site_short_title = 'PA'
admin.site.unregister(auth.models.Group)


# class IncomeGroupAdmin(admin.ModelAdmin):

#     class Meta:
#         model = IncomeGroup
#         verbose_name = 'Income Group'
#         verbose_name_plural = "Income Group's"
#         fields = ['id', 'name']

# admin.site.register(IncomeGroup, IncomeGroupAdmin)


class CustomerAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = CustomerResource
    list_display = ['id', 'gender', 'income_group', 'region', 'marital_status']
    search_fields = ['id']
    list_per_page = 10

    list_filter = (
            ('gender', ChoiceDropdownFilter),
            ('income_group', RelatedDropdownFilter),
            ('region', ChoiceDropdownFilter),
        )


    class Meta:
        model = Customer
        verbose_name = 'Customer'
        verbose_name_plural = "Customer's"
        fields = ['id', 'gender', 'income_group', 'region', 'marital_status']

admin.site.register(Customer, CustomerAdmin)


# class FuelTypeAdmin(admin.ModelAdmin):

#     class Meta:
#         model = FuelType
#         verbose_name = 'Customer'
#         verbose_name_plural = "Customer's"
#         fields = ['id', 'fuel_type']

# admin.site.register(FuelType, FuelTypeAdmin)


# class VehicleSegmentAdmin(admin.ModelAdmin):

#     class Meta:
#         model = VehicleSegment
#         verbose_name = 'Vehicle Segment'
#         verbose_name_plural = "Vehicle Segment's"
#         fields = ['id', 'vehicle_segment']

# admin.site.register(VehicleSegment, VehicleSegmentAdmin)


class PolicyAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = PolicyResource
    readonly_fields = ['date_of_purchase', 'customer']
    list_display = ['id', 'customer', 'vehicle_segment', 'fuel', 'date_of_purchase',
                    'premium', 'bodily_injury_liability', 'personal_injury_protection',
                    'property_damage_liability', 'collision', 'comprehensive' ]
    search_fields = ['id', 'customer__id']
    list_editable = ['premium']
    list_per_page = 10

    list_filter = (
            ('date_of_purchase', DateRangeFilter),
            ('vehicle_segment', RelatedDropdownFilter),
            ('fuel', RelatedDropdownFilter),
        )

    class Meta:
        model = Policy
        verbose_name = 'Policy'
        verbose_name_plural = "Policy's"
        fields = ['id', 'customer', 'vehicle_segment', 'fuel', 'date_of_purchase', 
                'premium', 'bodily_injury_liability', 'personal_injury_protection',
                'property_damage_liability', 'collision', 'comprehensive']

admin.site.register(Policy, PolicyAdmin)