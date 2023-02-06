import os
import json
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from mscreening.services import Full_code_fin

from velzon.settings import DJANGO_DRF_FILEPOND_UPLOAD_TMP
from django_drf_filepond.api import store_upload
from django_drf_filepond.api import get_stored_upload
from django_drf_filepond.api import get_stored_upload_file_data

# Create your views here.
class MscreeningView(LoginRequiredMixin,TemplateView):
    pass
    
mscreening_view = MscreeningView.as_view(template_name="mscreening/index.html")

@require_POST # 해당 뷰는 POST method 만 받는다.
def getExcelParse(request):
    # POST 요청일 때
    if request.method == 'POST':
        data = json.loads(request.body)
        result = {}
        # do something
        print(data["key"])

        print("여기가 시작")

        files = os.listdir(os.path.join(DJANGO_DRF_FILEPOND_UPLOAD_TMP, data["key"]))

        for file in files: 
            filename = os.path.join(os.path.join(DJANGO_DRF_FILEPOND_UPLOAD_TMP, data["key"]), file)
            # os.rename(filename, filename + '.xlsx') 
            # Full_code_fin(filename + '.xlsx')
            try: 
                os.rename(filename, filename + '.xlsx') 
                result = Full_code_fin(filename + '.xlsx')
            except: 
                print('error')
                pass

        return JsonResponse(result)