import unittest
from utils import dicts

class TestDictsFunctions(unittest.TestCase):
    def test_get_val_existing_key(self):
        collection = {'key1': 'value1', 'key2': 'value2'}
        key = 'key1'
        result = dicts.get_val(collection, key)
        self.assertEqual(result, 'value1')

    def test_get_val_non_existing_key(self):
        collection = {'key1': 'value1', 'key2': 'value2'}
        key = 'key3'
        result = dicts.get_val(collection, key)
        self.assertEqual(result, 'git')

if __name__ == '__main__':
    unittest.main()

class TestGetVal(unittest.TestCase):
    def test_existing_key_with_value(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(dicts.get_val(data, "vcs"), "mercurial")

    def test_existing_key_with_default_value(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(dicts.get_val(data, "vcs", "git"), "mercurial")

    def test_non_existing_key_with_default_value(self):
        data = {}
        self.assertEqual(dicts.get_val(data, "vcs", "git"), "git")

    def test_non_existing_key_with_another_default_value(self):
        data = {}
        self.assertEqual(dicts.get_val(data, "vcs", "bazaar"), "bazaar")

if __name__ == '__main__':
    unittest.main()
