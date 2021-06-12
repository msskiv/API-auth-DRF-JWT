from django.conf.urls import url
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView, authenticate_user

app_name = 'users'
urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^obtain_token/$', authenticate_user, name='obtain_token_api'),
]
