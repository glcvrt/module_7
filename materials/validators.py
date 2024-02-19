import re
from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube.com')
        tmp = dict(value).get(self.field)
        if not bool(reg.match(tmp)):
            raise ValidationError('Недопустимая ссылка')
