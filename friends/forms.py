from django import forms
from string import printable


class SearchForm(forms.Form):   
    tag_search = forms.CharField(max_length=20)
    
    def clean_tag_search(self):
        tag = self.cleaned_data['tag_search']
        for i in tag:
            if i not in printable:    
                raise forms.ValidationError('Могут использоваться только английские символы')
        return tag