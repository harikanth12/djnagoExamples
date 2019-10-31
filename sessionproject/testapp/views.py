from django.shortcuts import render
from testapp.forms import additemsForm

# Create your views here.

def additems(request):
    form = additemsForm()
    return render(request,'additems.html',{'form':form})

def displayitems(request):
    # item = request.session.get('items')

    return render(request,'displayitems.html')

def success(request):
    itemname = request.GET['ItemName']
    itemquantity = request.GET['ItemQuantity']
    # dict1 = {'name':itemname,'quantity':itemquantity}
    # item_name_exits = request.session.get(itemname)
    # item_
    # request.session['itemname']=itemname
    # request.session['itemquantity']=itemquantity
    item_get = int(request.session.get(itemname,0))
    request.session[itemname] = item_get+int(itemquantity)
    return render(request,'success.html')
