from django.conf.urls import url
from my_app import views as ask_views

urlpatterns = [
    # url(r'^question/(?P<question_id>\d+)/$', ask_views.question, name='question'),
    url(r'^$', ask_views.index, name='index'),
]