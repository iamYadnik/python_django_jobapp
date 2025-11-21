from django import forms
from django.core.exceptions import ValidationError
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('invalid last name')
#     return value



class Subscribeform(forms.ModelForm):
    class Meta:
        model=Subscribe
        # fields = ['first_name', 'last_name', 'email']
        fields = '__all__'
        # exclude = {'first_name'}
        labels = {'first_name' : _('Enter first name'),
                  'last_name' : _('enter last name'),
                  'email' : _('enter email')}
        error_messages = {'first_name' : {'required' : _('you can not go ahead')},
                          'last_name' : {'required' : _('you can not go ahead')}}
        help_texts = {'first_name' : _('')}

    # first_name = forms.CharField(max_length=100, required=False,
    #                               label='Enter your first name',
    #                               help_text='Enter characters only',
    #                               disabled=False,
    #                               validators=[validate_comma],)
    # last_name = forms.CharField(max_length=100,
    #                              label='Enter your Last name',
    #                              validators=[validate_comma],)
    # email = forms.EmailField(max_length=100, required=False,
    #                           label='Enter your email',
    #                           validators=[validate_comma])



    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError('invalid first name')
            
    #     return data
