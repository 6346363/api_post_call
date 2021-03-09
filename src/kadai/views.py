# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView,ListView
from .models import ai_analysis_log
from .forms import ai_analysis_logForm
from django.shortcuts import redirect
import requests
import json

class LogCreateView(CreateView):
    model = ai_analysis_log
    form_class = ai_analysis_logForm
    template_name = "kadai/form.html"
    success_url = "/"

    def form_valid(self,form):
        
        imagePath = self.request.POST.get("image_path")
        apiUrl = 'https://****/dw_stage/dw-resource'
        query = {
            'image_path':imagePath
        }

        post = form.save(commit=False)
        post.request_timestamp = 309014200 # 適当な値をセット

        # API Post
        response = requests.post(apiUrl,json=query)
        resJson = response.json() # Json形式に変換

        post.response_timestamp = 309015000 # 適当な値をセット

        post.success = resJson['success']
        post.message = resJson['message']
        if resJson["success"] == "true":
            post.class_value = resJson['estimated_data']['class'] # 3 #response.estimated_data.'class'
            post.confidence = resJson['estimated_data']['confidence'] #response.estimated_data.confidence
        
        # DBに保存
        post.save()

        return redirect('kadai:list')

class LogListView(ListView):
    model = ai_analysis_log
    template_name = "kadai/list.html"
