from django.shortcuts import render

# Create your views here.


rooms = [
    {'id' :1, 'name':'lets go mai'},
    {'id' :2, 'name':'ambogtr'},
    {'id' :3, 'name':"argggggggg"},
]

def main(request):
    return render(request,'main.html')


def navbar(request):
    return render(request,'navbar.html')

def home(request):
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')