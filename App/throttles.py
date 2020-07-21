#  节流

from rest_framework.throttling import SimpleRateThrottle

#  访问时  报错 'UserModel' object has no attribute 'is_authenticated'
#  自定义方法 解决次问题 Alt+ Enter 载入抽样方法
from App.models import UserModel

#  用户节流代码
class UserThrottle(SimpleRateThrottle):
    #  从原码中拿代码，修改成我们想要的
    scope = 'user'
    #  request ,view 参数可以指定哪种请求方式（post,get） 还有哪个接口
    def get_cache_key(self, request, view):
        # 当前用户是UserModel  则已登录
        if isinstance(request.user,UserModel):
            #  auth 为内置的函数，非自定义
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

#  Address 节流代码
class AddressThrottle(SimpleRateThrottle):
    #  从原码中拿代码，修改成我们想要的
    scope = 'addr'
    #  request ,view 参数可以指定哪种请求方式（post,get） 还有哪个接口
    def get_cache_key(self, request, view):
        # 当前用户是UserModel  则已登录
        if isinstance(request.user,UserModel):
            #  auth 为内置的函数，非自定义
            ident = request.auth
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }





