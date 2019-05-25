from django import forms

class AssignmentForm(forms.Form):
    #example = forms.CharField(label="title")
    assignment_name = forms.CharField(label="assignment_name")
    assignment_desc = forms.CharField(label="assignment_desc", widget=forms.Textarea)
    in_file = forms.FileField(label="in_file")
    out_file = forms.FileField(label="out_file")