from django import forms


class ImportBooksForm(forms.Form):
    query = forms.CharField(label='Enter Keywords',
                            max_length=100,
                            required=False)
