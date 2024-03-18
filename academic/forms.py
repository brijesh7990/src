from django import forms
from academic.models import *



class AddStandardForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    class Meta:
        model = Standard
        fields = [
            "school",
            "standard",
        ]
        widgets = {
            "school": forms.Select(attrs={"class": "form-control"}),
            "standard": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(AddStandardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    def save(self, commit=True):
        standard = super(AddStandardForm, self).save(commit=False)
        standard.save()
        standard.subject.set(self.cleaned_data['subjects'])
        return standard