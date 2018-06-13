from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# 提取出了 pygments 支持的所有语言的词法分析程序
LEXERS = [item for item in get_all_lexers() if item[1]]
# 提取出了 pygments 支持的所有语言列表
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# 提取出了 pygments 支持的所有格式化风格列表
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)  # 是否显示行号
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
