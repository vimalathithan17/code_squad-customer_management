from django.shortcuts import redirect, render
from .forms import CustomerProfileForm,CustomerCreationForm,TravelHistoryForm
from django.contrib import messages
from .models import Customer,CustomerProfile,TravelHistory
from django.contrib.auth.decorators import login_required
current_customer=None
# Create your views here.
@login_required
def select(request):
    return render ( request, 'detail_management/select.html' )
@login_required
def to_view_customer(request):
    profile=CustomerProfile.objects.get(customer=current_customer)
    result=TravelHistory.objects.all().filter(customer=current_customer)
    return render(request,'detail_management/main.html',{'customer':Customer.objects.get(customer_id=current_customer),'profile':profile,'result':result})
@login_required
def create_customer(request):
    if request.method=='POST':
        customer_form=CustomerCreationForm(request.POST)
        if(customer_form.is_valid()):
            customer_form.save()   
            messages.success(request,'customer created sucessfully')
            global current_customer
            current_customer=request.POST['customer_id']
            return redirect('create_profile')
        
        else:
            return render(request,'detail_management/customer_creation.html',{'form':customer_form})
    else :
        customer_form=CustomerCreationForm()
    return render(request,'detail_management/customer_creation.html',{'form':customer_form})
@login_required
def create_profile(request):
    if request.method=='POST':
        profile_form=CustomerProfileForm(request.POST,request.FILES) 
        if(profile_form.is_valid()):
            profile_form.save()
            messages.success(request,'customer profile created sucessfully')
            return redirect('to_view_customer')
        else:
            return render(request,'detail_management/profile.html',{'form':profile_form})
    else :
        profile_form=CustomerProfileForm()
    return render(request,'detail_management/profile.html',{'form':profile_form})
@login_required
def update_profile(request):
    if request.method=='POST':
        CustomerProfile.objects.get(customer=current_customer).delete()
        profile_form=CustomerProfileForm(request.POST,request.FILES) 
        if(profile_form.is_valid()):
            
            profile_form.save()
            messages.success(request,'customer profile updated sucessfully')
            print('hi')
            return redirect('to_view_customer')
        else:
            return render(request,'detail_management/profile.html',{'form':profile_form})
    else :
        print("ccc",current_customer)
        profile=CustomerProfile.objects.get(customer=current_customer)
        print(profile)
        profile_form=CustomerProfileForm(instance=profile)
    return render(request,'detail_management/profile.html',{'form':profile_form})

@login_required
def view_customer(request):
    if request.method=='POST':
        print('hi',request.POST)
        global current_customer
        current_customer=request.POST['customer_id']
        print(current_customer)
        profile=CustomerProfile.objects.get(customer=current_customer)
        result=TravelHistory.objects.all().filter(customer=current_customer)
        return render(request,'detail_management/main.html',{'customer':Customer.objects.get(customer_id=current_customer),'profile':profile,'result':result})
    else:
        return render(request,'detail_management/select_customer.html')
@login_required
def add_travel(request):
    if request.method=='POST':
        add_travel_form=TravelHistoryForm(request.POST)
        if(add_travel_form.is_valid()):
            add_travel_form.save()
            return redirect('to_view_customer')
    else:
        add_travel_form=TravelHistoryForm({'customer':current_customer})
        return render(request,'detail_management/add_travel.html',{'form':add_travel_form})
