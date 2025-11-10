from django import forms
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

# Django Form for validation
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()  # only accepts valid email formats
    message = forms.CharField(widget=forms.Textarea)

# View
def contact_view(request):
    scroll_to_contact = False  # flag for template to scroll after success

    if request.method == 'POST':
        # Bind form with POST data
        form = ContactForm(request.POST)

        if form.is_valid():
            # Get cleaned data
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']

            # Compose full message
            full_message = f"Message from {name} ({user_email}):\n\n{message_text}"

            try:
                # Send email via your Gmail account
                email = EmailMessage(
                    subject=f"New message from {name}",
                    body=full_message,
                    from_email=settings.EMAIL_HOST_USER,  # always your Gmail
                    to=[settings.EMAIL_HOST_USER],        # admin receives it
                    reply_to=[user_email],                # allows reply to user email
                )
                email.send(fail_silently=False)

                messages.success(request, "Your message has been sent successfully!")
                scroll_to_contact = True
                return redirect('/#contact_us')

            except Exception as e:
                messages.error(request, "Something went wrong. Please try again later.")
                logger.error(f"Error sending contact message: {e}")

        else:
            # Form invalid (e.g., email format wrong)
            messages.error(request, "Please enter a valid email and all required fields.")

    else:
        form = ContactForm()  # empty form for GET requests

    return render(request, 'index.html', {'scroll_to_contact': scroll_to_contact, 'form': form})
