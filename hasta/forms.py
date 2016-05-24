from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, HTML
from crispy_forms.bootstrap import FormActions,StrictButton, InlineRadios
from localflavor.tr.forms import TRIdentificationNumberField
from .models import Hasta, KateterOlayi, DiyalizOlayi, Duyarlilik
from antibiyogram.models import Mikroorganizma
import datetime


class HastaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.merkez = kwargs.pop('merkez',None)
        super(HastaForm, self).__init__(*args, **kwargs)
        unrequired = ['HBsAg','AntiHBs','AntiHBcIgG','AntiHBcIgM','AntiHCV','AntiHIV']
        for fieldname in unrequired:
            if fieldname in self.fields:
                self.fields[fieldname].required = False
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
                    'ayh_HT','ayh_DM','polikistik_bobrek','dogustan_tek_bobrek','ailesel_bobrek_hastaliklari','nefrolitiazis','idiopatik','ayh_diger',
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
                    InlineRadios('HBsAg'),
                    InlineRadios('AntiHBs'),
                    InlineRadios('AntiHBcIgG'),
                    InlineRadios('AntiHBcIgM'),
                    InlineRadios('AntiHCV'),
                    InlineRadios('AntiHIV'),
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

    def clean(self):
        cleaned_data = super(HastaForm, self).clean()
        other_patients_of_merkez = self.merkez.hasta_set
        if self.instance:
            other_patients_of_merkez = other_patients_of_merkez.exclude(id=self.instance.id)

        try:
            if other_patients_of_merkez.filter(tckn = cleaned_data['tckn']).exists():
                other_patient = other_patients_of_merkez.filter(tckn = cleaned_data['tckn'])[0]
                self.add_error('tckn','Girdiğiniz no ile kayıtlı bir hasta zaten var: {} {}'.format(other_patient.ad,other_patient.soyad))
        except:
            pass



    class Meta:
        fields = [
            'tckn','ad','soyad','dogum_yili','cinsiyet',
            'boy','kilo','diyaliz_ilk_yil','calisma_durumu','yasadigi_il',
            'ayh_HT','ayh_DM','polikistik_bobrek','dogustan_tek_bobrek','ailesel_bobrek_hastaliklari','nefrolitiazis','idiopatik','ayh_diger',
            'kh_HT','kh_DM','gecirilmis_SVO','koroner_arter_hastaligi','astim_koah','kh_diger',
            'alkol','sigara','uyusturucu_madde',
            'HBsAg','AntiHBs','AntiHBcIgG','AntiHBcIgM','AntiHCV','AntiHIV',
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
        hidden_neden = kwargs.pop('hidden_neden',False)

        super(KateterOlayiForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if hidden_neden:
            del self.fields['degisim_nedeni']

        if hidden_neden:
            self.helper.layout = Layout(
                Fieldset(
                    '',
                    Field('tip',css_class='tip-select'),
                    Field('takilma_tarihi',template="custom-widgets/date-widget.html", css_class="datepicker"),
                    'takildigi_merkez',
                    Div('yeri',css_class="fistul-hide")
                ),
                FormActions(
                    StrictButton("Ekle",type='submit')
                ),
            )
        else:
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
            'yeri','degisim_nedeni',
        ]
        model = KateterOlayi

    class Media:
        js = ('js/kateter-tip-select.js',)

class OlayForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.hasta = kwargs.pop('hasta',None)
        super(OlayForm, self).__init__(*args, **kwargs)
        if not self.hasta:
            try:
                self.hasta = self.instance.hasta
            except:
                pass
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            Div(
                Div(
                    Field('olay_tarihi',template="custom-widgets/date-widget.html", css_class="datepicker"),
                    Fieldset(
                        'Olay tipi',
                        'isi_hiperemi_puy','iv_antibiyotik',
                        Field('kan_kulturunde_ureme',css_class='kultur-select'),
                    ),
                    Fieldset(
                        'Hasta tipi',
                        'gecici_hasta'
                    ),
                    css_class='col-sm-12 col-md-6'
                ),
                Div(
                    Fieldset(
                        'Kan kültüründe üreme ile ilgili bilgiler',
                        'kateterde_ureme','periferde_ureme','etken_alindi_mi','olasi_kaynak',
                    ),
                    css_class='col-sm-12 col-md-6 kultur-hide'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Fieldset(
                        'Spesifik problemler',
                        'ates','hipotansiyon','acik_yara','selulit','uriner_enfeksiyon','pnomoni_sye','diger',
                    ),
                    css_class='col-sm-12 col-md-6'
                ),
                Div(
                    Fieldset(
                        'Olaya bağlı gelişen mortalite/morbidite',
                        InlineRadios('kateter_cikarildi'),
                        InlineRadios('hospitalizasyon'),
                        InlineRadios('olum')
                    ),
                    css_class='col-sm-12 col-md-6 kultur-hide'
                ),
                css_class='row'
            )
        )

    def clean(self):
        cleaned_data = super(OlayForm, self).clean()
        olay_tarihi = cleaned_data.get("olay_tarihi")
        isi_hiperemi_puy = cleaned_data.get("isi_hiperemi_puy")
        iv_antibiyotik = cleaned_data.get("iv_antibiyotik")
        kan_kulturunde_ureme = cleaned_data.get("kan_kulturunde_ureme")

        if not olay_tarihi:
            return

        timedelta = datetime.timedelta(days=21)
        before_olay = olay_tarihi - timedelta
        after_olay = olay_tarihi + timedelta

        if self.instance.id:
            otherObjects = DiyalizOlayi.objects.exclude(id=self.instance.id)
        else:
            otherObjects = DiyalizOlayi.objects

        if isi_hiperemi_puy:
            if otherObjects.filter(olay_tarihi__range=(before_olay, olay_tarihi),isi_hiperemi_puy__exact=True, hasta=self.hasta).exists():
                self.add_error('isi_hiperemi_puy','Girdiğiniz tarihten 21 gün öncesine kadar başka bir Isı artışı / hiperemi / püy olayı olamaz. Bilgileri bir önceki Isı artışı / hiperemi / püy olayına eklemelisiniz')

            if otherObjects.filter(olay_tarihi__range=(olay_tarihi, after_olay),isi_hiperemi_puy__exact=True, hasta=self.hasta).exists():
                self.add_error('isi_hiperemi_puy','Girdiğiniz tarihten 21 gün sonrasına kadar başka bir Isı artışı / hiperemi / püy olayı olamaz. Daha ileri tarihli Isı artışı / hiperemi / püy olayının tarihini geriye alabilirsiniz')

        if iv_antibiyotik:
            if otherObjects.filter(olay_tarihi__range=(before_olay, olay_tarihi),iv_antibiyotik__exact=True, hasta=self.hasta).exists():
                self.add_error('iv_antibiyotik','Girdiğiniz tarihten 21 gün öncesine kadar başka bir IV Antibiyotik olayı olamaz. Bilgileri bir önceki IV Antibiyotik olayına eklemelisiniz')

            if otherObjects.filter(olay_tarihi__range=(olay_tarihi, after_olay),iv_antibiyotik__exact=True, hasta=self.hasta).exists():
                self.add_error('iv_antibiyotik','Girdiğiniz tarihten 21 gün sonrasına kadar başka bir Isı IV Antibiyotik olayı olamaz. Daha ileri tarihli IV Antibiyotik olayının tarihini geriye alabilirsiniz')

        if kan_kulturunde_ureme:
            if otherObjects.filter(olay_tarihi__range=(before_olay, olay_tarihi),kan_kulturunde_ureme__exact=True, hasta=self.hasta).exists():
                self.add_error('kan_kulturunde_ureme','Girdiğiniz tarihten 21 gün öncesine kadar başka bir Kan kültüründe üreme olayı olamaz. Bilgileri bir önceki Kan kültüründe üreme olayına eklemelisiniz')

            if otherObjects.filter(olay_tarihi__range=(olay_tarihi, after_olay),kan_kulturunde_ureme__exact=True, hasta=self.hasta).exists():
                self.add_error('kan_kulturunde_ureme','Girdiğiniz tarihten 21 gün sonrasına kadar başka bir Kan kültüründe üreme olayı olamaz. Daha ileri tarihli Kan kültüründe üreme olayının tarihini geriye alabilirsiniz')

        if not (isi_hiperemi_puy or iv_antibiyotik or kan_kulturunde_ureme):
            self.add_error('isi_hiperemi_puy','En az bir olay tipi seçmelisiniz')
            self.add_error('iv_antibiyotik','En az bir olay tipi seçmelisiniz')
            self.add_error('kan_kulturunde_ureme','En az bir olay tipi seçmelisiniz')

        kateterde_ureme = cleaned_data.get("kateterde_ureme")
        periferde_ureme = cleaned_data.get("periferde_ureme")
        if kan_kulturunde_ureme and (not (kateterde_ureme or periferde_ureme)):
            self.add_error('kateterde_ureme','En az bir üreme tipi eklemelisiniz')
            self.add_error('periferde_ureme','En az bir üreme tipi eklemelisiniz')

    olay_tarihi = forms.DateField(input_formats=['%d/%m/%Y','%d.%m.%Y'],initial=datetime.date.today(),widget=superDateField(format='%d/%m/%Y'))

    class Meta:
        model = DiyalizOlayi
        fields = [
            'olay_tarihi',
            'isi_hiperemi_puy','iv_antibiyotik','kan_kulturunde_ureme',
            'gecici_hasta',
            'kateterde_ureme','periferde_ureme','etken_alindi_mi','olasi_kaynak',
            'ates','hipotansiyon','acik_yara','selulit','uriner_enfeksiyon','pnomoni_sye','diger',
            'kateter_cikarildi','hospitalizasyon','olum',
        ]

    class Media:
        js = ('js/kultur-select.js',)

class AddEtkenForm(forms.Form):
    def __init__(self,*args, **kwargs):
        queryset = kwargs.pop('queryset')
        super().__init__(*args, **kwargs)
        self.fields['mikroorganizmalar'].queryset = queryset
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            'mikroorganizmalar'
        )
    mikroorganizmalar = forms.ModelMultipleChoiceField(required=False,queryset=Mikroorganizma.objects.all(),label='Etken olarak eklemek istediğiniz mikroorganizmaları seçin')

class DuyarlilikForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        direnc_label_name = kwargs.pop('direnc_label_name')
        super(DuyarlilikForm, self).__init__(*args, **kwargs)
        self.fields['direnc'].label = direnc_label_name
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-12 col-md-12'
        self.helper.field_class = 'col-sm-12 col-md-12'
        self.helper.form_tag = False
        self.helper.layout=Layout(
            InlineRadios('direnc')
        )
    duyarlilik_id = forms.HiddenInput()
    class Meta:
        model = Duyarlilik
        fields = [
            'direnc',
        ]
