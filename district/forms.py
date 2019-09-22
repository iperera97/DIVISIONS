from django import forms
from .models import District
from Province.models import Province


class DistrictInitForm(forms.ModelForm):

    introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': "form-control", "rows": 12}
        )
    )

    class Meta:
        model = District
        fields = ['introduction',
                  'province',
                  'sinhalaName',
                  'englishName',
                  "tamilName",
                  "area",
                  "featureImage",
                  "mapUrl"]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for fieldName in self.fields:

            self.fields[fieldName].widget.attrs.update(
                {'class': 'form-control'})
