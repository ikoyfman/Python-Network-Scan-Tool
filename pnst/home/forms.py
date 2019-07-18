from django import forms

from home.models import Scan

class ScanForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(ScanForm, self).__init__(*args,**kwargs)
        self.fields['subnet'].widget = forms.NumberInput()
        self.fields['subnet'].widget.attrs.update({"placeholder":"Leave blank for 1 host"})
    

    class Meta:
        model = Scan
        fields = ['scan_target','subnet']

    
    def clean_subnet(self):
        subnet = self.cleaned_data['subnet']
        if not subnet:
            return  subnet
        elif subnet > 32 or subnet < 1:
            raise forms.ValidationError("The subnet can only be between 1 and 32")
        
        return subnet

