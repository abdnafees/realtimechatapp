from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateChatRoomForm
from .models import ChatRoom


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

@login_required
def all_chatrooms_view(request):
    chat_rooms = ChatRoom.objects.all()  # Assumes you have a ChatRoom model
    context = {'chat_rooms': chat_rooms}
    return render(request, 'chat/chatrooms.html', context)

def chatroom_view(request, pk):
    chatroom = get_object_or_404(ChatRoom, pk=pk)
    messages = chatroom.chatmessage_set.all()
    context = {'chatroom': chatroom, 'messages': messages}
    return render(request, 'chat/chatroom.html', context)

def create_chatroom(request):
    if request.method == 'POST':
        form = CreateChatRoomForm(request.POST)
        if form.is_valid():
            chatroom = form.save(commit=False)
            chatroom.owner = request.user
            chatroom.save() 
            chatroom.users.add(request.user)
            return redirect('chatroom', name=chatroom.name)
    else:
        form = CreateChatRoomForm()
    return render(request, 'chat/create_chatroom.html', {'form': form})