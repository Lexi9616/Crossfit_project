from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm
from django import forms

from crossfit.models import Profile, WorkoutResponse


class UserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data['email']
        existing_user = Profile.objects.filter(email=email).first()
        if existing_user is not None:
            raise forms.ValidationError("This email is already taken!")


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = Profile
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class ResetPasswordForm(PasswordResetForm):
    class Meta:
        model = Profile
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class PasswordSetForm(SetPasswordForm):
    class Meta:
        model = Profile
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'))

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


    class Meta:
        model = Profile
        fields = ['gender', 'age', 'height', 'weight']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'})
            # 'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class WorkoutResponseForm(forms.ModelForm):
    class Meta:
        model = WorkoutResponse
        fields = ['time_taken', 'rounds_completed', 'weight_used']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_taken'].widget.attrs['class'] = 'form-control'
        self.fields['rounds_completed'].widget.attrs['class'] = 'form-control'
        self.fields['weight_used'].widget.attrs['class'] = 'form-control'
