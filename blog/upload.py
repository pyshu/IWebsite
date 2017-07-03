# -*- coding: utf-8 -*-
#coding=utf-8
import  os
import  uuid
import  json
import  datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import  HttpResponse
from django.conf import settings

'''
@csrf_exempt用于取消csrftoken验证
url为:http://127.0.0.1:8000/admin/upload/?dir=media post请求
'''
@csrf_exempt
def upload(request):
    '''
    kindeditor图片上传返回数据格式说明：
    {"error": 1, "message": "出错信息"}
    {"error": 0, "url": "图片地址"}
    '''
    result = {"error": 1, "message": u"上传失败"}
    files = request.FILES.get("imgFile", None)  #input type="file" 中name属性对应的值为imgFile
    type = request.GET['dir']  #获取资源类型
    if  files:
        result = process_upload(files,type)
    #结果以json形式返回
    return HttpResponse(json.dumps(result),content_type="application/json")


def is_ext_allowed(type,ext):
    '''
    根据类型判断是否支持对应的扩展名
    '''
    ext_allowed = {}
    ext_allowed['image'] = ['jpg','jpeg', 'bmp', 'gif', 'png']
    ext_allowed['flash'] = ["swf", "flv"]
    ext_allowed['media'] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb", "mp4"]
    ext_allowed['file'] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz", "bz2", 'pdf']
    return ext in ext_allowed[type]

def get_relative_file_path():
    '''
    获取相对路径
    '''
    dt = datetime.datetime.today()
    relative_path = '%s/%s/' %(dt.year,dt.month)
    absolute_path = os.path.join(settings.MEDIA_ROOT,relative_path)
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    return relative_path


def process_upload(files,type):
    dir_types = ['image','file']
    #判断是否支持对应的类型
    if type not in dir_types:
        return {"error":1, "message": u"上传类型不支持[必须是image,flash,media,file]"}

    cur_ext = files.name.split('.')[-1]  #当前上传文件的扩展名
    #判断是否支持对应的扩展名
    if not is_ext_allowed(type,cur_ext):
        return {'error':1, 'message': u'error:扩展名不支持 %s类型不支持扩展名%s' %(type,cur_ext)}

    relative_path = get_relative_file_path()
    #linux中一切皆文件
    file_name = str(uuid.uuid1()) + "." + cur_ext
    base_name = os.path.join(settings.MEDIA_ROOT,relative_path)
    file_full_path = os.path.join(base_name,file_name).replace('\\','/') #windows中的路径以\分隔
    file_url = settings.MEDIA_URL + relative_path + file_name

    with open(file_full_path,'wb') as f:
        if  files.multiple_chunks() == False:  #判断是否大于2.5M
            f.write(files.file.read())
        else:
            for chunk in files.chunks():
                f.write(chunk)


    return {"error": 0, "url": file_url}