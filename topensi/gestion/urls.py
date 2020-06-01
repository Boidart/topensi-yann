from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from gestion.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^add/$', login_required(AddView.as_view())),
    url(r'^update/$', login_required(UpdateView.as_view())),
    url(r'^recurrent/$', login_required(RecurrentView.as_view())),
    url(r'^login/$', LoginView.as_view()),
    url(r'^add/ajouter_client/$', login_required(AjouterClientView.as_view())),
    url(r'^add/ajouter_type/$', login_required(AjouterTypeView.as_view())),
    url(r'^add/ajouter_partenaire/$', login_required(AjouterPartenaireView.as_view())),
    url(r'^add/ajouter_etat/$', login_required(AjouterEtatView.as_view())),
    url(r'^add/ajouter_info/$', login_required(AjouterInfoView.as_view())),
    url(r'^filter/$', login_required(FilterInfoView.as_view())),
    url(r'^filter/recurrent/$', login_required(FilterRecurrentView.as_view())),
    url(r'^update/delete/$', login_required(DeleteInfo.as_view())),
    url(r'^update/maj/$', login_required(UpdateInfo.as_view())),
    url(r'^recurrent/maj/$', login_required(UpdateRecurrent.as_view())),
    url(r'^export/$', login_required(ExportView.as_view())),
]