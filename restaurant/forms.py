from django import forms

class ApplicationForm(forms.Form):
    name = forms.CharField(label="name of applicant",max_length=50)
    address = forms.CharField(label="address",max_length=100)
    post = (('manager','manager'),('Cashier','Cashier'),('Operator','Operator'))
    field = forms.ChoiceField(choices=post)