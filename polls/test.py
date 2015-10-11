from django.test import TestCase
import sys

# runthis suite by "manage.py test"

class AnimalTestCase(TestCase):
    def setUp(self):
        print >>sys.stderr, "in setup"

    def test_of_test(self):
        print >>sys.stderr, "in first test"
