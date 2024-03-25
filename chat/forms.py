from django import forms

from .models import ChatRoom


class CreateChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'topic']