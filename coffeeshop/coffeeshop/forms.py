from django import forms


class NameForm(forms.Forms):
    name = forms.CharField(label='Your name', max_length=100)

    def save(self):
        pass