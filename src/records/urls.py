"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as records_views

urlpatterns = [
    path('record_list_user/', records_views.RecordUserList.as_view(), name='Record-User-List'),
    path('record_list_all/', records_views.RecordListAll.as_view(), name='record-list-all'),
    path('view_record/<int:pk>/', records_views.ViewRecord.as_view(), name='view-record'),
    path('new_patient/', records_views.new_patient.as_view(), name='new_patient'),
    path('new_record/', records_views.new_record.as_view(), name='new_record'),
    path('edit/<int:pk>/', records_views.edit_record.as_view(), name='edit-record'),

]
