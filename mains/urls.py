from django.urls import path

from . import views

#Must   : urlpattern(string), view.py function
#NotMust: kwargs (to target view), name (For unambiguously refer Templates)
app_name = 'mains'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]