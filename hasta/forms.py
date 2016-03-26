from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field
from crispy_forms.bootstrap import FormActions,StrictButton, InlineRadios
from localflavor.tr.forms import TRIdentificationNumberField
from .models import Hasta, KateterOlayi, DiyalizOlayi
from antibiyogram.models import Mikroorganizma
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

class superDateField(forms.DateInput):
    class Media:
        css = {
            'all' : (
                'datepicker/css/bootstrap-datetimepicker.min.css',
            ),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.6/moment.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.6/locale/tr.js',
            'datepicker/js/bootstrap-datetimepicker.min.js',
            'datepicker/js/datepicker-initialize.js'
        )

class KateterOlayiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KateterOlayiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('tip',css_class='tip-select'),
                Field('takilma_tarihi',template="custom-widgets/date-widget.html", css_class="datepicker"),
                'takildigi_merkez',
                Div('yeri','degisim_nedeni',css_class="fistul-hide")
            ),
            FormActions(
                StrictButton("Ekle",type='submit')
            ),
        )

    takilma_tarihi = forms.DateField(input_formats=['%d/%m/%Y','%d.%m.%Y'],initial=datetime.date.today(),widget=superDateField(format='%d/%m/%Y'))

    class Meta:
        fields = [
            'tip','takilma_tarihi',
            'takildigi_merkez',
            'yeri','degisim_nedeni'
        ]
        model = KateterOlayi

    class Media:
        js = ('js/kateter-tip-select.js',)

class OlayForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OlayForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            Fieldset(
                'Diyaliz olayı',
                'isi_hiperemi_puy',
            )
        )
    class Meta:
        model = DiyalizOlayi
        fields = [
            'isi_hiperemi_puy',
        ]

class AddEtkenForm(forms.Form):
    def __init__(self,*args, **kwargs):
        queryset = kwargs.pop('queryset')
        super().__init__(*args, **kwargs)
        self.fields['mikroorganizmalar'].queryset = queryset
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_tag = False
        self.helper.layout=Layout(
            'mikroorganizmalar'
        )
    mikroorganizmalar = forms.ModelMultipleChoiceField(required=False,queryset=Mikroorganizma.objects.all(),label='Etken olarak eklemek istediğiniz mikroorganizmaları seçin')