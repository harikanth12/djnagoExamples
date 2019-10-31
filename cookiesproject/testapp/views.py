from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    count = int(request.COOKIES.get('count',0))
    newcount= count +1
    response = render(request,'count.html',{'count':newcount})
    # return render(request,'count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response

def Namecookie(request):
    if request.method == "POST":
        uname = request.POST['uname']
        res = redirect(ageCookie)
        res.set_cookie('uname',uname)
        return res
    return render(request,'cookes.html')

def ageCookie(request):
    uname = request.COOKIES.get('uname')
    if request.method == "POST":
        age = request.POST['age']
        res = redirect(gfcookies)
        res.set_cookie('age',age)
        return res
    return render(request,'age.html',{'uname':uname})
        
def gfcookies(request):
    uname = request.COOKIES.get('uname')
    if request.method == "POST":
        gfname = request.POST['gfname']
        res = redirect(success)
        res.set_cookie('gfname',gfname)
        return res
    return render(request,'gfname.html',{'uname':uname})

def success(request):
    uname = request.COOKIES.get('uname')
    age = request.COOKIES.get('age')
    gfname = request.COOKIES.get('gfname')
    return render(request,'success.html',{'uname':uname,'age':age,'gfname':gfname})
    
def home(request):
    uname = request.GET['age']
    return render(request,'home.html',{'name':uname})