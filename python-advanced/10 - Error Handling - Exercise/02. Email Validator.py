import re


class EmailValidatorError(Exception):
    pass


class NameTooShortError(EmailValidatorError):
    pass


class MustContainAtSymbolError(EmailValidatorError):
    pass


class InvalidDomainError(EmailValidatorError):
    pass


def email_validator():

    VALID_TLDS = ('.com', '.bg', '.org', '.net')

    pattern = re.compile(
        r'(?P<name>[\w\.-]+)(?P<at_sign>@)([\w\.-]+)*(?P<tld>\.[a-z]+)'
    )

    emails = []

    while True:
        email = input()
        if email == 'End':
            break
        emails.append(email)
    
    for email in emails:

        for match in pattern.finditer(email):
            try:
                at_sign = match.group('at_sign')
                if not at_sign:
                    raise MustContainAtSymbolError('Email must contain @')

                name = match.group('name')
                if not name or len(name) <= 4:
                    raise NameTooShortError(
                        'Name must be more than 4 characters')

                tld = match.group('tld')
                if not tld or tld not in VALID_TLDS:
                    raise InvalidDomainError(
                        f'Domain must be one of the following: {", ".join(VALID_TLDS)}')

                print('Email is valid')

            except EmailValidatorError as err:
                raise err.with_traceback(err.__traceback__)


email_validator()
# email_validator('peter@gmail.com', 'petergmail.com')
# email_validator('peter@gmail.hotmail')
