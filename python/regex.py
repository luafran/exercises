import unittest
import re


def replace_email_domain(text, old_domain, new_domain):
    regex = re.compile(r'(\w+)@' + old_domain)
    return regex.sub(r'\g<1>@' + new_domain, text)


class TestReplaceEmailDomain(unittest.TestCase):

    def test_dont_replace1(self):
        text = 'this is not an email @something@ so it should not be replaced'

        self.assertEqual(text, replace_email_domain(text, 'old.com', 'new_domain.com'))

    def test_dont_replace2(self):
        text = 'this is not the domain to be replaced something@not_old.com so it should not be replaced'

        self.assertEqual(text, replace_email_domain(text, 'old.com', 'new_domain.com'))

    def test_dont_replace3(self):
        text = 'this is not an email @old.com so it should not be replaced'

        self.assertEqual(text, replace_email_domain(text, 'old.com', 'new_domain.com'))

    def test_replace1(self):
        text = 'this is an email user@old.com so it should be replaced'
        expected_text = 'this is an email user@new_domain.com so it should be replaced'

        self.assertEqual(expected_text, replace_email_domain(text, 'old.com', 'new_domain.com'))
