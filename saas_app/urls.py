from django.urls import path
from .views import RegisterView, EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
