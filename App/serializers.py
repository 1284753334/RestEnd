from rest_framework import serializers

from App.models import UserModel, Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url','id','a_address')

#  UserSerializer 需要引用 AddressSerializer ,so  UserSerializer 置于AddressSerializer 之后
class UserSerializer(serializers.HyperlinkedModelSerializer):
    #  通过用户显示地址，添加addresss_list
    address_set = AddressSerializer(many=True,read_only=True)
    #  如果非要使用自定义模型  address_list  需要修改模型 字段，详见模型
    # address_list = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('url','id','u_name','u_password','address_set')
        # fields = ('url','id','u_name','u_password','address_list')