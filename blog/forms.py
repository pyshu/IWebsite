__author__ = 'lius'

from django.forms import ModelForm
from blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('username','email','content','article')
        # fields = "__all__"