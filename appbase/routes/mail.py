from rest_framework.routers import SimpleRouter

from appbase.views.mail import MailView

router = SimpleRouter(False)
router.register("mail", MailView, "mail")
urls = router.urls