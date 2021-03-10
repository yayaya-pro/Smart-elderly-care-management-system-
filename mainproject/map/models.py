from django.db import models

# Create your models here.
class Test(models.Model):

    class Meta:
        verbose_name = u"地图管理"
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.Meta.verbose_name

