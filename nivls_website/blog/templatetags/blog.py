# -*- coding: utf-8 -*-

import urllib, hashlib
from datetime                        import datetime
from django                          import template
from nivls_website.blog.models       import Category, Tag, Entry, Comment
from django.contrib.sites.models     import Site

register = template.Library()


@register.inclusion_tag('blog/templatetags/category_list.html')
def category_list():
    categories = Category.objects.order_by('left', 'level')
    cat_list = []
    if categories:
        for i, cat in enumerate(categories):
            if i != 0:
                if cat.level < categories[i-1].level:
                    for j in range(categories[i-1].level - cat.level):
                        cat_list.append('level_down')
                elif cat.level > categories[i-1].level:
                    cat_list.append('level_up')
            cat_list.append(cat)

    return {'nested_tree': cat_list}


@register.inclusion_tag('blog/templatetags/display_entries.html')
def display_entries(entries):
    return {'entries': entries}


@register.inclusion_tag('blog/templatetags/display_entry.html')
def display_entry(entry, display_share_buttons = False):
    return {'entry':                entry,
            'display_share_buttons': display_share_buttons}


@register.inclusion_tag('blog/templatetags/display_pagination.html')
def display_pagination(paginator):
    return {'paginator': paginator}


@register.inclusion_tag('blog/templatetags/flash_tag_cloud.html')
def flash_tag_cloud():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('blog/templatetags/archive_list.html')
def archive_list():
    date_list = Entry.objects.dates('date', 'month').order_by('-date')
    return {'date_list': date_list}


@register.inclusion_tag('blog/templatetags/display_comment_list.html')
def display_comment_list(Entry):
    comment_list = Comment.objects.filter(entry=Entry.id).order_by('date')
    return {'comment_list': comment_list,
            'entry': Entry}


@register.inclusion_tag('blog/templatetags/display_comment.html')
def display_comment(Entry, Comment, preview=False):
    return {'comment': Comment,
            'entry'  : Entry,
            'preview': preview}


@register.inclusion_tag('blog/templatetags/display_gravatar.html')
def display_gravatar(email, size=48):
    default = "http://localhost:8000/media/img/avatar.png"
    url = "http://www.gravatar.com/avatar.php?" + urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        'default':     default,
        'size':        str(size)
        })
    return {'gravatar': {'url':  url,
                         'size': size}}
