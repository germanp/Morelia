from morelia import Parser

from casper.tests import CasperTestCase

class MoreliaCasperTestCase(CasperTestCase):
    def test_evaluate_file(self):
        if hasattr(self.__class__, 'feature_file'):
            Parser().parse_file(self.__class__.feature_file).evaluate(self)
