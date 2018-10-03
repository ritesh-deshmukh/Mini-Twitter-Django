from django.core.exceptions import ValidationError


# validate on migrations
def validate_content(value):
    if value == "":
        raise ValidationError("Content cannot be Blank")
    return value