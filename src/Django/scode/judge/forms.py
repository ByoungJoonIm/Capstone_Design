from django import forms

class AssignmentForm(forms.Form):
    assignment_name = forms.CharField(label="assignment_name")
    assignment_desc = forms.CharField(label="assignment_desc", widget=forms.Textarea)
    deadline = forms.IntegerField(label="deadline", initial=7)
    in_file = forms.FileField(label="in_file")
    out_file = forms.FileField(label="out_file")

class CodingForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(), label="code")

class LoginForm(forms.Form):
    userid = forms.CharField(label="userid")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
