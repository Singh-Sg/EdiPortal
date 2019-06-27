import json
import logging
import pandas as pd

from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime, timezone
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import TruncMonth
from django.core.serializers.json import DjangoJSONEncoder


from .models import InfraVltgDetail
from .tasks import uploadExcelSheet


def index(request):
    """
    """
    #by environment
    environment = InfraVltgDetail.objects.values("environment").annotate(name_count=Count('environment'))
    #by user
    byuser = InfraVltgDetail.objects.values("username").annotate(name_count=Count('username'))
    # by time
    # by_month = InfraVltgDetail.objects.values("create_dt__month").annotate(name_count=Count('create_dt__month'))
    
    by_month = InfraVltgDetail.objects.annotate(month=TruncMonth('create_dt')).values('month').annotate(name_count=Count('id')).values('month', 'name_count')

    # import pdb; pdb.set_trace()
    context = {'data': InfraVltgDetail.objects.all().count(), 'environment': environment,
               'byuser': byuser, 'byMonth': by_month}
    return render(request, 'portal/index.html', context)


def envByUserName(request, *args, **kwargs):
    """
    """
    try:
        env = request.GET['environment']
        username = InfraVltgDetail.objects.filter(environment=env).values("username").annotate(name_count=Count('username'))
        users = []
        for user in username:
            users.append(user)
        return JsonResponse({"data": users, 'status_code': "200", 'env': env})
    except Exception:
        return JsonResponse({'error': 'invalid request', 'status': 'fail'})


def envByMonth(request, *args, **kwargs):
    """
    """
    try:
        env = request.GET['environment']
        username = request.GET['username']
        query_object =Q(environment=env) & Q(username=username)
        by_month = InfraVltgDetail.objects.filter(query_object).annotate(month=TruncMonth('create_dt')).values('month').annotate(name_count=Count('id')).values('month', 'name_count')
        by_month_data = json.dumps(list(by_month), cls = DjangoJSONEncoder)
        return JsonResponse({"data": by_month_data, 'status_code': "200"})
    except Exception:
        return JsonResponse({'error': 'invalid request', 'status': 'fail'})


def environmentsByUser(request, *args, **kwargs):
    """
    """
    try:
        username = request.GET['username']
        environments = InfraVltgDetail.objects.filter(username=username).values("environment").annotate(name_count=Count('environment'))
        env = []
        for environment in environments:
            env.append(environment)
        return JsonResponse({"data": env, 'status_code': "200", 'username': username})
    except Exception:
        return JsonResponse({'error': 'invalid request', 'status': 'fail'})


def environmentsByMonth(request, *args, **kwargs):
    """
    """
    try:
        month = request.GET['month']
        environments = InfraVltgDetail.objects.filter(create_dt__month=month).values("environment").annotate(name_count=Count('environment'))
        env = []
        for environment in environments:
            env.append(environment)
        return JsonResponse({"data": env, 'status_code': "200", 'month': month})
    except Exception:
        return JsonResponse({'error': 'invalid request', 'status': 'fail'})


def userByEnvironmentsByMonth(request, *args, **kwargs):
    """
    """
    try:
        env = request.GET['environment']
        month = request.GET['month']
        query_object = Q(environment=env) & Q(create_dt__month=month)
        usernames = InfraVltgDetail.objects.filter(query_object).values("username").annotate(name_count=Count('username'))
        username_data = []
        for data in usernames:
            username_data.append(data)
        return JsonResponse({"data": username_data, 'status_code': "200"})
    except Exception:
        return JsonResponse({'error': 'invalid request', 'status': 'fail'})


def excelSheetData(request, *args, **kwargs):
    """
    API endpoint to upload excel sheet
    """
    if request.method == "POST":
        """
        Get excel sheet from zigway bosses
        """
        try:
            file = request.FILES.get('file')
            # Reading file using pandas
            data = pd.read_excel(file)

            # data = pd.read_excel(file, dtype={'ASOF': str, 'USERNAME': srf})
        except Exception as e:
            logger = logging.getLogger('root')
            logger.error('Unable to upload file', exc_info=True, extra={
                'exception': e,
            })
            return JsonResponse({'status': 500, 'exception': e})

        # uploadExcelSheet.delay(data)
        uploadExcelSheet(data)

        return JsonResponse({'status': 200})
