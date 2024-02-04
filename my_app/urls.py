from django.urls import path
from . import views

urlpatterns = [
    path('fines/', views.update_fines, name='fines'),
    path('books/', views.BookView.as_view()),
    path('transactions/', views.TransactionView.as_view()),
    path('return_a_book/<str:pk>', views.return_a_book, name='return')
]