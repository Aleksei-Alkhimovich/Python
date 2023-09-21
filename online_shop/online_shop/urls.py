from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users import views as userViews
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('registration', userViews.register, name='reg'),
    path('login', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit', authViews.LogoutView.as_view(template_name='main/index.html'), name='exit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
