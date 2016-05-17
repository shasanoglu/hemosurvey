from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Div
from crispy_forms.bootstrap import InlineRadios
from .models import Gozlem, FistulKanulasyonu, FistulDekanulasyonu, ElHijyeni, KateterBakimi, BaglamaAyirma
from hasta.forms import superDateField
import datetime

class GozlemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GozlemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            Field('gozlem_tarihi',template="custom-widgets/date-widget.html", css_class="datepicker"),
            'gozlem_saati', 'gozlem_suresi'
        )

    gozlem_tarihi = forms.DateField(input_formats=['%d/%m/%Y','%d.%m.%Y'],initial=datetime.date.today(),widget=superDateField(format='%d/%m/%Y'))

    class Meta:
        fields = [
            'gozlem_tarihi',
            'gozlem_saati', 'gozlem_suresi',
        ]
        model = Gozlem

class AbstractGozlemAdimiType(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        radio_name_list = kwargs.pop('radio_name_list',None)
        super(AbstractGozlemAdimiType, self).__init__(*args, **kwargs)
        unrequired = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10']
        for fieldname in unrequired:
            if fieldname in self.fields:
                self.fields[fieldname].required = False
        head_layout = Layout(
            Div(
                Div(
                    'gozlenen',
                    css_class='col-sm-12 col-md-4'
                ),
                css_class='row'
            )
        )
        foot_layout = Layout(
            Div(
                'ek_yorum',
                css_class='col-sm-12 col-md-4'
            )
        )

        inline_radio_list = self.get_inline_radio_list(radio_name_list)
        mid_layout = Layout(*inline_radio_list)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout=Layout(
            head_layout,
            mid_layout,
            foot_layout,
        )
    def get_inline_radio_list(self,name_list):
        inline_radio_list = []
        for name in name_list:
            inline_radio_list.append(
                InlineRadios(name)
            )
        return inline_radio_list


class FistulKanulasyonuForm(AbstractGozlemAdimiType):
    def __init__(self, *args, **kwargs):
        kwargs['radio_name_list'] = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10']
        super(FistulKanulasyonuForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
        model = FistulKanulasyonu


class FistulDekanulasyonuForm(AbstractGozlemAdimiType):
    def __init__(self, *args, **kwargs):
        kwargs['radio_name_list'] = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09']
        super(FistulDekanulasyonuForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
        model = FistulDekanulasyonu


class ElHijyeniForm(AbstractGozlemAdimiType):
    def __init__(self, *args, **kwargs):
        kwargs['radio_name_list'] = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10']
        super(ElHijyeniForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
        model = ElHijyeni


class KateterBakimiForm(AbstractGozlemAdimiType):
    def __init__(self, *args, **kwargs):
        kwargs['radio_name_list'] = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10']
        super(KateterBakimiForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
        model = KateterBakimi

class BaglamaAyirmaForm(AbstractGozlemAdimiType):
    def __init__(self, *args, **kwargs):
        kwargs['radio_name_list'] = ['ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09']
        super(BaglamaAyirmaForm, self).__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
        model = BaglamaAyirma