from django.urls import reverse_lazy
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import redirect

# Create your views here .
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from contacts.forms import ContactForm, NemberForm

# from contacts.forms import ContactForm
from .models import Contact, Numbers

# @method_decorator(login_required, name='dispatch')
# class ContactList(ListView, PermissionMixin):


class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "contact_list.html"
    context_object_name = "contact_list"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# this contact was working successfully for adding signle numnber for  contact


class AddContact(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "contacts/add_contact.html"
    success_url = reverse_lazy("contacts:contact-list")
    fields = ("firstname", "lastname", "email", "mobile_phone")

    form = ContactForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# def add_contact(request):

#     user = request.user
#     NumberInlineFormSet = forms.inlineformset_factory(Numbers, Contact, fields=("phone", "firstname"))
#     if request.method == "POST":
#         formset = NumberInlineFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()

#             return redirect("contacts:contact-list")
#     else:
#         formset = NumberInlineFormSet()
#     return render(request, "contacts/add_contact.html", {"form": formset})

# ContactSet = forms.inlineformset_factory(
#     parent_model=Contact,
#     model=Numbers,
#     form=NemberForm,
#     can_delete=True,
#     extra=2,
# )


# class AddContact(LoginRequiredMixin, CreateView):
#     model = Contact
#     template_name = "contacts/add_contact.html"
#     success_url = reverse_lazy("contacts:contact-list")
#     # fields = ("firstname", "lastname", "email", "mobile_phone")
#     # fields = "__all__"
#     form_class = ContactSet

#     def post(self, request, *args, **kwargs):
#         """Overriding post method to handle inline formsets."""
#         # Setup the formset for PlanCost
#         MemberFormSet = forms.inlineformset_factory(
#             parent_model=Contact,
#             model=Numbers,
#             form=NemberForm,
#             can_delete=True,
#             extra=1,
#         )

#         self.object = None
#         form = self.get_form(self.get_form_class())
#         member_forms = MemberFormSet(self.request.POST)

#         if form.is_valid() and member_forms.is_valid():
#             return self.form_valid(form, member_forms)

#         return self.form_invalid(form, member_forms)
