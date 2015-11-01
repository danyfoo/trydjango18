from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]  #Campos que se desplegaran al momento de ver la app desde el admin
    form = SignUpForm   #Formulario que se utilizara para anadir a la DB
    #class Meta:
    #    model = SignUp

admin.site.register(SignUp, SignUpAdmin)