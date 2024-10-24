from rest_framework import serializers

from appbase.helpers.enums.mail_templates import MailTemplates

class SendMailWithTemplateSerializer(serializers.Serializer):
    to = serializers.ListField(
        child=serializers.EmailField(max_length=150, min_length=1),
        allow_empty=False,
        max_length=20
    )
    subject = serializers.CharField(min_length=1, max_length=250)
    template = serializers.ChoiceField(MailTemplates.choices)
    context = serializers.DictField(required=False, allow_null=True)