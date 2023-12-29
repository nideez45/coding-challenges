import unittest
from serializer import Serializer
from deserializer import Deserializer

class TestSerializerDeserializer(unittest.TestCase):

    def test_serialize_string(self):
        input_string = "hello"
        expected_output = "$5\r\nhello\r\n"
        result = Serializer.serialize_string(input_string)
        self.assertEqual(result, expected_output)

    def test_serialize_list(self):
        input_list = ["SET", "key", "value"]
        expected_output = "*3\r\n$3\r\nSET\r\n$3\r\nkey\r\n$5\r\nvalue\r\n"
        result = Serializer.serialize(input_list)
        self.assertEqual(result, expected_output)

    def test_deserialize_simple_string(self):
        input_response = "+OK\r\n"
        expected_output = "OK"
        result = Deserializer.deserialize(input_response)
        self.assertEqual(result, expected_output)

    def test_deserialize_integer(self):
        input_response = ":42\r\n"
        expected_output = "(integer) 42"
        result = Deserializer.deserialize(input_response)
        self.assertEqual(result, expected_output)

    def test_deserialize_bulk_string(self):
        input_response = "$5\r\nhello\r\n"
        expected_output = "hello"
        result = Deserializer.deserialize(input_response)
        self.assertEqual(result, expected_output)

    def test_deserialize_bulk_string_nil(self):
        input_response = "$-1\r\n"
        expected_output = None
        result = Deserializer.deserialize(input_response)
        self.assertEqual(result, expected_output)

    def test_deserialize_error(self):
        input_response = "-Error message\r\n"
        expected_output = "(error) Error message"
        result = Deserializer.deserialize(input_response)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
