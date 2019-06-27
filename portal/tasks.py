import string
import logging
import pandas as pd
from celery import shared_task
from django.http import JsonResponse
from datetime import datetime



from .models import *


# @shared_task
def uploadExcelSheet(data):
    """
    Create Data
    """
    for row in range(data.shape[0]):
        # date = pd.to_datetime('3/17/2019 6:23:23.000000 PM')
        # date_with_time = datetime.combine(date, tzone.now().time())
        # date_with_timezone = date_with_time.replace(tzinfo=tzone.utc)
        try:

            asof = data.iat[row, 0]
            environment = data.iat[row, 1]
            username = data.iat[row, 2]
            vltg_identity = data.iat[row, 3]
            cvproduct = data.iat[row, 4]
            cvapi = data.iat[row, 5]
            srcip = data.iat[row, 6]
            typeofapi = data.iat[row, 7]
            hostname = data.iat[row, 8]
            create_dt = data.iat[row, 9]

            try:
                asof = datetime.strptime(asof.split(" ")[0], "%m/%d/%Y")
            except Exception:
                asof = datetime.strptime(asof.split(" ")[0], "%Y-%d-%m")

            try:
                create_dt = datetime.strptime(create_dt.split(" ")[0], "%m/%d/%Y")
            except Exception:
                create_dt = datetime.strptime(create_dt.split(" ")[0], "%Y-%d-%m")

            InfraVltgDetail.objects.create(
                asof=asof,
                environment=environment,
                username=username,
                vltg_identity=vltg_identity,
                cvproduct=cvproduct,
                cvapi=cvapi,
                srcip=srcip,
                typeofapi=typeofapi,
                hostname=hostname,
                create_dt=create_dt
            )
        except Exception as e:
            logger = logging.getLogger('root')
            logger.error('Excel Sheet error', exc_info=True, extra={
                'exception': e,
            })
            return JsonResponse({'status': 500, 'exception': e})
    return True
