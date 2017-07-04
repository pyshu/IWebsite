# -*- coding:utf-8 -*-
__author__ = 'lius'

from django import template
from django.utils.html import format_html
register = template.Library()  #注册到django的语法库

@register.simple_tag
def guess_page(current_page,loop_num):
    offset = abs(current_page-loop_num)
    if offset <= 3:
        if current_page == loop_num:
            page_ele = '''<li class="active" ><a class="atv" href="?page=%s">%s</a> </li>'''%(loop_num, loop_num)
        else:
            page_ele = '''<li class="" ><a href="?page=%s">%s</a> </li>'''%(loop_num, loop_num)
        return format_html(page_ele)
    else:
        return ''

