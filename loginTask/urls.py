from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirige a login
]