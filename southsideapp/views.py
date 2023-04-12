from django.shortcuts import render, redirect
from . models import QAAudit
from django.contrib.auth.models import User
from . forms import QA_Forms, User_Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . decorators import allowed_users, Manager_only ,unauthenticated_user

# Create your views here.

#@login_required(login_url='LoginPage')
#@Manager_only
def Home(request):
    TheAudits = QAAudit.objects.all()
    return render(request, 'Home.html',
                  {'TheAudits':TheAudits})


#@login_required(login_url='LoginPage')
def Audit_form(request):
    The_form = QA_Forms
    if request.method == 'POST':
        The_form = QA_Forms(request.POST)
        if The_form.is_valid():
            The_form.save()
            return redirect('Home')
    return render(request, 'Audit_form.html',
                  {'The_form':The_form})

#@login_required(login_url='LoginPage')
def QA_Audit_Edit(request, audit_id):
    The_Audits_edit = QAAudit.objects.get(pk=audit_id)
    The_form_edit = QA_Forms(request.POST or None, instance=The_Audits_edit)
    if request.method == 'POST':
        if The_form_edit.is_valid():
            The_form_edit.save()
    return render(request, 'QA_Audit_Edit.html',
                  {'The_Audits_edit':The_Audits_edit,
                   'The_form_edit':The_form_edit})

#@login_required(login_url='LoginPage')
def QA_Audit_details(request, audit_id):
    TheAuditsEdit = QAAudit.objects.get(pk=audit_id)
    return render(request, 'QA_Audit_details.html',
                  {'TheAuditsEdit':TheAuditsEdit})

#@unauthenticated_user
'''def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Please try again, your password is wrong!")
    return render(request, 'Login.html')
''''''
def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')'''

#@unauthenticated_user
def Register(request):
    TheRegisterForm = User_Register
    if request.method == 'POST':
        TheRegisterForm = User_Register(request.POST)
        if TheRegisterForm.is_valid():
            TheRegisterForm.save() 
            messages.success(request, "User has been added to SouthSide!")
            return redirect('LoginPage')
    return render(request, 'Register.html',
                  {'TheRegisterForm':TheRegisterForm})


#@login_required(login_url='LoginPage')
#@Manager_only
def TheUser(request):
    Agents_work = request.user
    work = QAAudit.objects.filter(QA_Audit=Agents_work)
    return render(request, 'TheUser.html',
                  {'work':work})