from django.urls import path

from .views import (
    components_extented_lightbox_view,
    components_extented_rangeslider_view,
    components_extented_sweetalert_view,
    components_extented_rating_view,
    components_extented_notifications_view,

    components_forms_basicelements_view,
    components_forms_validation_view,
    components_forms_advanced_view,
    components_forms_editors_view,
    components_forms_fileupload_view,
    components_forms_wizard_view,
    components_forms_mask_view,

    components_tables_bootstrapbasic_view,
    components_tables_advancedtables_view,

    components_charts_apexcharts_view,
    components_charts_chartsjs_view,

    components_icons_feather_view,
    components_icons_boxicons_view, 
    components_icons_materialdesign_view,
    components_icons_dripicons_view,
    components_icons_fontawesome_view,

    components_maps_googlemaps_view,
    components_maps_vectormaps_view,
    components_maps_leafletmaps_view,
)

app_name = "components"
urlpatterns = [
    # Extented
    path("extented/lightbox", view=components_extented_lightbox_view, name="extented.lightbox"),
    path("extented/rangeslider", view= components_extented_rangeslider_view, name="extented.rangeslider"),
    path("extented/sweetalert", view= components_extented_sweetalert_view, name="extented.sweetalert"),
    path("extented/rating", view= components_extented_rating_view, name="extented.rating"),
    path("extented/notifications", view= components_extented_notifications_view, name="extented.notifications"),

    #forms
    path("forms/basicelements", view = components_forms_basicelements_view, name="forms.basicelements"),
    path("forms/validation", view = components_forms_validation_view, name="forms.validation"),
    path("forms/advanced", view = components_forms_advanced_view, name="forms.advanced"),
    path("forms/editors", view = components_forms_editors_view, name="forms.editors"),
    path("forms/fileupload", view = components_forms_fileupload_view, name="forms.fileupload"),
    path("forms/wizard", view = components_forms_wizard_view, name="forms.wizard"),
    path("forms/mask", view = components_forms_mask_view, name="forms.mask"),

    #tables
    path("tables/bootstrapbasic", view = components_tables_bootstrapbasic_view, name="tables.bootstrapbasic"),
    path("tables/advancedtables", view = components_tables_advancedtables_view, name="tables.advancedtables"),

    #charts
    path("charts/apexcharts", view = components_charts_apexcharts_view, name="charts.apexcharts"),
    path("charts/chartsjs", view = components_charts_chartsjs_view, name="charts.chartsjs"),

    #icons
    path("icons/feather", view = components_icons_feather_view, name="icons.feather"),
    path("icons/boxicons", view = components_icons_boxicons_view, name="icons.boxicons"),
    path("icons/materialdesign", view = components_icons_materialdesign_view, name="icons.materialdesign"),
    path("icons/dripicons", view = components_icons_dripicons_view, name="icons.dripicons"),
    path("icons/fontawesome", view = components_icons_fontawesome_view, name="icons.fontawesome"),

    #maps
    path("maps/google", view = components_maps_googlemaps_view, name="maps.google"),
    path("maps/vector", view = components_maps_vectormaps_view, name="maps.vector"),
    path("maps/leaflet", view = components_maps_leafletmaps_view, name="maps.leaflet"),

]