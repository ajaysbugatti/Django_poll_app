from django.contrib import admin
from django.urls import path,include
from . import views

app_name='poll'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


'''urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
   # path('<int:a>/',views.hanu)
]
'''