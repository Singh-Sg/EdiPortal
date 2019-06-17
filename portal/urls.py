from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excel-upload/', views.excelSheetData, name='excel_sheet_data'),

]