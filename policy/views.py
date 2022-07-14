from django.contrib import admin
from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.template.loader import get_template
from django.db.models.functions import ExtractMonth

from .models import Policy

class PolicyChartReport(View):

    def get(self, request):
        template = 'report/policy_chart.html'
        context = {
            "site_title": admin.site.site_title,
            "site_header": admin.site.site_header,
            "site_url": admin.site.site_url,
            "has_permission": admin.site.has_permission(request),
            "available_apps": admin.site.get_app_list(request),
            "is_popup": False,
            "is_nav_sidebar_enabled": admin.site.enable_nav_sidebar,
        }
        return render(request, template, context)


class PolicyChartData(View):

    def get(self, request):
        labels = []
        data = []
        query_filter = {}

        request_data = request.POST if request.method == 'POST' else request.GET

        if request_data['region'] != '0':
            query_filter['customer__region'] = request_data['region']
        
        get_month_wise_data = Policy.objects.filter(**query_filter).values(
            month=ExtractMonth('date_of_purchase')
        ).order_by().values('month').annotate(
            number_of_policy=Count('id')
        ).values('month', 'number_of_policy')

        for entry in get_month_wise_data:
            labels.append(entry['month'])
            data.append(entry['number_of_policy'])
            
        return JsonResponse({'labels': labels, 'data': data})