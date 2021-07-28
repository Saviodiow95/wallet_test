from django.contrib import admin
from financial.models import Wallet, Asset, Application, Rescue

admin.site.register(Wallet)
admin.site.register(Asset)
admin.site.register(Application)
admin.site.register(Rescue)
