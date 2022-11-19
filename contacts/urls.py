from django.urls import path

from contacts.views import ContactList, AddContact, ViewContact

urlpatterns = [
    path("", ContactList.as_view(), name="contact-list"),
    # path("add-contact", AddContact.as_view(), name="add-contact"),
    path("add-contact", AddContact.as_view(), name="add-contact"),
    path("view-contact/<str:pk>", ViewContact.as_view(), name="view-contact"),
]
