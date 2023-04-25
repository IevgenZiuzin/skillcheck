from django.urls import re_path, include

urlpatterns = [
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.authtoken'))
]
