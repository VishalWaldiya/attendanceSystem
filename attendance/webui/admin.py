from django.contrib import admin
from webui.models import (  MemberType, Member, Center, SecurityPost,
                            Transaction, MiscContact )
# Register your models here.
admin.site.register(MemberType)
admin.site.register(MiscContact)
admin.site.register(Center)
admin.site.register(SecurityPost)
admin.site.register(Transaction)

class MemberAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name' ]
    list_display = ['id', 'name' , 'MemberTypeDetails','CenterDetails' ]

admin.site.register(Member,MemberAdmin)
