import uuid
from rest_framework import viewsets, status
from django.core.cache import cache
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.generics import CreateAPIView, RetrieveAPIView

# 实现注册和登录 都用post
from rest_framework.response import Response

from App.Auth import LoginAuthentication
from App.models import UserModel, Address
from App.permissions import  RequireLoginPermission

from App.serializers import UserSerializer, AddressSerializer
from App.throttles import UserThrottle


class UsersAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        if action == 'login':
            u_name = request.data.get('u_name')
            u_password = request.data.get('u_password')
            try:
                user = UserModel.objects.get(u_name =u_name)
                if not user.u_password == u_password:
                    raise exceptions.AuthenticationFailed
                # 生成uuid
                token = uuid.uuid4().hex
                # 设置token的值 user.id 并将uuuid放在缓存中,若不配置缓存
                # 默认存在内存中 ，毛病多，尽量配置到redis缓存中

                cache.set(token, user.id, timeout=60 * 60*24)
                print(token)

                data = {
                    'msg': 'login success',
                    'status': 200,
                    'token': token,
                }
                return Response(data=data)
            except UserModel.DoesNotExist:
                raise exceptions.NotFound

        elif action =='register':
            return self.create(request, *args, **kwargs)
        else:
            raise exceptions. ParseError


class UserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
#      加认证，登录才能查看
    authentication_classes = (LoginAuthentication, )
    permission_classes = (RequireLoginPermission,)
    # 也可以把节流的加到此处,之针对此处的UserAPIView函数有效，dettings为全局变量，全部有效
    # throttle_classes = (UserThrottle,)



    def retrieve(self, request, *args, **kwargs):
        # query_params 默认类型是 string  pk在 路径参数 中的kwaegs 中
        if kwargs.get('pk') != str(request.user.id):
            raise exceptions.AuthenticationFailed
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddressAPIView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    # 登录认证，在 Auth.py 中
    authentication_classes = (LoginAuthentication, )
#      认证完成加权限 permssion.py
    permission_classes = (RequireLoginPermission, )

    # 重写create方法，实现地址和用户关联
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #  设置头信息
        headers = self.get_success_headers(serializer.data)
        # 获取用户
        user= request.user
        # 地址 address所在位置
        a_id = serializer.data.get('id')
        # print(a_id)
        #  获取地址模型对象
        address=Address.objects.get(pk=a_id)
        # 绑定用户
        address.a_user=user
        address.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    #  重写list 方法，获取request .user,获取单个对象的数据  能够获取  用户 和 地址的 联数据
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(a_user=request.user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)










