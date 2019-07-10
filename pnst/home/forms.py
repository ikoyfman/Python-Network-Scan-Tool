from django import forms

from home.models import Scan

class ScanForm(forms.ModelForm):

    class Meta:
        model = Scan
        fields = ['scan_target','subnet']
