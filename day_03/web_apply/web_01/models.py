from django.db import models

# # Create your models here.
# class Group(models.Model):
#     name = models.CharField(max_length=64, verbose_name='用户名')
#
#     class Meta:
#         db_table = 'tb_group'
#         verbose_name = '用户组表'
#
#
# class User(models.Model):
#     username = models.CharField(max_length=128, verbose_name='用户名')
#     password = models.CharField(max_length=128, verbose_name='密码')
#
#     group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True,verbose_name='用户组')
#     class Meta:
#         db_table = 'tb_users'
#         verbose_name = '用户表'

from django.db import models

# Create your models here.


# 定义一个用户模型类
class User(models.Model):
    """用户模型类"""
    # 模型类字段名 = models.字段类型(选项参数)
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    # default：设置向数据库添加数据时，字段使用的默认值


    class Meta:
        # 指定模型类对应表名称
        db_table = 'tb_users'
        verbose_name = '用户表'
