from django.contrib import admin

from sendemail.models import Student, Grade

#  定制站点信息 例如按钮之类的  继承adminsite 后所有的东西都需要改成自己的
class MyAdminSite(admin.AdminSite):
    #  更改tittle
    site_title = '个人中心'
    site_header = '管理中心'
    site_url = "/send/home"

# 创建一个对象 将所有注册  的admin 改成 创建的
site = MyAdminSite()

#  实现插入班级 时 插入学生信息
class StudentInfo(admin.TabularInline):
    extra = 3
    model = Student

#  创建类，显示字段 搜索 等功能
class GradeAdmin(admin.ModelAdmin):
    list_display = 'g_name', 'g_position',
    search_fields = 'g_name',
    inlines = [StudentInfo]

 #  注册模型，继承各自admin,实现 显示字段 等
#   定制站点信息 需要更给下面的代码为我们设置的
# admin.site.register(Grade, GradeAdmin)
site.register(Grade, GradeAdmin)

class StudentAdmin(admin.ModelAdmin):
    search_fields = 's_name',

    #  定义函数，修改后台默认的字段
    def sex(self):
        if self.s_sex:
            return '女'
        else:
            return '男'

    list_display = ('s_name', 's_age', sex)
    sex.short_description = '性别'
    #  分组显示
    fieldsets = (
        ('基本信息', {'fields': ('s_name', 's_age', 's_sex')}),
        ('可选信息', {'fields': ('s_height', 's_weight')}),

)

 #  注册模型，继承各自admin,实现 显示字段 等
#   定制站点信息 需要更给下面的代码为我们设置的
# admin.site.register(Student, StudentAdmin)
site.register(Student, StudentAdmin)








