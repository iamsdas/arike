from allauth.account.forms import SignupForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    name = forms.CharField(
        max_length=30,
        label="Full Name",
    )
    phone = forms.CharField(max_length=16, label="Phone Number")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "label": "Full Name",
                "placeholder": "Full Name",
            }
        )
        self.fields["phone"].widget.attrs.update(
            {
                "label": "Phone Number",
                "placeholder": "Phone Number",
            }
        )


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].label = ""
        self.fields["password"].label = ""
