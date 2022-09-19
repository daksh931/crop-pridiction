from django.shortcuts import render 
import joblib
import pandas as pd
from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout


mp = joblib.load('./models/modelpickle')
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'index.html')
    # return HttpResponse(" This is Homepage")

def services(request):
    return render(request, 'services.html')
    
def form(request):
    return render(request, 'form.html')

def dataset(request):
    return render(request, 'dataset.html')

def model(request):
    return render(request, 'model.html')


# -------------> Sign UP
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')



def predict(request):
    print(request)  
    if request.method == "POST":
        print("Hello ----- world Hello world ")
        temp = {}
        temp['N']=request.POST.get('N')
        temp['P']=request.POST.get('P')
        temp['K']=request.POST.get('K')
        temp['temperature']=request.POST.get('temperature')
        temp['humidity']=request.POST.get('humidity')
        temp['ph']=request.POST.get('ph')
        temp['rainfall']=request.POST.get('rainfall')
        

    testdf = pd.DataFrame({'X':temp}).transpose()
    predictedCrop = mp.predict(testdf.values)[0]
    print(predictedCrop)
    context = {'PredictedCrop':predictedCrop}
    return render(request, 'form.html',context)