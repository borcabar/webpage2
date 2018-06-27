from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

'''
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]
'''