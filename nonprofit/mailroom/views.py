from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from postmark import PMMail
from nonprofit.mailroom.forms import MailroomForm

def contact(request):

    if request.method == "POST":

        form = MailroomForm(request.POST, label_suffix='')

        if form.is_valid():

            slot = form.cleaned_data['slot']
            recipients = ", ".join(slot.recipients())

            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']

            message = render_to_string("mailroom/email.txt", form.cleaned_data)

            try:

                # mail to Sunlight staff
                PMMail(
                    to=recipients,
                    cc=getattr(settings, "MAILROOM_CC", ""),
                    reply_to="%s <%s>" % (name, from_email),
                    subject="[%s] message from %s" % (settings.NONPROFIT_URL_DISPLAY, name),
                    text_body=message,
                ).send()

                # confirmation email to recipient
                PMMail(
                    to="%s <%s>" % (name, from_email),
                    subject="Thank you for contacting %s" % settings.NONPROFIT_NAME,
                    text_body=render_to_string("mailroom/confirmation.txt", {'slot': slot, 'name': name}),
                ).send()

                messages.success(request, 'Thank you for contacting us! We will get back to you shortly.')

            except:

                messages.error(request, 'Sorry, your message could not be sent. Please email us directly at %s' % settings.NONPROFIT_EMAIL)

            return HttpResponseRedirect("/contact/")

    else:

        form = MailroomForm(label_suffix='')

    return render_to_response("mailroom/form.html",
                              { "form": form },
                              context_instance=RequestContext(request))