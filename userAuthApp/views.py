from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, logout, login

# Username and Password for test user:-
# username = Yash, password = yash@****@1234

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "home.html")
    # return HttpResponse("This is home page")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

         # If authentication is successful
        if user is not None:
            login(request, user)
            return redirect('/')

        # If authentication is failed
        else:
            return redirect('/login')
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')        
