from django.urls import path,re_path
from boards import views


urlpatterns = [

    re_path(r'^$',views.home,name='home'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.board_topics,name='board_topics'),

]

