from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

def card_num_validator(value):
    if len(value) != 16:
        raise ValidationError (
            _('This card number is too long or too short'),
            params={'value':value},
        )
    if not value.isnumeric():
        raise ValidationError(
            _('Card number can only contain numbers'),
            params={'value': value},
        )

def exp_date_validator(value):
    now = datetime.date.now()
    value_lis = value.split(".")

    if value_lis[1].isnumeric():
        year = int(value_lis[1])
    else:
        raise ValidationError(
            _('Year must be a digit'),
            params={'value': value},
        )

    if value_lis[0].isnumeric():
        month = int(value_lis[0])
    else:
        raise ValidationError(
            _('Month must be a digit'),
            params={'value': value},
        )

    if month < 1 or month > 12:
        raise ValidationError(
            _('Month must be a digit between 1 and 12'),
            params={'value': value},
        )

    input_date = datetime.date(year, month)
    if input_date < now:
        raise ValidationError(
            _('This card is expired'),
            params={'value': value},
        )
