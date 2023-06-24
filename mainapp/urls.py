from django.urls import path

from . import views

urlpatterns = [
    path('create-user/', views.create_user, name="create_user"),
    path('create_user_super/', views.create_user_super, name="create_user_super"),
    path('render-usuarios/', views.render_usuarios, name="render_usuarios"),

]
