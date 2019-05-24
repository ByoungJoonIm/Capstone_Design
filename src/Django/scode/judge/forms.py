from django import forms

class AssignmentForm(forms.Form):
    #example = forms.CharField(label="title")
    assignment_name = forms.CharField(label="assignment_name")
    assignment_desc = forms.CharField(label="assignment_desc", widget=forms.Textarea)
    test_case_file = forms.FileField(label="test_case")
    solution_file = forms.FileField(label="solution")
