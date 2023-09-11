from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),  # Handles GET requests for the login page
    path('login/action/', views.login_action, name='login_action'),  # Handles POST requests for the login action
    path('logout/',views.logout,name='logout'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    # path('get_courses/<int:department_id>/', views.get_courses, name='get_courses'),
    path('get_courses', views.get_courses, name='get_courses'),
    path('order_now/', views.order_now, name='order_now'),

]
