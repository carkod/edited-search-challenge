import unittest
import json
from search import relevance_scoring_search

f = open("./search_dataset.json", "r")
data = json.load(f)


class TestQueries(unittest.TestCase):
    """
    Testing edge cases
    """

    def test_standard_query(self):
        """
        Long search query should return results
        """
        long_query = "floral dress"
        search_results = relevance_scoring_search(long_query, data)
        self.assertTrue(len(search_results) > 1)

    def test_long_queries(self):
        """
        Long search query should return results
        """
        long_query = "prada perforated runway duffel bag"
        search_results = relevance_scoring_search(long_query, data)
        self.assertTrue(len(search_results) > 1)

    def test_empty_query(self):
        """
        Empty search query should not return results
        """
        empty_query = ""
        with self.assertRaises(ValueError):
            relevance_scoring_search(empty_query, data)

    def test_none_query(self):
        """
        When user forgets to provide a search query
        """
        empty_query = None
        with self.assertRaises(ValueError):
            relevance_scoring_search(empty_query, data)

if __name__ == "__main__":
    unittest.main()
