from  django.shortcuts import   render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from meetup.models import Room, Message

def home(request):
    return render(request,'home.html')
def home1(request):
    return render(request,'home1.html')
def home2(request):
    return render(request,'home2.html')
def home3(request):
    return render(request,'home3.html')


def index(request):
    return render(request,'homepage.html')
@csrf_protect
def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name',False)
        last_name=request.POST.get('last_name',False)
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')

            else:
                user=User.objects.create_user(last_name=last_name,first_name=first_name,username=username,password=password1,email=email)
                user.save();
                print('user created ')
                return redirect('login')
               
        else:
            messages.info(request,'Password not matching')

        return redirect('/')
    else:
        return render(request,'signup.html')
def login(request):
    if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']

         user=auth.authenticate(username=username,password=password)
         if user is not None:
             auth.login(request,user)
             context={'user':username}
             return render(request,"dashboard.html ",context)
         else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')




def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
        
    return render(request, 'room.html', {
            'username': username,
            'room': room,
            'room_details': room_details
        })
   

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

