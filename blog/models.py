from django.db import models

# Create your models here.
from django import forms


class BlogPost(models.Model):
    """
    博客内容管理，对应数据库中相应的表
    """
    title = models.CharField('标题', max_length=150)
    body = models.TextField('正文')
    timestamp = models.DateTimeField('编辑时间')
    objects = models.Manager()

    class Meta:
        # 修改表名
        db_table = 'blog_post'
        ordering = ('-timestamp',)


class BlogPostForm(forms.ModelForm):
    """
    表单
    """
    # title = forms.CharField(max_length=50)
    # body = forms.CharField(widget=forms.Textarea(
    #     attrs={'cols': 60, 'rows': 3}
    # ))
    # timestamp = forms.DateTimeField()
    class Meta:
        model = BlogPost
        exclude = {'timestamp'}



