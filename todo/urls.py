from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^savetodo/$', views.save_todo, name='save_todo'),
  url(r'^deletetodo/$', views.delete_todo, name='delete_todo'),
  url(r'^completetodo/$', views.complete_todo, name='complete_todo'),
  url(r'^edit/(?P<todo_id>[0-9]+)/$', views.edit_todo, name='edit_todo'),
  url(r'^not-found/$', views.not_found, name='not_found')
]