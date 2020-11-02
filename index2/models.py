from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 't_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.user_name

    @property
    def beauty(self):
        return '三吉彩花'

