from django.shortcuts import render

# Create your views here.


rooms = [
    {'id' :1, 'name':'Lets learn python!'},
    {'id' :2, 'name':'Design with me'},
    {'id' :3, 'name':"Frontend developer"},
]

BEDrooms = [ 
    {'id':1,'name':'home one'},
    {'id':2,'name':'bathroome'},
    {'id':3,'name':'aliona'},
]

def hotel(request ):
    context = {'BEDrooms': BEDrooms}
    return render(request, 'base/hotel.html', context)

def hotelroom(request, pk):
    hotelroom = None
    for i in BEDrooms:
        if i['id'] == int(pk):
            hotelroom = i
    context = {'hotelroom': hotelroom}
    return render(request , 'base/hotelroom.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def main(request):
    return render(request,'main.html')


def navbar(request):
    return render(request,'navbar.html')

def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)