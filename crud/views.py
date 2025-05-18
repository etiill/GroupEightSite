from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Genders

# Create your views here.

def gender_list(request):
    try:
        genders = Genders.objects.all() # SELECT * FROM tbl_genders

        data = {
            'genders':genders
        }

        return render(request, 'gender/GendersList.html', data)
    except Exception as e:
        return HttpResponse(f'Error occurred during load genders: {e}')

def add_gender(request):
    try:
        if request.method == 'POST':
            gender = request.POST.get('gender')

            Genders.objects.create(gender=gender).save()
            messages.success(request, 'Gender added successfully!')
            return redirect('/gender/list')
        else:
            return render(request, 'gender/AddGender.html')
    except Exception as e:
        return HttpResponse(f'Error occurred during add gender: {e}')
    
def edit_gender(request, genderId):
        try:
            if request.method == 'POST':
                genderObj = Genders.objects.get(pk=genderId)

                gender = request.POST.get('gender')

                genderObj.gender = gender
                genderObj.save() # UPDATE 

                messages.success(request, 'Gender Updated Successfully!')

                data = {
                'gender': genderObj
            }
                return render(request, 'gender/EditGender.html', data)
            else:
                genderObj = Genders.objects.get(pk=genderId)

            data = {
                'gender': genderObj
            }

            return render(request, 'gender/EditGender.html', data)
        except Exception as e:
            return HttpResponse(f'Error occurred during edit gender: {e}')

def delete_gender(request, genderId):
    try:
        if request.method == 'POST':
            genderObj = Genders.objects.get(pk=genderId)
            genderObj.delete()

            messages.success(request, 'Gender deleted successfully!')
            return redirect('/gender/list')
        else:
            genderObj = Genders.objects.get(pk=genderId)
        
            data ={
                'gender': genderObj
            }

            return render(request, 'gender/DeleteGender.html', data)
    except Exception as e:
            return HttpResponse(f'Error occurred during delete gender: {e}')
