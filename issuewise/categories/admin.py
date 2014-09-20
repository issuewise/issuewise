from django.contrib import admin
from categories.models.wisecategories import PublicCategory, GroupCategory

admin.site.register(PublicCategory)
admin.site.register(GroupCategory)
