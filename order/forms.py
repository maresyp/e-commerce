from django import forms
from .models import Order

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['city', 'street', 'house_number', 'postal_code', 'phone_number']
        labels = {
            'city': 'Miejscowość',
            'street': 'Ulica', 
            'house_number': 'Numer domu', 
            'postal_code': 'Kod pocztowy', 
            'phone_number': 'Numer telefonu',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DeliveryAddressForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['city'].initial = user.profile.city
            self.fields['street'].initial = user.profile.street
            self.fields['house_number'].initial = user.profile.house_number
            self.fields['postal_code'].initial = user.profile.postal_code
            self.fields['phone_number'].initial = user.profile.phone_number

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    def clean(self):
        cleaned_data = super().clean()
        for field_name in self.fields:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, f"Pole {self.fields[field_name].label} jest wymagane.")
        return cleaned_data
