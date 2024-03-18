from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path("standardlist/", login_required(views.StandardView.as_view()), name="standardlist"),
    path("addstandard/", login_required(views.AddStandardView.as_view()), name="addstandard"),
    path("standardajax", login_required(views.StandardAjaxView.as_view()), name="standardajax"),
    # path("sectionlist/", login_required(views.SectionView.as_view()), name="sectionlist"),
    # path("addsection/", login_required(views.AddSectionView.as_view()), name="addsection"),
    # path("sectionajax", login_required(views.SectionAjaxView.as_view()), name="sectionajax"),
]
