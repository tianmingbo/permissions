from django.db import models

# Create your models here.
'''
用户表（和角色多对多）
角色表（和权限多对多）
权限表（）
'''


class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    roles = models.ManyToManyField(to="Roles")

    def __str__(self):
        return self.name


class Roles(models.Model):
    title = models.CharField(max_length=32)
    peimissions = models.ManyToManyField(to='Permissions')

    def __str__(self):
        return self.title


class Permissions(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)

    action = models.CharField(max_length=32)
    group = models.ForeignKey('PermissionGroup')

    def __str__(self):
        return self.title


class PermissionGroup(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title
