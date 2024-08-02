from django.contrib import admin
from django.urls import path, include
from ballers085.views import first_page
from django.conf.urls import handler404
from django.shortcuts import render 
from ballers085.views import CustomLoginView
from .settings import DEBUG

def custom_404(request, exception):
    return render(request, '404.html', status=404)

if DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', first_page, name='first_page'),
        path('ballers085/', include('ballers085.urls')),
        path('accounts/login/', CustomLoginView.as_view(), name='login'),
        path('accounts/', include('django.contrib.auth.urls'))
    ]
else:
    urlpatterns = [
        path('', first_page, name='first_page'),
        path('ballers085/', include('ballers085.urls')),
        path('accounts/login/', CustomLoginView.as_view(), name='login'),
        path('accounts/', include('django.contrib.auth.urls'))
    ]
handler404 = custom_404
