from django import forms
from .models import TransactionPermanent, MemberList

GEEKS_CHOICES = MemberList.objects.values_list('id','id')

class TransactionPermanentForm(forms.Form):
    fields = '__all__'
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


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].queryset = 

























from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ExampleForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'someId'
        self.helper.form_class = 'some-class'
        self.helper.form_method = 'post'
        self.helper.form_action = 'sample_form_name'

        # Note that the submit button is added separately, with a Semantic UI class.
        self.helper.add_input(Submit('submit', 'Submit',
                              css_class='ui button'))

    like_website = forms.TypedChoiceField(
        label='Do you like this website?',
        choices=((1, 'Yes'), (0, 'No')),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )

    favorite_food = forms.CharField(
        label='What is your favorite food?',
        max_length=80,
        required=True,
    )

    favorite_color = forms.CharField(
        label='What is your favorite color?',
        max_length=80,
        required=True,
    )

    favorite_number = forms.IntegerField(
        label='Favorite number',
        required=False,
    )

    notes = forms.CharField(
        label='Additional notes or feedback',
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.fields['like_website'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter email'})
        self.fields['keywords'].widget.attrs.update({'class' : 'ui input','placeholder':'Enter Key words'})
        self.fields['search_frequency'].widget.attrs.update({'class' : 'ui input','placeholder':'In Hours'})
        self.fields['attachment'].widget.attrs.update({'class' : 'ui input'})
