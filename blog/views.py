from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from blog.models import BlogPost, BlogPostForm


def archive(request):
    """
    页面显示
    :param request:
    :return:
    """
    posts = BlogPost.objects.all().order_by('-timestamp')
    form = BlogPostForm()
    return render(request, 'archive.html',
                  locals())


def create_blog(request):
    """
    博客内容编辑提交类
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 未使用django自带的表单模式
        # try:
        #     blog = BlogPost.objects.create(
        #         title=request.POST.get('title'),
        #         body=request.POST.get('body'),
        #         timestamp=datetime.now(),
        #     )
        #     print(blog)
        # except:
        #     print("失败")

        # 使用form类创建
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # 由于时间参数，所以save时不能执行
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    # 通过HttpResponseRedirect重定向到指定页面
    return HttpResponseRedirect('/blog/')









