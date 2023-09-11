# storeapp/forms.py
from django import forms

from storeapp.models import Department


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = forms.CharField(max_length=20)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = forms.MultipleChoiceField(choices=[('Notebook', 'Notebook'), ('Pen', 'Pen'), ('Exam Papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)

from django import forms
from .models import Department, Course

class OrderForm(forms.Form):
    name = forms.CharField(max_length=255)
    # Add other form fields as needed
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='Select Department')
    course = forms.ModelChoiceField(queryset=Course.objects.none(), empty_label='Select Course')
    # Add other form fields as needed

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
