import unittest
from credis_cli import RedisClient

class TestRedisClient(unittest.TestCase):

    def setUp(self):
        self.redis_client = RedisClient()

    def tearDown(self):
        self.redis_client.close()

    def test_set_get_value(self):
        key = 'test_key'
        value = 'test_value'

        set_command = f'SET {key} {value}'
        result = self.redis_client.execute_command(set_command)
        self.assertEqual(result, 'OK')

        get_command = f'GET {key}'
        result = self.redis_client.execute_command(get_command)
        self.assertEqual(result, value)

    def test_set_get_nonexistent_key(self):
        nonexistent_key = 'nonexistent_key'
        get_command = f'GET {nonexistent_key}'
        result = self.redis_client.execute_command(get_command)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
