from django.urls import path, include, reverse_lazy, re_path
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    re_path(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    re_path(r'^done/$', password_reset_done, name='password_reset_done'),
    re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    re_path(r'^complete/$', password_reset_complete, name='password_reset_complete'),
]
