from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'^$' ,views.allurls , name = 'urls' ) ,
  url('list' , views.listall , name = 'list'),
  url('update_task/<int:id>' , views.updatetask , name = 'update'),
  url('createTask' , views.createTask , name = "create"),
  url('task_detail/<int:id>' , views.taskDetail , name= 'detail'),
  url('delete_task/<int:id>' , views.deleteTask , name = 'delete'),

]
