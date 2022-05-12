from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CartItem
from .models import Arma
from .models import Monicao

admin.site.register(CartItem)
admin.site.register(Arma)
admin.site.register(Monicao)
