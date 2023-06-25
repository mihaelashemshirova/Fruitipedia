from django.core.exceptions import ValidationError


def check_start_with_a_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def fruit_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
