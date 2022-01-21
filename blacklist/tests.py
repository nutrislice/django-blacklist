from unittest import TestCase

from blacklist.utils import sanitize_ip


class SanitizeIpTests(TestCase):
    def test_empty(self):
        self.assertEqual(sanitize_ip(None), '')
        self.assertEqual(sanitize_ip(''), '')

    def test_regular_ip(self):
        self.assertEqual(sanitize_ip('65.2.3.4'), '65.2.3.4')

    def test_extra_junk(self):
        self.assertEqual(sanitize_ip('some junk),65.26.12.345'), '65.26.12.345')
        self.assertEqual(sanitize_ip('65.26.12.345,some junk)'), '65.26.12.345')
        self.assertEqual(sanitize_ip("LnGMzz8O') OR 859=(SELECT 859 FROM PG_SLEEP(15))--,65.26.12.345"), '65.26.12.345')
