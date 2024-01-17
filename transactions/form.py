from django import forms
# from .models import Transaction


class AddMoneyForm(forms.Form):
    amount = forms.DecimalField(min_value=0, label="Add money")
