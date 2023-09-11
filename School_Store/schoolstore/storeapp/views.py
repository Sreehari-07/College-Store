from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Department, Course
from .forms import UserInfoForm
from django.http import JsonResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Login action view
def login_action(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new_page')  # Redirect to the new page upon successful login
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return redirect('login')

# User registration view
def register(request):
    departments = Department.objects.all()  # Fetch departments data
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')



    return render(request, "register.html", {'departments': departments})  # Pass departments data to the template

# Login page view
def login_page(request):
    departments = Department.objects.all()  # Fetch departments data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')



    return render(request, "login.html", {'departments': departments})  # Pass departments data to the template


# Logout view
def logout(request):
    auth.logout(request)
    return redirect('/')

# New page view
def new_page(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    return render(request, 'new_page.html', {'departments': departments, 'courses': courses})

# Home view (requires login)
# @login_required
def home(request):
    departments = Department.objects.all()
    courses = Course.objects.all()
    user = request.user  # Get the logged-in user
    return render(request, 'home.html', {'departments': departments, 'courses': courses, 'user': user})

# Course detail view
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})

# Get courses JSON view
def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse({'courses': list(courses)})

def order_now(request):
    # You can add any logic you need here before redirecting
    # For example, checking if the user is eligible to place an order

    return redirect('new_page')