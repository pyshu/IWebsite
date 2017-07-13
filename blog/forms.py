__author__ = 'lius'

from django.forms import ModelForm
from blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('username','email','content')
        # fields = "__all__"
        labels = {
            'username': '用户名',
            'email': '邮箱',
        }
        error_messages = {
            'email': {
                'required': '邮箱不能为空.',
                'invalid': '邮箱格式错误.',
            }
        }