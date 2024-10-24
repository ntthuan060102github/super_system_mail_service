from dataclasses import dataclass, field
from appbase.helpers.enums.mail_templates import MailTemplates

@dataclass
class SendMailWithTemplateDTO:
    to: list[str] = field(default_factory=list)
    subject: str = ""
    template: str = ""
    context: dict = field(default_factory=dict)
