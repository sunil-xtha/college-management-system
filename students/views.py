from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib import messages
from .forms import Students

# Create your views here.
def create(request):
    if request.method == 'GET':
        context = {
            'form':StudentForm()
        }
        return render(request,'add_record.html',context)
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            try:
                data.save()
            except:
                messages.add_message(request, messages.ERROR, 'Student Record Already Exits')
                return render(request, 'add_record.html', {'form': form})
            return redirect('home')


def update(request,id):
    student = Students.objects.get(id = id)
    form = StudentForm(request.POST, request.FILES, instance=student)

    if form.is_valid():
        data = form.save()
        data.save()
        return render(request,'index.html')
    else:
        return render(request, 'update_record.html', {'form': form, 'sts':student})

def delete(request, id):
    student = Students.objects.get(id = id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'student': student})



