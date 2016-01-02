from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from crispy_forms.bootstrap import FormActions,StrictButton
from localflavor.tr.forms import TRIdentificationNumberField
from .models import Hasta, KateterOlayi
import datetime


class HastaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HastaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            Fieldset(
                'Hasta bilgileri',
                'tckn',
                'ad',
                'soyad'
            )
        )
    tckn = TRIdentificationNumberField()

    class Meta:
        fields = ['tckn','ad','soyad']
        model = Hasta

class KateterOlayiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KateterOlayiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                'Mevcut kateter bilgileri',
                Field('takilma_tarihi',template="custom-widgets/date-widget.html"),
                'tip',
            ),
            FormActions(
                StrictButton("Ekle",type='submit')
            ),
        )

    takilma_tarihi = forms.DateField(input_formats=['%d/%m/%Y','%d.%m.%Y'],initial=datetime.date.today(),widget=forms.DateInput(format='%d/%m/%Y'))

    class Meta:
        fields = ['takilma_tarihi','tip']
        model = KateterOlayi