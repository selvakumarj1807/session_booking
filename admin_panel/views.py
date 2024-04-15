import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from .forms import SessionForm, CustomUserForm
from admin_panel.models import CustomUser, Session

logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                logger.info(f"Superuser {username} logged in successfully.")
                return render(request, 'admin_templates/admin.html')
            else:
                logger.info(f"User {username} logged in successfully.")
                return render(request, 'adminlogin.html')
        else:
            logger.error(f"Failed login attempt for user {username}.")
            return render(request, 'adminlogin.html', {'error_message': 'Invalid username or password'})

    return render(request, 'adminlogin.html')

def create_user(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # Process the form data and save to the database
            form.save()
           # return redirect('success_url')  # Redirect to a success URL
    else:
        form = CustomUserForm()
    
    return render(request, 'admin_templates/create_user.html',{'users': users, 'form': form})

def user_edit(request, id):
    user = get_object_or_404(CustomUser, id=id)  # Get the CustomUser instance or return a 404 if not found
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)  # Populate the form with the user instance
        if form.is_valid():
            form.save()  # Save the updated user data
            return redirect('create_user')  # Redirect to a success URL after editing
    else:
        form = CustomUserForm(instance=user)  # Create the form with the user instance
    
    return render(request, 'admin_templates/user_edit.html', {'form': form, 'user': user})

def user_destroy(request, id): 
    user = CustomUser.objects.get(id=id) 
    user.delete() 
    return redirect("create_user") 

def create_session(request):
    more_session = Session.objects.all()
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            # Process the form data and save to the database
            form.save()
            #return redirect('success_url')  # Redirect to a success URL
    else:
        form = SessionForm()
    
    return render(request, 'admin_templates/create_session.html', {'more_session': more_session,'form': form})


def session_edit(request, id):
    session = get_object_or_404(Session, id=id)  # Get the CustomUser instance or return a 404 if not found
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)  # Populate the form with the user instance
        if form.is_valid():
            form.save()  # Save the updated user data
            return redirect('create_session')  # Redirect to a success URL after editing
    else:
        form = SessionForm(instance=session)  # Create the form with the user instance
    
    return render(request, 'admin_templates/session_edit.html', {'form': form, 'session': session})

def session_delete(request, id): 
    user = Session.objects.get(id=id) 
    user.delete() 
    return redirect("create_session")