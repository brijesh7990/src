from django.shortcuts import render
from django.views.generic.list import ListView
from academic.forms import AddStandardForm
from user.models import Parent, SchoolUser, Teacher, User
from academic.models import *
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


class StandardView(ListView):
    template_name = "academic/standard.html"
    context_object_name = "standards"
    queryset = Standard.objects.all()




class StandardAjaxView(DataTableMixin, View):
    model = User
    queryset = Standard.objects.all()

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(school__name__icontains=self.search) |
                Q(standard__icontains=self.search) |
                Q(subject__icontains=self.search)
            )
        # print(f"==>> qs: {qs}")
        return qs
    
    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            print(f"==>> o: {o}")

            

            data.append({
                'school': o.school.name,
                'standard': o.standard,
                'subject': list(o.subject.all().values_list('name', flat=True))
                
            })
        print(f"==>> data: {data}")
        return data
    
    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


class AddStandardView(CreateView):
    model = User
    form_class = AddStandardForm
    template_name = "academic/addstandard.html"
    success_url = reverse_lazy("standardlist")



# class SectionView(ListView):
#     template_name = "academic/section.html"
#     context_object_name = "sections"
#     queryset = Section.objects.all()




# class SectionAjaxView(DataTableMixin, View):
#     model = User
#     queryset = Section.objects.all()

#     def filter_queryset(self, qs):
#         """Return the list of items for this view."""
#         # If a search term, filter the query
#         if self.search:
#             return qs.filter(
#                 Q(school__name__icontains=self.search) |
#                 Q(name__icontains=self.search) |
#                 Q(standard__standard__icontains=self.search) |
#                 Q(teacher__user__username__icontains=self.search)
#             )
#         print(f"==>> qs: {qs}")
#         return qs
    
#     def prepare_results(self, qs):
#         # Create row data for datatables
#         data = []
#         for o in qs:
#             print(f"==>> o: {o}")

            

#             data.append({
#                 'school': o.school.name,
#                 'standard': o.standard,
#                 'subject': list(o.subject.all().values_list('name', flat=True))
                
#             })
#         print(f"==>> data: {data}")
#         return data
    
#     def get(self, request, *args, **kwargs):
#         context_data = self.get_context_data(request)
#         return JsonResponse(context_data)


# class AddSectionView(CreateView):
#     model = User
#     form_class = AddStandardForm
#     template_name = "academic/addstandard.html"
#     success_url = reverse_lazy("standardlist")