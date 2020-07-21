from django.db import models

# 级联数据 序列化

class UserModel(models.Model):
    u_name = models.CharField(max_length=32,unique=True)
    u_password = models.CharField(max_length=256)

    #  在后台显示字段
    def __str__(self):
        return self.u_name

class Address(models.Model):
    a_address = models.CharField(max_length=256)
    a_user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
#  见 序列化器  如果非要使用自定义模型  address_list  需要添加模型 字段，
#      需指定 Related_name = 'adderss_list'
#     a_user = models.ForeignKey(UserModel,related_name='address_list',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.a_address


