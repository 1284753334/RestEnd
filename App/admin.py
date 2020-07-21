from django.contrib import admin

from App.models import UserModel, Address


class UserAdmin(admin.ModelAdmin):
    #  添加显示的字段
    list_display = 'u_name','u_password'
#     过滤字段
    list_filter='u_name',
# 搜索字段
    search_fields='u_name',
    #  分页 默认显示20条
    list_per_page = 4
# ordering  排序规则
# fields=(
#     ('班级'{'fields':('sgrade')}),
#     ('姓名'{'fields':('sname')}),
# fields  显示的字段   exclude 不显示的字段
# )



admin.site.register(UserModel,UserAdmin)
admin.site.register(Address)