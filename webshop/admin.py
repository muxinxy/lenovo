from django.contrib import admin

# Register your models here.
from .models import Commodity
admin.site.register(Commodity)
from .models import Thumb
admin.site.register(Thumb)
from .models import Option
admin.site.register(Option)
