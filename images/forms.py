# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from models import Image


class ImageForm(forms.ModelForm):
    image_path = forms.CharField(
        max_length=255,
        widget=forms.HiddenInput(),
        required=False,
    )
    delete_image = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False,
    )

    class Meta:
        model = Image
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Image form"),
                layout.Field("title", css_class="form-control"),
                layout.HTML(u"""{% load i18n %}
                    <div id="image_upload_widget">
                        <div class="preview">
                            {% if instance.image %}
                                <img src="{{ MEDIA_URL }}{{ instance.image }}" alt="" />
                            {% endif %}
                        </div>
                        <div class="uploader">
                            <noscript>
                                <p>{% trans "Please enable JavaScript to use file uploader." %}</p>
                            </noscript>
                        </div>
                        <p class="help_text" class="help-block">{% trans "Available formats are JPG, GIF, and PNG." %}</p>
                        <div class="messages"></div>
                    </div>
                """),
                "image_path",
                "delete_image",
            ),
            bootstrap.FormActions(
                layout.Submit('submit', _('Save'), css_class="btn btn-primary"),
            )
        )