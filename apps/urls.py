from django.urls import path

from .views import (
    apps_calendar_calendar_view,
    apps_chat_chat_view,

    #Email
    apps_email_inbox_view,
    apps_email_read_view,

    # Ecommerce
    apps_ecommerce_products_view,
    apps_ecommerce_product_detail_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_cart_view,
    apps_ecommerce_checkout_view,
    apps_ecommerce_shops_view,
    apps_ecommerce_add_product_view,

    apps_invoice_list_view,
    apps_invoice_details_view,

    apps_contacts_usergrid_view,
    apps_contacts_userlist_view,
    apps_contacts_userprofile_view,
)

app_name = "apps"
urlpatterns = [
    # calendar
    path("calendar", view=apps_calendar_calendar_view, name="calendar"),
    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),
    # Email
    path("email/inbox", view=apps_email_inbox_view, name="email.inbox"),
    path("emial/read_email", view=apps_email_read_view ,name="email.read"),

    # Ecommerce
    path("ecommerce/products",view=apps_ecommerce_products_view,name="ecommerce.products"),
    path("ecommerce/product-detail",view=apps_ecommerce_product_detail_view,name="ecommerce.product_detail"),
    path("ecommerce/orders",view=apps_ecommerce_orders_view,name="ecommerce.orders"),
    path("ecommerce/customers",view=apps_ecommerce_customers_view,name="ecommerce.customers"),
    path("ecommerce/cart",view=apps_ecommerce_cart_view,name="ecommerce.cart"),
    path("ecommerce/checkout",view=apps_ecommerce_checkout_view,name="ecommerce.checkout"),
    path("ecommerce/shops",view=apps_ecommerce_shops_view,name="ecommerce.shops"),
    path("ecommerce/add-product",view=apps_ecommerce_add_product_view,name="ecommerce.add_product"),

    #Invoice
    path("invoice/invoice_list", view=apps_invoice_list_view, name="invoice.list"),
    path("invoice/invoice_details", view=apps_invoice_details_view, name="invoice.details"),

    #Contacts
    path("contacts/user_grid", view= apps_contacts_usergrid_view, name="contacts.usergrid"),
    path("contacts/user_list", view= apps_contacts_userlist_view, name="contacts.userlist"),
    path("contacts/user_profile", view= apps_contacts_userprofile_view, name="contacts.userprofile"),
]