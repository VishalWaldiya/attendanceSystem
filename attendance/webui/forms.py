from django import forms
from .models import TransactionPermanent, MemberList ,MemberType, Center, GENDER_TYPE

GEEKS_CHOICES = MemberList.objects.values_list('id','id')

class TransactionPermanentForm(forms.Form):
    ID = forms.ChoiceField(
        choices = GEEKS_CHOICES,
        # queryset = MemberList.objects.values_list('id','id'),
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