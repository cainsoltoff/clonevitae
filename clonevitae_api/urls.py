from django.urls import path
from . import views

urlpatterns = [
    path('get_autocomplete_options/', views.get_autocomplete_options, name='get_autcomplete'),
    path('get_entries_for_gene/', views.get_entries_for_gene, name='get_entries_for_gene')
]