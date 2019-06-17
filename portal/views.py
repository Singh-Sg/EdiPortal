import json
import logging
import pandas as pd

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime, timezone
from django.views.decorators.csrf import csrf_exempt


from .models import *
from .tasks import uploadExcelSheet


def index(request):
    """
    """
    data = InfraVltgDetail.objects.all()
    import pdb; pdb.set_trace()
    context = {'data': data.count(), 'query':data}
    return render(request, 'portal/index.html', context)


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
