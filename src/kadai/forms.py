from django import forms

from .models import ai_analysis_log


class ai_analysis_logForm(forms.ModelForm):

    class Meta:
        model = ai_analysis_log
        fields = ("image_path",)