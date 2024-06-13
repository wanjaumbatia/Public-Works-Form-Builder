from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='/login')
def homepage(request):
    return render(request,'index.html')

urlpatterns = [
    path('', homepage, name='home'),
    path('', include('authentication.urls')),
    path('users/', include('users.urls')),
    
    
    path('admin/', admin.site.urls),
    # Third party apps
    path("api-auth/", include("rest_framework.urls")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration", include("dj_rest_auth.registration.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    
    
    path("", include('forms_builder.urls')),
]
