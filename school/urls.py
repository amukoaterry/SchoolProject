
from django.contrib import admin
from django.urls import path
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('student/',include("student.urls")),
    path('accounts/', include('accounts.urls')),
    path('homepage/', include('homepage.urls')),

]





