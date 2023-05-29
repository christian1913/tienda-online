from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , include('backend.urls')),
    path('' , include('frontend.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'),name="logout"),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)