from django import forms
from .models import Province


class ProvinceForm(forms.ModelForm):

    class Meta:
        model = Province
        fields = (
            "introduction", "sinhalaName", "tamilName",
            "englishName", "area", "featureImage", "mapUrl"
        )

    introduction = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': "form-control", "rows": 6}
        )
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for fieldName in self.fields:

            self.fields[fieldName].widget.attrs.update(
                {'class': 'form-control'})
