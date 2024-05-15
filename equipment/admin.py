from django.contrib import admin

from equipment.models import GP, Approve, Contractor, Kait, Worker, Kip


@admin.register(GP)
class AdminGP(admin.ModelAdmin):
    list_display = ['id', 'number']


@admin.register(Approve)
class AdminApprove(admin.ModelAdmin):
    list_display = ['name', 'job_title', ]


@admin.register(Contractor)
class AdminContractor(admin.ModelAdmin):
    list_display = ['name', 'job_title', ]


@admin.register(Kait)
class AdminKait(admin.ModelAdmin):
    list_display = ['name', 'job_title', ]


@admin.register(Worker)
class AdminWorker(admin.ModelAdmin):
    list_display = ['name', 'job_title', ]


@admin.register(Kip)
class AdminKip(admin.ModelAdmin):
    list_display = ['serial_number', 'id', 'defective_act', 'date_of_detection', 'letter_to_INVEST', 'date_at']
    list_filter = ['poz_GP', 'date_at']
    search_fields = ['serial_number', 'date_at']
