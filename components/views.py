from django.shortcuts import render

# Create your views here.

from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView


# Create your views here.
class ComponentsView(LoginRequiredMixin,TemplateView):
    pass
#components 

#extended   
components_extented_lightbox_view = ComponentsView.as_view(template_name="components/extended/lightbox.html")
components_extented_rangeslider_view = ComponentsView.as_view(template_name="components/extended/rangeslider.html")
components_extented_sweetalert_view = ComponentsView.as_view(template_name="components/extended/sweetalert.html")
components_extented_rating_view = ComponentsView.as_view(template_name="components/extended/rating.html")
components_extented_notifications_view = ComponentsView.as_view(template_name="components/extended/notifications.html")

#forms
components_forms_basicelements_view = ComponentsView.as_view(template_name="components/forms/basicelements.html")
components_forms_validation_view = ComponentsView.as_view(template_name="components/forms/validation.html")
components_forms_advanced_view = ComponentsView.as_view(template_name="components/forms/advanced.html")
components_forms_editors_view = ComponentsView.as_view(template_name="components/forms/editors.html")
components_forms_fileupload_view = ComponentsView.as_view(template_name="components/forms/fileupload.html") 
components_forms_wizard_view = ComponentsView.as_view(template_name="components/forms/wizard.html") 
components_forms_mask_view = ComponentsView.as_view(template_name="components/forms/mask.html")

#tables
components_tables_bootstrapbasic_view = ComponentsView.as_view(template_name="components/tables/bootstrapbasic.html")
components_tables_advancedtables_view = ComponentsView.as_view(template_name="components/tables/advancedtables.html")

#charts
components_charts_apexcharts_view = ComponentsView.as_view(template_name="components/charts/apexcharts.html")
components_charts_chartsjs_view = ComponentsView.as_view(template_name="components/charts/chartsjs.html")

#icons
components_icons_feather_view = ComponentsView.as_view(template_name="components/icons/feather.html")
components_icons_boxicons_view = ComponentsView.as_view(template_name="components/icons/boxicons.html")
components_icons_materialdesign_view = ComponentsView.as_view(template_name="components/icons/materialdesign.html")
components_icons_dripicons_view = ComponentsView.as_view(template_name="components/icons/dripicons.html")
components_icons_fontawesome_view = ComponentsView.as_view(template_name="components/icons/fontawesome.html")

#maps
components_maps_googlemaps_view = ComponentsView.as_view(template_name="components/maps/googlemaps.html")
components_maps_vectormaps_view = ComponentsView.as_view(template_name="components/maps/vectormaps.html")
components_maps_leafletmaps_view = ComponentsView.as_view(template_name="components/maps/leafletmaps.html")







