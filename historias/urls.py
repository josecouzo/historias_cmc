from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_index, name="home"),
    path('historias/', views.render_historias, name="historias"),
    path('upload-complementario/<int:id_>', views.upload_complementario, name="upload_complementario"),
    path('render_PDF/', views.render_PDF, name="render_PDF"),
    path('historias-ajax/', views.historias_ajax, name="historias_ajax"),
    path('hoja-cargo-ajax/', views.hoja_cargo_ajax, name="hoja_cargo_ajax"),
    path('add-historias/', views.render_add_historia, name="add_historia"),
    path('edit-historia/<int:id_>', views.edit_historia, name="edit_historia"),
    path('add-historia-ajax/', views.ajax_add_historia, name="add_historia_ajax"),
    path('add-consulta-ajax/', views.ajax_add_consulta, name="add_consulta_ajax"),
    path('add-consulta/<int:id_historia>', views.render_add_consulta, name="add_consulta"),
    path('get-operacionesByhistoria/<int:id_>', views.get_operacionesByhistoria, name="get_operacionesByhistoria"),
    path('print_receipt/<int:id_>', views.print_receipt, name="print_receipt"),
    path('print_consulta/<int:id_>', views.print_consulta, name="print_consulta"),
    path('ajax-edit-historia/<int:id_>', views.ajax_edit_historia, name="ajax_edit_historia"),
    path('delete-complementario-ajax/<int:id_>', views.delete_complementario_ajax, name="delete_complementario_ajax"),

]
