from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ: List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentmngs/student_list.html', {'students': students})

# CREATE: Add a new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'studentmngs/student_form.html', {'form': form, 'title': 'Add Student'})

# UPDATE: Edit student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentmngs/student_form.html', {'form': form, 'title': 'Edit Student'})

# DELETE: Remove student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'studentmngs/student_confirm_delete.html', {'student': student})
