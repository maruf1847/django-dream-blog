from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (index, blog, post_detail,
                         search, post_create,
                         post_update, post_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('post/<int:id>/', post_detail, name='post-detail'),
    path('post/<int:id>/update/', post_update, name='post-update'),
    path('post/<int:id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
