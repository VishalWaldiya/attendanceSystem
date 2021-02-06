from django import forms
from django.contrib.admin import widgets                                       
from .models import Transaction, Member ,MemberType, Center, GENDER_TYPE, SecurityPost
from django.core.exceptions import ValidationError
import re

GEEKS_CHOICES = Member.objects.values_list('id','id')

def validate_alt_contact(value):
    return re.search(r'd{10}$', value)


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         # fields = '__all__'
#         exclude = ['status', 'misc']
#         widgets = {
#             'inTime': DateInput(),
#         }


    # def __init__(self, *args, **kwargs):
    #     super(TransactionForm, self).__init__(*args, **kwargs)
    #     # self.fields['username'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter Username'})
    #     # self.fields['email'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter email'})
    #     # self.fields['keywords'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter Key words'})
    #     # self.fields['search_frequency'].widget.attrs.update({'class' : 'ui input','placeholder':'In Hours'})
    #     self.fields['inTime'].widget.attrs.update({'class' : 'ui calender'})
    #     self.fields['outtime'].widget.attrs.update({'type' : 'datetime-local'})


class TransactionForm(forms.Form):
    ID = forms.ChoiceField(
        choices = GEEKS_CHOICES,
        # queryset = Member.objects.all().values('id'),
        label = 'Select or Search #',
        widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Name", 
                                        "class": "ui " })
    )

    # MemberType = forms.ModelChoiceField(
    #     queryset=MemberType.objects.all(),
    #     widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
    #     )

    # CenterDetails = forms.ModelChoiceField(
    #     queryset=Center.objects.all(),
    #     widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
    # )

    FatherName = forms.CharField(
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Father Name", 
                                        "class": "ui " })
    )

    # Gender = forms.ChoiceField(
    #     choices=GENDER_TYPE,
    #     widget=forms.Select(attrs={"_dropdown_icon": "dropdown"})
    # )

    Contact = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Contact Number", 
                                        "class": "ui " })
    )

    AlternateContact = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Alternate Contact Number", 
                                        "class": "ui " }),
        validators=[validate_alt_contact],
        help = "Enter 10 Digits"
    )

    Department = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Department", 
                                        "class": "ui " })
    )

    SecurityPost = forms.ModelChoiceField(
        queryset=SecurityPost.objects.all(),
        widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
        )
    

    # inTime = forms.DateTimeField(input_formats=['%Y-%m-%d %I:%M'], widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # outTime = forms.DateTimeField(input_formats=['%Y-%m-%d %I:%M'], required=False, widget=forms.DateInput(attrs={'type':'datetime-local'}))

    inTime = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y')) 


    outime = forms.DateTimeField(input_formats=['%I:%M %p %d-%b-%Y'],
             widget = forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y')) 
