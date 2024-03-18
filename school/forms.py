from django import forms

from user.models import Parent, Teacher, User, Student
from school.models import School
from academic.models import Section, Standard
from django.contrib.auth.hashers import make_password


class AddStudentForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all())
    standard = forms.ModelChoiceField(queryset=Standard.objects.all())
    section = forms.ModelChoiceField(queryset= Section.objects.all())

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "dob",
            "gender",
            "blood_group",
            "phone",
            "religion",
            "address",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "type": "password"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
    
    
    def save(self, commit=True):
        print(">>>>>>", self.cleaned_data)
        user = super(AddStudentForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.role = User.STUDENT
        
        user.save()
        if commit:
            student = Student.objects.create(
                user=user,
                standard=self.cleaned_data['standard'],
                section=self.cleaned_data['section'],
                school=self.cleaned_data['school']
            )
            student.save()
        return user



class AddParentForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label="Username", required=True)
    email = forms.EmailField(
        label="Email Address", widget=forms.EmailInput(attrs={"type": "email"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"type": "password"})
    )
    dob = forms.CharField(
        label="Date of Birth", widget=forms.TextInput(attrs={"type": "date"})
    )
    students = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(role="student")
    )
    profile_pic = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Parent
        fields = [
            "school",
            "father_name",
            "mother_name",
            "father_occupation",
            "mother_occupation",
        ]

    def __init__(self, *args, **kwargs):
        super(AddParentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def save(self, commit = True):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        dob = self.cleaned_data.get("dob")
        students = self.cleaned_data.get("students")
        profile_pic = self.cleaned_data.get("profile_pic")

        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            dob=dob,
            profile_pic=profile_pic,
            role=User.PARENT,
        )
        parent = super().save(commit=False)
        parent.user = user
        parent.save()

        parent.students.set(students)
        return parent


class AddTeacherForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all())
    joining_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Joining Date")
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "dob",
            "gender",
            "blood_group",
            "phone",
            "religion",
            "address",
        ]

        widgets = {
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "type": "password"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AddTeacherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        user.role =User.TEACHER
        user.save()
        if commit:
            teacher = Teacher.objects.create(
                user = user,
                joining_date = self.cleaned_data["joining_date"],
                school = self.cleaned_data["school"]
            )
            teacher.save()
        return teacher


