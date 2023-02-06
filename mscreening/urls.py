from django.urls import path
from mscreening.views import (
    getExcelParse,
    mscreening_view,
)

app_name = 'mscreening'

urlpatterns = [
    path('',view =mscreening_view,name="mscreening"),
    path('getExcelParse',view =getExcelParse,name="home"),
   
]


