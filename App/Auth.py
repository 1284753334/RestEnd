from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

#  实现 登录的人才能加地址，认证一下
from App.models import UserModel


class LoginAuthentication(BaseAuthentication):
    # 继承函数里面包含抽象 函数
    def authenticate(self, request):
        #  增删改查都需要认证，method 有点多余
        # if request.method == 'GET':
        try:
            #  获取令牌
            token= request.query_params.get('token')
            # 从缓存中获取token  不加引号
            user_id = cache.get(token)
            user = UserModel.objects.get(pk=user_id)
            return user, token
        except Exception:
            return
