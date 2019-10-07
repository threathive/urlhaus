import unittest
from urlhaus import UrlHaus

class UrlHausTest(unittest.TestCase):
    def setUp(self):
        self.u = UrlHaus()

    def test_pull_urls(self):
        _urls = self.u.pull_recent_urls()
        self.assertTrue(_urls)

    def test_pull_payloads(self):
        _payloads = self.u.pull_recent_payloads()
        self.assertTrue(_payloads)

    def test_download_sample(self):
        _download = self.u.download_sample("020f1fa6072108c79ed6f553f4f8b08e157bf17f9c260a76353300230fed09f0")
        self.assertTrue(_download)

    def test_lookup_by_signature(self):
        _hits = self.u.lookup_by_signature("gozi")
        self.assertTrue(_hits)

    def test_lookup_by_tag(self):
        _hits = self.u.lookup_by_tag("gozi")
        self.assertTrue(_hits)

    def test_lookup_by_urlid(self):
        _hit = self.u.lookup_by_urlid("237847")
        self.assertTrue(_hit)

    def test_lookup_by_url(self):
        _hit = self.u.lookup_by_url("http://zsdstat14tp.world/isb777amx.exe")
        self.assertTrue(_hit)

    def test_lookup_by_hash(self):
        _hit = self.u.lookup_by_hash("1a4e065eed31548e1f3bea5f0f9576a752e5c7eb93d87feb65a9178b61358569")
        self.assertTrue(_hit)

    def test_lookup_by_host(self):
        _hit = self.u.lookup_by_host("zsdstat14tp.world")
        self.assertTrue(_hit)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
