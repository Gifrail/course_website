from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Course, Purchase

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    purchased = False
    if request.user.is_authenticated:
        purchased = Purchase.objects.filter(user=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {'course': course, 'purchased': purchased})

@login_required
def purchase_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    # Простейшая логика покупки
    Purchase.objects.get_or_create(user=request.user, course=course)
    return redirect('course_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})
