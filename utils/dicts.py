# файл utils/dicts.py
def get_val(collection, key, default='git'):
    pass
# файл utils/dicts.py
def get_val(collection, key, default='git'):
    return collection.get(key, default)

def test_get_val_existing_key_with_value(self):
    collection = {'key1': 'value1', 'key2': 'value2'}
    key = 'key2'
    result = dicts.get_val(collection, key)
    self.assertEqual(result, 'value2')

def test_get_val_existing_key_with_empty_value(self):
    collection = {'key1': '', 'key2': 'value2'}
    key = 'key1'
    result = dicts.get_val(collection, key)
    self.assertEqual(result, '')

def test_get_val_non_existing_key(self):
        collection = {'key1': 'value1', 'key2': 'value2'}
        key = 'key3'
        result = dicts.get_val(collection, key)
        self.assertEqual(result, 'git')
def get_val(data, key, default='git'):
    return data.get(key, default)

asd