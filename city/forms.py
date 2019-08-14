from django import forms
from .models import City
from district.models import District


class CityInitForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('introduction',
                  'sinhalaName',
                  'englishName',
                  'tamilName',
                  'area',
                  'district',
                  'featureImage',
                  'mapUrl',
                  'postal_code')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # add bootstrap class name
        for fieldName in self.fields:

            self.fields[fieldName].widget.attrs.update(
                {'class': 'form-control'})
