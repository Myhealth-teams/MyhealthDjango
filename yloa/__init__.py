import pymysql
from django.template.defaultfilters import register
from django.utils.safestring import mark_safe

pymysql.install_as_MySQLdb()



@register.filter(is_safe=True)
def to_str(value:str):
    return str(value)


@register.filter(is_safe=True)
def to_img_tag(value:str):
    if value.endswith('.jpg') or value.endswith('.JPG') or value.endswith('.png') or value.endswith('jpeg') or value.startswith("http:"):
        return mark_safe('<td style="width:120px"><img width="120px" height="120px" src="%s" > </td>' % value)

    return mark_safe("<td>%s</td>" % value)