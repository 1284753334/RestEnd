from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^users/$', views.UsersAPIView.as_view()),
    # 获取单个对象详情的url
    url(r'^user/(?P<pk>\d+)/$', views.UserAPIView.as_view(),name ='usermodel-detail'),
    url(r'^address/', views.AddressAPIView.as_view(
        {'post': 'create',
         'get':'list',

         }
    )),
    #  获取单个对象的路由  参数 pk 为小写
    url(r'^address/(?P<pk>\d+)/$', views.AddressAPIView.as_view(
{'get': 'retrieve',

         }
    ),name='address-detail'),
]
