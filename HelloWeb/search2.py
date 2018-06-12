from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        if request.POST['q'] != '':
            ctx['rlt'] = '你提交的内容为：' + request.POST['q']
        else:
            ctx['rlt'] = '你提交了空表单'
    return render(request, "post.html", ctx)