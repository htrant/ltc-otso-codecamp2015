__author__ = 'hieutran'
#coding=utf-8

from django.core.mail import EmailMultiAlternatives


class EmailManager:
    def __init__(self):
        pass

    @staticmethod
    def send_feedback_request(email):
        msg = EmailMultiAlternatives(
            subject="Please send us a feedback",
            body="",
            from_email="The Propeller Hats <trunghieu.tran138@gmail.com>",
            to=[email],
            headers={'Reply-To': "The Propeller Hats <trunghieu.tran138@gmail.com>"}  # optional extra headers
        )
        message_body = "<p>Please give us your opinion about our products</p>" \
                       "<p><a href=\"http://ltc-otso2015-kurosh.c9users.io/feedbackformcust.html\">Fill in feedback form</a></p>"

        msg.attach_alternative(message_body, "text/html")
        msg.send()
