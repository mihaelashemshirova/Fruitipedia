from django import forms

from .models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_email', 'password']
        labels = {
            'first_name': '',
            'last_name': '',
            'profile_email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'profile_email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitCreateFrom(FruitBaseForm):
    pass


class FruitEditFrom(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_readonly_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

    def __set_readonly_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
