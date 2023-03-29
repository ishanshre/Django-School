from django import forms

from student.models import Student, StudentContact, Guardian

from phonenumber_field.widgets import PhoneNumberPrefixWidget


form_view = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
class DateInput(forms.DateInput):
    input_type = 'date'


class StudentCreateForm(forms.ModelForm):
    create = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = Student
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'picture',
            'date_of_birth',
            'gender',
            'email',
            'temporary_address',
            'permanent_address',
            'registration_id',
            'fathers_name',
            'mothers_name',
            'work_status',
            'disablity',
            'disablity_description',
            'enrolled_date',
        ]
        widgets = {
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":form_view}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name", "class":form_view}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name", "class":form_view}),
            'email':forms.EmailInput(attrs={"placeholder":"Email Address", "class":form_view}),
            'temporary_address':forms.TextInput(attrs={"placeholder":"Temporary Address", "class":form_view}),
            'permanent_address':forms.TextInput(attrs={"placeholder":"Permanent Address", "class":form_view}),
            'registration_id':forms.NumberInput(attrs={"placeholder":"Registration Id", "class":form_view}),
            'fathers_name':forms.TextInput(attrs={"placeholder":"Fathers Name", "class":form_view}),
            'mothers_name':forms.TextInput(attrs={"placeholder":"Mothers Name", "class":form_view}),
            'work_status':forms.TextInput(attrs={"placeholder":"Work Status", "class":form_view}),
            'disablity_description':forms.Textarea(attrs={"placeholder":"Disablity Description", "class":form_view}),
            'date_of_birth':DateInput(),
            'enrolled_date':DateInput()
        }


class StudentUpdateForm(forms.ModelForm):
    update = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = Student
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'picture',
            'date_of_birth',
            'gender',
            'email',
            'temporary_address',
            'permanent_address',
            'registration_id',
            'fathers_name',
            'mothers_name',
            'work_status',
            'disablity',
            'disablity_description',
            'enrolled_date',
        ]
        widgets = {
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":form_view}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name", "class":form_view}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name", "class":form_view}),
            'email':forms.EmailInput(attrs={"placeholder":"Email Address", "class":form_view}),
            'temporary_address':forms.TextInput(attrs={"placeholder":"Temporary Address", "class":form_view}),
            'permanent_address':forms.TextInput(attrs={"placeholder":"Permanent Address", "class":form_view}),
            'registration_id':forms.NumberInput(attrs={"placeholder":"Registration Id", "class":form_view}),
            'fathers_name':forms.TextInput(attrs={"placeholder":"Fathers Name", "class":form_view}),
            'mothers_name':forms.TextInput(attrs={"placeholder":"Mothers Name", "class":form_view}),
            'work_status':forms.TextInput(attrs={"placeholder":"Work Status", "class":form_view}),
            'disablity_description':forms.Textarea(attrs={"placeholder":"Disablity Description", "class":form_view}),
            'date_of_birth':DateInput(),
            'enrolled_date':DateInput()
        }


class StudentDeleteForm(forms.Form):
    delete = forms.BooleanField(initial=True, widget=forms.HiddenInput)



class StudentContactCreateForm(forms.ModelForm):
    student_contact_add = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = StudentContact
        fields = ['phone']
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial="NP")
        }

class StudentContactUpdateForm(forms.ModelForm):
    student_contact_update = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = StudentContact
        fields = ['phone']
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial='NP')
        }

class StudentContactDeleteForm(forms.Form):
    student_contact_delete = forms.BooleanField(initial=True, widget=forms.HiddenInput)

class GuardianCreateForm(forms.ModelForm):
    guardian_create = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = Guardian
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'picture',
            'date_of_birth',
            'gender',
            'email',
            'temporary_address',
            'permanent_address',
            'phone',
            'identity',
            'relationship'
        ]
        widgets = {
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":form_view}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name", "class":form_view}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name", "class":form_view}),
            'date_of_birth': DateInput(),
            'email':forms.EmailInput(attrs={"placeholder":"Email Address", "class":form_view}),
            'temporary_address':forms.TextInput(attrs={"placeholder":"Temporary Address", "class":form_view}),
            'permanent_address':forms.TextInput(attrs={"placeholder":"Permanent Address", "class":form_view}),
            'phone':PhoneNumberPrefixWidget(initial="NP"),
            'relationship':forms.Textarea(attrs={"placeholder":"Guardian relationship with student", "class": form_view})            
        }


class GuardianUpdateForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'picture',
            'date_of_birth',
            'gender',
            'email',
            'temporary_address',
            'permanent_address',
            'phone',
            'identity',
            'relationship'
        ]
        widgets = {
            'first_name':forms.TextInput(attrs={"placeholder":"First Name", "class":form_view}),
            'middle_name':forms.TextInput(attrs={"placeholder":"Middle Name", "class":form_view}),
            'last_name':forms.TextInput(attrs={"placeholder":"Last Name", "class":form_view}),
            'date_of_birth': DateInput(),
            'email':forms.EmailInput(attrs={"placeholder":"Email Address", "class":form_view}),
            'temporary_address':forms.TextInput(attrs={"placeholder":"Temporary Address", "class":form_view}),
            'permanent_address':forms.TextInput(attrs={"placeholder":"Permanent Address", "class":form_view}),
            'phone':PhoneNumberPrefixWidget(initial="NP"),
            'relationship':forms.Textarea(attrs={"placeholder":"Guardian relationship with student", "class": form_view})            
        }


class GuardianDeleteForm(forms.Form):
    guardian_delete = forms.BooleanField(initial=True, widget=forms.HiddenInput)

        