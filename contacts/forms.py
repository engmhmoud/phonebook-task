from django import forms

from .models import Contact, Numbers

# from django.forms import inlineformset_factory

# BookFormSet = inlineformset_factory(Contact, Numbers, fields=("title",), formset=forms.BaseInlineFormSet)
# author = Contact.objects.get(name="Mike Royko")
# formset = BookFormSet(instance=author)


# class NumberInline(forms.BaseInlineFormSet):
#     model = Numbers


# class ContactForm(forms.ModelForm):
#     inlines = [
#         NumberInline,
#     ]

#     class Meta:
#         model = Contact
#         fields = ("firstname", "lastname", "email", "numbers", "mobile_phone")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("firstname", "lastname", "email", "mobile_phone")


class NemberForm(forms.ModelForm):
    class Meta:
        model = Numbers
        fields = ("phone",)


# NumberFormSet = forms.inlineformset_factory(Contact, Numbers, form=MemberForm, extra=2)
NemberFormSet = forms.inlineformset_factory(Contact, Numbers, form=NemberForm, extra=2)
