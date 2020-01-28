from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.http import HttpResponseRedirect

from posts.views import index, blog, post, search,post_create, post_update, post_delete, company, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('contact/', contact, name='contact_us'),
    path('search/', search, name='search'),
    path('create/', post, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('company/', company, name='company_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
