"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
from . import views
#
# def login(request):
#     """
#     处理用户请求，并返回结果
#     :param request中放着用户请求的所有信息
#     :return
#         HttpResponse只能输出字符串
#         render：第一个参数是request,第二个参数是网页文件
#     """
#     if request.method == "GET":
#         # return HttpResponse('<input/>')
#         return render(request,'2.html')
#     else:
#         # 这样写即便没有也不会报错，而是得到一个null
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         print(u)
#         print(p)
#         if u == 'root' and p == '123123':
#             # print('跳转到老男孩网站！')
#             # return redirect('http://www.oldboyedu.com')
#             return redirect('/index/')
#         else:
#             return render(request,'2.html',{'msg':'123123'})
# def index(request):
#     return render(request, 'index.html', {
#                                             "name": "alex",
#                                             "users":['李贽','李杰'],
#                                             "dict":{'k1':'v1','k2':'v2'},
#                                             "user_list_dict":[
#                                                 {'id':1,'name':'alex','email':'112233'},
#                                                 {'id':2,'name':'alwwex','email':'112ww233'}
#                                             ]
#                                         })

# 一下用来将网址和对应的函数（网页文件）关联起来，实现网址和网页的关联和跳转
urlpatterns = [
    # path('admin/', admin.site.urls),   # 这是django自带的，暂时用不到，先注释掉
    url(r'^own/',views.own),
    url(r'^results/',views.results),
    url(r'^mainPage/',views.mainPage),
]

