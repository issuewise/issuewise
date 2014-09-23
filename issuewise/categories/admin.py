from django.contrib import admin
from categories.models.wisecategories import WisePublicCategory, WiseGroupCategory

admin.site.register(WisePublicCategory)
admin.site.register(WiseGroupCategory)
