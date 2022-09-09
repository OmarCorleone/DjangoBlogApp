from django.contrib import admin
from django.urls import path
from memory import views
app_name="memory"

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addmemory/",views.addMemory,name="addmemory"),
    path("memory/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.updateMemory,name="update"),
    path("delete/<int:id>",views.deleteMemory,name="delete"),
    path("",views.memories,name="memories"),
    path("comment/<int:id>",views.addComment,name="comment"),
    path("deleteComment/<int:id>",views.deleteComment,name="deleteComment"),



]