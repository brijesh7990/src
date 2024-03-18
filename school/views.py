from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from school.forms import AddParentForm, AddStudentForm, AddTeacherForm
from user.models import Parent, SchoolUser, Teacher, User
from django.views.generic.edit import CreateView
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import View
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q


# Create your views here.


class DashboardView(TemplateView):
    template_name = "users/superadmindashboard.html"


class StudentView(ListView):
    template_name = "users/studentlist.html"
    context_object_name = "students"
    queryset = User.objects.filter(role=User.STUDENT)


class ParentView(ListView):
    template_name = "users/parentlist.html"
    context_object_name = "parents"
    queryset = User.objects.filter(role=User.PARENT)


class TeacherView(ListView):
    template_name = "users/teacherlist.html"
    context_object_name = "teachers"
    queryset = User.objects.filter(role=User.TEACHER)


class AddStudentView(CreateView):
    model = User
    form_class = AddStudentForm
    template_name = "users/addstudent.html"
    success_url = reverse_lazy("students")




class AddParentView(CreateView):
    model = Parent
    form_class = AddParentForm
    template_name = "users/addparent.html"
    success_url = reverse_lazy("parents")



class AddTeacherView(CreateView):
    model = Teacher
    form_class = AddTeacherForm
    template_name = "users/addteacher.html"
    success_url = reverse_lazy("teachers")


class StudentAjaxView(DataTableMixin, View):
    model = User
    queryset = User.objects.filter(role = User.STUDENT)

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search) |
                Q(email__icontains=self.search) |
                Q(phone__icontains=self.search) |
                Q(address__icontains=self.search)
            )
        return qs
    
    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append({
                'username': o.username,
                'email': o.email,
                'phone': o.phone,
                'address': o.address,
                
            })
        return data
    
    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)



class ParentAjaxView(DataTableMixin, View):
    model = User
    queryset = User.objects.filter(role = User.PARENT)

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search) |
                Q(email__icontains=self.search) |
                Q(phone__icontains=self.search) |
                Q(address__icontains=self.search)
            )
        return qs
    
    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append({
                'username': o.username,
                'email': o.email,
                'phone': o.phone,
                'address': o.address,
                
            })
        return data
    
    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)



class TeacherAjaxView(DataTableMixin, View):
    model = User
    queryset = User.objects.filter(role = User.TEACHER)

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search) |
                Q(email__icontains=self.search) |
                Q(phone__icontains=self.search) |
                Q(address__icontains=self.search)
            )
        return qs
    
    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append({
                'username': o.username,
                'email': o.email,
                'phone': o.phone,
                'address': o.address,
                
            })
        return data
    
    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)

