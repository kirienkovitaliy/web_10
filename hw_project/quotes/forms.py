from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput


class AuthorForm(UserCreationForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput(attrs={"class": "form-control"}))
    date_born = CharField(max_length=50, required=False, widget=TextInput(attrs={"class": "form-control"}))
    location_born = CharField(max_length=150, required=False, widget=TextInput(attrs={"class": "form-control"}))
    bio = CharField(max_length=1500, required=False, widget=TextInput(attrs={"class": "form-control"}))
    quotes = CharField(max_length=1500, required=False, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("fullname", "date_born", "location_born", "bio",
                  "quotes")


class QuoteForm(UserCreationForm):
    name = CharField(max_length=50, required=False, widget=TextInput(attrs={"class": "form-control"}))
    quote = CharField(max_length=1500, required=True, widget=TextInput(attrs={"class": "form-control"}))
    tag = CharField(max_length=100, required=False, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("name", "quote", "tag")
