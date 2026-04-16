from django.urls import path

from .views import (
    bootstrap_alerts_view,
    bootstrap_buttons_view,
    bootstrap_cards_view,
    bootstrap_carousel_view,
    bootstrap_dropdowns_view,
    bootstrap_grid_view,
    bootstrap_images_view,
    bootstrap_modals_view,
    bootstrap_offcanvas_view,
    bootstrap_placeholders_view,
    bootstrap_progressbars_view,
    bootstrap_tabs_view,
    bootstrap_typography_view,
    bootstrap_video_view,
    bootstrap_general_view,
    bootstrap_colors_view,
)

app_name = "bootstrap"
urlpatterns = [
    path("alerts", view=bootstrap_alerts_view, name="bootstrap.alerts"),
    path("buttons", view=bootstrap_buttons_view, name="bootstrap.buttons"),
    path("cards", view=bootstrap_cards_view, name="bootstrap.cards"),
    path("carousel", view=bootstrap_carousel_view, name="bootstrap.carousel"),
    path("dropdowns", view=bootstrap_dropdowns_view, name="bootstrap.dropdowns"),
    path("grid", view=bootstrap_grid_view, name="bootstrap.grid"),
    path("images", view=bootstrap_images_view, name="bootstrap.images"),
    path("modals", view=bootstrap_modals_view, name="bootstrap.modals"),
    path("offcanvas", view= bootstrap_offcanvas_view, name="bootstrap.offcanvas"),
    path("placeholders", view= bootstrap_placeholders_view, name="bootstrap.placeholders"),
    path("progressbars", view= bootstrap_progressbars_view, name="bootstrap.progressbars"),
    path("tabs", view =bootstrap_tabs_view, name="bootstrap.tabs"),
    path("typography", view =bootstrap_typography_view, name="bootstrap.typography"),
    path("video", view = bootstrap_video_view, name="bootstrap.video"),
    path("general", view = bootstrap_general_view, name="bootstrap.general"),
    path("colors", view = bootstrap_colors_view, name="bootstrap.colors"),

]