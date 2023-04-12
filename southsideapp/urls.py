from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),
    path('Audit_form/', views.Audit_form, name='Audit_form'),
    path('QA_Audit_details/<int:audit_id>', views.QA_Audit_details, name='QA_Audit_details'),
    path('QA_Audit_Edit/<int:audit_id>', views.QA_Audit_Edit, name='QA_Audit_Edit'),
    #path('Login/', views.LoginPage, name='LoginPage'),
    #path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
    path('Register/', views.Register, name='Register'),
    path('TheUser/', views.TheUser, name='TheUser'),

]