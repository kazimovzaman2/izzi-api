from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Tasker)
admin.site.register(TaskerSkills)
admin.site.register(TaskerCertificate)
admin.site.register(City)

admin.site.register(Blog)

admin.site.register(Customer)

admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(ServiceBook)

admin.site.register(Order)