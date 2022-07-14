from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedBackView.as_view()),
    path('done/', views.DoneView.as_view()),
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
    path('list/', views.ListFeedBackView.as_view()),
    path('list/<id_feedback>', views.DetailFeedBack.as_view(), name='feedback_detail'),
]
