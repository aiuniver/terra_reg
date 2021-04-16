from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from users.models import TerraUser


def validate_unique_user(value):
    if not value:
        return
    if TerraUser.objects.filter(email=value).exists():
        raise ValidationError("Пользователь с таким E-mail уже существует")


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="E-mail", validators=[validate_unique_user])

    class Meta:
        model = TerraUser
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_id = "form-registration"
        self.helper.attrs = {"novalidate": "novalidate"}
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-6 mb-0 mx-auto"),
                css_class="form-row",
            ),
            Row(
                Column("last_name", css_class="form-group col-md-6 mb-0 mx-auto"),
                css_class="form-row",
            ),
            Row(
                Column("email", css_class="form-group col-md-6 mb-0 mx-auto"),
                css_class="form-row",
            ),
        )
        self.helper.add_input(Submit("submit", "Зарегистрироваться"))
