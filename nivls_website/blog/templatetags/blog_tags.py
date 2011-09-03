from django import template
from django.db.models import Count
from blog.models import Post, SeeAlso, Category
from tags.models import Tag

register = template.Library()

@register.inclusion_tag("blog/templatetags/slideshow.html")
def blog_slideshow():
    posts = Post.objects.all()[:5]
    return {'object': posts}

@register.inclusion_tag("blog/templatetags/seeAlso.html")
def blog_see_also():
    links = SeeAlso.objects.order_by("name")
    return {'links': links}

@register.inclusion_tag("blog/templatetags/archives.html")
def blog_archives():
    dates = Post.objects.dates('pub_date', 'month', order='DESC')
    return {'dates': dates}

@register.inclusion_tag("blog/templatetags/tag_cloud.html")
def blog_tagcloud():
    tags = Tag.objects.order_by("name").annotate(num_post=Count('post__id'))

    largest = 24
    smallest = 10

    for i, tag in enumerate(tags):
        if i == 0:
            count_min = tag.num_post
            count_max = tag.num_post
        else:
            if count_min > tag.num_post:
                count_min = tag.num_post
            elif count_max < tag.num_post:
                count_max = tag.num_post

    spread = count_max - count_min
    if spread <= 0:
        spread = 1
    font_spread = largest - smallest
    font_step = font_spread / spread

    tag_list = list()
    for i, tag in enumerate(tags):
        tag_size = int(smallest + ((tag.num_post - count_min) * font_step))
        tag_list.append({"obj":tag, "size":tag_size})

    return {'tags': tag_list}

@register.inclusion_tag("blog/templatetags/categories.html")
def blog_categories():
    categories = Category.objects.order_by('left')
    cat_list = list();
    if categories:
        for i, cat in enumerate(categories):
            cat_list.append(cat)
            if cat.is_root:
                last_root = cat;
            if i != 0 and (not cat.is_root or not categories[i-1].is_root):
                r = cat.left - categories[i-1].right
                if r > 1:
                    for j in range(r - 1):
                        cat_list.insert(cat_list.index(cat), 'level_down')
                if i == len(categories) - 1:
                    for j in range(last_root.right - cat.right):
                        cat_list.append('level_down')
            if cat.has_child():
                cat_list.append('level_up')
    return {'nested_tree': cat_list}
