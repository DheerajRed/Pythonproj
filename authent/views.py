from django.shortcuts import render, redirect, get_object_or_404
from .models import createtask
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import InviteForm
from .models import Invite
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    content = createtask.objects.all()
    if request.method=="POST":
        title = request.POST.get('titletext')
        description = request.POST.get('descriptiontext')
        if title and description:
            createtask.objects.create(Title=title, Description=description)
            return redirect('home')


    context = {
        "tasks":content
    }
    return render( request, 'templates/index.html', context)



def edit(request, task_id):
    task = get_object_or_404(createtask, id=task_id)
    if request.method =="POST":
        title = request.POST.get('titletext')
        description = request.POST.get('descriptiontext')
        if title and description:
            task.Title = title
            task.Description = description
            task.save()
            return redirect('home')

    return render(request, 'templates/edit.html')
            

def Delete(request, task_id):
    task = get_object_or_404(createtask,id=task_id)
    task.delete()

    return redirect('home')


def logout(request):
    logout(request)
    return redirect('home')



@login_required
def invite_user(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save the invite to the database
            invite = Invite.objects.create(sender=request.user, email=email)
            invite_link = f"http://127.0.0.1:8000/register?token={invite.token}"
            print(f" the generate link is {invite_link}")
            
            # Send an email invitation
            send_mail(
                'You are invited!',
                f"Hello! {request.user.username} has invited you to join the Task Manager. Click the link below to join:\nhttp://127.0.0.1:8000/register",
                'admin@taskmanager.com',  # Change this to your project's email
                [email],
                fail_silently=False,
            )
            
            return redirect('home')
    else:
        form = InviteForm()
    
    return render(request, 'templates/profile.html', {'form': form})


def register(request):
    return render(request,'templates/register.html')

@login_required
def profilepage(request):
    return render(request, 'templates/profile.html', {'email':request.user.email})