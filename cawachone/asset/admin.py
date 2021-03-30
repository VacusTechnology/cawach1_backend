from django.contrib import admin

# Register your models here.
from asset.models import Asset, AssetHealth

admin.site.register(Asset)
admin.site.register(AssetHealth)