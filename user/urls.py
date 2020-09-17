from django.urls import path
from .views      import SignUpView
from .views      import LoginView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view())
]
