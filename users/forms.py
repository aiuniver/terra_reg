from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from users.models import TerraUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = TerraUser
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column('last_name', css_class='form-group col-md-6 mb-0 mx-auto'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0 mx-auto'),
                css_class='form-row'
            ),
        )
        self.helper.add_input(Submit('submit', 'Sign Up'))