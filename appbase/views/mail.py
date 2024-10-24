from dataclasses import asdict
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from pkg_helpers.logging import logger
from pkg_helpers.response.response import RestResponse
from pkg_helpers.decorators.validate_request import validate_request

from appbase.dtos.send_mail_with_template import SendMailWithTemplateDTO
from appbase.helpers.mail import background_send_mail_with_template
from appbase.serializers.send_mail_with_template import SendMailWithTemplateSerializer

class MailView(ViewSet):
    @action(methods=["POST"], detail=False, url_path="background")
    @swagger_auto_schema(request_body=SendMailWithTemplateSerializer)
    @validate_request(SendMailWithTemplateSerializer)
    def background_send_mail_with_template(self, request: Request, validated_data: dict):
        try:
            data = SendMailWithTemplateDTO(**validated_data)
            background_send_mail_with_template.apply_async(kwargs={"data": asdict(data)})
            return RestResponse().success().response
        except Exception as e:
            logger.exception("MailView.background_send_mail_with_template exc=%s", e)
            return RestResponse().internal_server_error().response