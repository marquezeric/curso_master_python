from django import forms
from django.core import validators

#  Generación de un formulario más ágil, mantenible y validado (más limpia)  Basado en clases, tomando como 
#  nombre de las clases, los nombres de nuestros modelos

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Título",
        max_length = 40,
        required = True,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Introduce el título',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 í]*$', 'El título está mal formado', 'invalid_title')
        ]

    )
    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea,
            validators=[
                validators.MaxLengthValidator(20,'Has revasado el límite de texto')
            ]

                             #(
            #attrs={
            #    'placeholder':'Introduce el contenido',
            #    'class':'contenido_form_article'
            #}
        #)
    )
# -----------Otra forma de darle atributos a nuestros objetos de formulario---------------------------
    content.widget.attrs.update({
        'placeholder':'Ahora introduce el contenido',
        'class':'contenido_form_article',
        'id': 'contenido_form'
    })

    public_options= [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )