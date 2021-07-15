from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세유ㅋ 저는 인덱스 입니다ㅋ")