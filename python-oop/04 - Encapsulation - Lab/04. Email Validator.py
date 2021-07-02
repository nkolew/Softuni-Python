from typing import Tuple


class EmailParser:
    def parse(self, email: str) -> Tuple[str, str, str]:
        name, *rest = email.split('@')
        mail, domain = rest[0].split('.')
        return name, mail, domain


class EmailValidator:
    min_length: int
    mails: list
    domains: list
    __parser: EmailParser

    def __init__(self, min_length: int, mails: list, domains: list) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
        self.__parser = EmailParser()

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email) -> bool:
        name, mail, domain = self.__parser.parse(email)

        return self.__is_name_valid(name) and \
            self.__is_mail_valid(mail) and \
            self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

import unittest

class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_name_valid("abc"), False)
        self.assertEqual(ev._EmailValidator__is_name_valid("abcdef"), True)
        
    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_mail_valid("me"), True)
        self.assertEqual(ev._EmailValidator__is_mail_valid("you"), False)
        
    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__is_domain_valid("he"), True)
        self.assertEqual(ev._EmailValidator__is_domain_valid("she"), False)
        
    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)
        
if __name__ == "__main__":
   unittest.main()