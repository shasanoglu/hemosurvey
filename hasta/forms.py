from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from crispy_forms.bootstrap import FormActions,StrictButton, InlineRadios
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
                Div(
                    'tckn','ad','soyad','dogum_yili','cinsiyet',
                    css_class="col-sm-12 col-md-6"
                ),
                Div(
                    'boy','kilo','diyaliz_ilk_yil','calisma_durumu','yasadigi_il',
                    css_class="col-sm-12 col-md-6"
                )

            ),
            Div(
                Fieldset(
                    'Diyaliz için altta yatan hastalık',
                    'ayh_HT','ayh_DM','polikistik_bobrek','dogustan_tek_bobrek','ailesel_bobrek_hastaliklari','ayh_diger',
                    css_class="col-sm-12 col-md-4",
                ),
                Fieldset(
                    'Komorbid hastalık',
                    'kh_HT','kh_DM','gecirilmis_SVO','koroner_arter_hastaligi','astim_koah','kh_diger',
                    css_class="col-sm-12 col-md-4",
                ),
                Fieldset(
                    'Bağımlılık',
                    'alkol','sigara','uyusturucu_madde',
                    css_class="col-sm-12 col-md-4",
                ),
                css_class='row'
            ),
            Div(
                Fieldset(
                    'Hepatit serolojisi',
                    'HBsAg','AntiHBs','AntiHBcIgG','AntiHBcIgM','AntiHCV',
                    css_class="col-sm-12 col-md-4 col-md-offset-2",
                ),
                Fieldset(
                    'Diğer',
                    InlineRadios('MRSA_kolonizayonu'),
                    InlineRadios('influenza_asisi'),
                    InlineRadios('pnomokok_asisi'),
                    InlineRadios('egitim'),
                    css_class="col-sm-12 col-md-4",
                ),
                css_class='row'
            )
        )
    tckn = TRIdentificationNumberField()

    class Meta:
        fields = [
            'tckn','ad','soyad','dogum_yili','cinsiyet',
            'boy','kilo','diyaliz_ilk_yil','calisma_durumu','yasadigi_il',
            'ayh_HT','ayh_DM','polikistik_bobrek','dogustan_tek_bobrek','ailesel_bobrek_hastaliklari','ayh_diger',
            'kh_HT','kh_DM','gecirilmis_SVO','koroner_arter_hastaligi','astim_koah','kh_diger',
            'alkol','sigara','uyusturucu_madde',
            'HBsAg','AntiHBs','AntiHBcIgG','AntiHBcIgM','AntiHCV',
            'MRSA_kolonizayonu','influenza_asisi','pnomokok_asisi','egitim',
        ]
        model = Hasta


class UpdateHastaForm(HastaForm):
    def __init__(self, *args, **kwargs):
        super(UpdateHastaForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            self.helper.layout,
            FormActions(
                StrictButton("Değiştir",type='submit')
            ),
        )


class KateterOlayiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KateterOlayiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
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