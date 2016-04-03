from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, HTML

from.models import AylikVeri

class AylikVeriHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AylikVeriHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        #self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.layout=Layout(
            Fieldset(
                '{{ form.instance }}',
                'ilk_iki_gun',
            )
        )
        self.render_required_fields = True

class AylikVeriForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AylikVeriForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.render_required_fields = True
        #self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout=Layout(
            Fieldset(
                '{}'.format(self.instance),
                'ilk_iki_gun',
            )
        )

    class Meta:
        model = AylikVeri
        fields = [
            'ilk_iki_gun',
        ]