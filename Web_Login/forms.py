from django.forms import ModelForm
from Web_Login.models import User, Profile
from Web_Main.models import Item

from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('firstname','lastname','address', 'postcode', 'phone')

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

class ToolListForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'description', 'price', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5')