from django.core.paginator import Paginator


# 组装分页
def page_group(pagenumber,items1):
    pagenumber = int(pagenumber)
    paginator = Paginator(items1, 10)
    if pagenumber > paginator.num_pages:
        pagenumber -= 1
    if pagenumber < 1:
        pagenumber += 1
    page = paginator.page(pagenumber)
    if paginator.num_pages < 15:
        page_list = [i for i in range(1, paginator.num_pages + 1)]
    else:
        page_list = [i for i in range(page.number, pagenumber + 15)]
    return page,page_list,paginator
