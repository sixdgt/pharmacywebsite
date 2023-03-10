from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import MedicineCreateForm, CategoryCreateForm
from .models import Medicine, Category
from django.contrib import messages

# Create your views here.
@login_required(login_url='/authentication/login')
def category_create(request):
    create_form = CategoryCreateForm()
    context = {"form": create_form}
    if request.method == "POST":
        form_obj = CategoryCreateForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            messages.success(request, 'Category added successfully')
            return redirect("medicines")
        messages.error(request, 'Something went wrong')
    return render(request, 'categories/add_category.html', context)

@login_required(login_url='/authentication/login')
def medicine_index(request):
    data = Medicine.objects.all()
    context = {"data": data}
    return render(request, 'medicines/index.html', context)

@login_required(login_url='/authentication/login')
def medicine_edit(request, id):
    data = Medicine.objects.get(id=id)
    context = {"data": data}
    return render(request, "medicines/edit_medicine.html", context)

@login_required(login_url='/authentication/login')
def medicine_update(request):
    if request.method == "POST":
        data = Medicine.objects.get(id=request.POST.get('id'))
        data.name = request.POST.get('name')
        data.description = request.POST.get('description')
        data.expiry_date = request.POST.get('expiry_date')
        data.mg = request.POST.get('mg')
        data.price = request.POST.get('price')
        data.quantity = request.POST.get('quantity')
        data.save()
        messages.success(request, 'Updated successfully')
        return redirect('medicines')
    return redirect('medicines')

@login_required(login_url='/authentication/login')
def medicine_show(request, id):
    data = Medicine.objects.get(id=id)
    context = {"data": data}
    return render(request, "medicines/show_medicine.html", context)

@login_required(login_url='/authentication/login')
def medicine_delete(request, id):
    data = Medicine.objects.get(id=id)
    data.delete()
    messages.success(request, 'Deleted successfully')
    return redirect("medicines")

@login_required(login_url='/authentication/login')
def medicine_create(request):
    create_form = MedicineCreateForm()
    context = {"form": create_form}

    if request.method == "POST":
        category = Category.objects.get(id=request.POST.get('category'))
        medicine_obj = Medicine()
        medicine_obj.name = request.POST.get('name')
        medicine_obj.description = request.POST.get('description')
        medicine_obj.price = request.POST.get('price')
        medicine_obj.expiry_date = request.POST.get('expiry_date')
        medicine_obj.mg = request.POST.get('mg')
        medicine_obj.quantity = request.POST.get('quantity')
        medicine_obj.category = category
        medicine_obj.user = request.user
        medicine_obj.save()
        messages.success(request, 'Added successfully')
        return redirect("add-medicine")
    return render(request, 'medicines/add_medicine.html', context)