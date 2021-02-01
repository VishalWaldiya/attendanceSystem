from django.contrib import admin
from webui.models import (  MemberType, MemberList, Center, SecurityPost,
                            TransactionPermanent )
# Register your models here.
admin.site.register(MemberType)
# admin.site.register(MemberList)
admin.site.register(Center)
admin.site.register(SecurityPost)
admin.site.register(TransactionPermanent)

class MemberListAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name' ]
    list_display = ['id', 'name' , 'MemberTypeDetails','CenterDetails' ]

admin.site.register(MemberList,MemberListAdmin)
