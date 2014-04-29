from morelia import Parser

from django.test import TestCase

class MoreliaTestCase(TestCase):
    def test_evaluate_file(self):
        if hasattr(self.__class__, 'feature_file'):
            Parser().parse_file(self.__class__.feature_file).evaluate(self)