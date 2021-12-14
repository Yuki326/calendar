'''
    form.py
'''
from django.core.files.storage import default_storage
from django import forms

from calendarSite.models import Subject_Schedule, Task
from calendarSite.models import Subject

class addDataForm(forms.Form):
    subject= forms.CharField(
        max_length=200,
        required=True
    )
    title=forms.CharField(
        max_length=200,
        required=True
    )
    date= forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        input_formats=['%Y-%m-%d']
    )
    user=forms.CharField(
        max_length=200,
        required=True
    )


class indexForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()

class subject_manageForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()
    chk=forms.CharField(
        widget=forms.CheckboxInput
    )


class subjectForm(forms.Form):
    subject = forms.CharField(
        max_length=200,
    )
    

class taskForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()



class userForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()

class testForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label = 'Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Subject_Schedule
        fields = ['subject_id','week','period']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['subject_id','name','contents']

