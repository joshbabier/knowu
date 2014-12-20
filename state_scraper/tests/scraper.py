import json

from django.test import TestCase

from state_scraper.scraper import read_url, pretty_print_content


class TestScraper(TestCase):
    """
    Tests the functionality of the scraper module.
    """
    base_url = 'http://api.sba.gov/geodata/city_county_links_for_state_of/'

    def setUp(self):
        pass

    def test_sanity(self):
        """
        Initial test to make sure Nose runner is working
        """
        assert 1 == 1

    def test_read_url(self):
        content = read_url(self.base_url + 'AL.json')

        # Makes sure content is a JSON string
        parsed_content = json.loads(content)
        # make sure we have a list
        assert isinstance(parsed_content, list)

    def test_read_url_that_does_not_exist(self):
        """
        Test to make sure a bad url is handled gracefully
        """
        content = read_url('does_not_exist')
        assert content == '{"error": "Bad Url"}'

    def test_read_url_with_invalid_path(self):
        """
        Test to make sure a good url with a bad request is handled gracefully
        """
        content = read_url(self.base_url + 'XXX')
        assert content == '{"error": "Bad Request"}'

    def test_pretty_print_content(self):
        content = '[{"county_name":"Mobile","description":null,"feat_class":"Populated Place","feature_id":"256",' \
                  '"fips_class":"C1","fips_county_cd":"97","full_county_name":"Mobile County","link_title":null,' \
                  '"url":"http:\/\/townofdauphinisland.org\/","name":"Dauphin Island","primary_latitude":"30.25",' \
                  '"primary_longitude":"-88.1","state_abbreviation":"AL","state_name":"Alabama"}]'
        pretty_content = pretty_print_content(content)
        expected_content = """[
    {
        "county_name": "Mobile",
        "description": null,
        "feat_class": "Populated Place",
        "feature_id": "256",
        "fips_class": "C1",
        "fips_county_cd": "97",
        "full_county_name": "Mobile County",
        "link_title": null,
        "name": "Dauphin Island",
        "primary_latitude": "30.25",
        "primary_longitude": "-88.1",
        "state_abbreviation": "AL",
        "state_name": "Alabama",
        "url": "http://townofdauphinisland.org/"
    }
]"""
        assert pretty_content == expected_content

    def test_pretty_print_content_not_json(self):
        """
        Test to make sure an attempt to pretty print non-JSON is handled gracefully
        """
        pretty_content = pretty_print_content("I am not JSON")
        assert pretty_content == '{"error": "Invalid JSON"}'
