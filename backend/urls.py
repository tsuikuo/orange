from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<code>[0-9]+)/annual_report$', views.annual_report, name='annual_report'),
    url(r'^stock_list$', views.stock_list, name='stock_list'),
    url(r'^(?P<code>[0-9]+)/tick_data$', views.tick_data, name='tick_data'),
    url(r'^(?P<code>[0-9]+)/basic_info$', views.basic_info, name='basic_info'),
    url(r'^(?P<code>[0-9]+)/level_0$', views.level_0, name='level_0'),
    url(r'^(?P<code>[0-9]+)/level_1$', views.level_1, name='level_1'),
]
