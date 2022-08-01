from django.contrib import admin
from django.urls import path
from Entregable1.views import first_template
urlpatterns = [
    path('admin/', admin.site.urls),
    path("familiares/", first_template),
]
