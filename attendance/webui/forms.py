from django import forms
from .models import Transaction, Member ,MemberType, Center, GENDER_TYPE, SecurityPost

GEEKS_CHOICES = Member.objects.values_list('id','id')

class TransactionForm(forms.Form):
    ID = forms.ModelChoiceField(
        # choices = GEEKS_CHOICES,
        queryset = Member.objects.values_list('id'),
        label = 'Select or Search #',
        widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Name", 
                                        "class": "ui " })
    )

    MemberType = forms.ModelChoiceField(
        queryset=MemberType.objects.all(),
        widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
        )

    CenterDetails = forms.ModelChoiceField(
        queryset=Center.objects.all(),
        widget=forms.Select(attrs={"_style": "search", "_dropdown_icon": "dropdown"})
    )

    FatherName = forms.CharField(
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Father Name", 
                                        "class": "ui " })
    )

    Gender = forms.ChoiceField(
        choices=GENDER_TYPE,
        widget=forms.Select(attrs={"_dropdown_icon": "dropdown"})
    )

    Contact = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Contact Number", 
                                        "class": "ui " })
    )

    AlternateContact = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
                                        "Placeholder": "Alternate Contact Number", 
                                        "class": "ui " })
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