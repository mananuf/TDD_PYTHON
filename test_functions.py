from unittest import TestCase;
from functions import addTwoNumbers;

class TestAdditionOfTwoNumbers(TestCase):

    def test_float_values(self):
        """ Test addiition when values are floats """
        self.assertAlmostEqual(addTwoNumbers(3.4556, 8.3567), 11.8123);
        self.assertEqual(addTwoNumbers(2.3, 5.7), 8);
        self.assertNotEqual(addTwoNumbers(3,7), 11);
    
    def test_additon_will_pass_if_values_are_integer(self):
        """ Test addiition when values are floats """
        self.assertEqual(addTwoNumbers(2, 5), 7);
        self.assertEqual(addTwoNumbers(3,7), 10);

    def test_will_raise_value_error_if_invalid_values_are_passed(self):
        """Test will raise value errors if invalid value is passed"""
        with self.assertRaises(ValueError): addTwoNumbers(-3, 7);
        with self.assertRaises(ValueError): addTwoNumbers(3, -7);

    def test_will_raise_type_error_if_invalid_types_are_passed(self):
        """Test will raise value errors if invalid value is passed"""
        with self.assertRaises(TypeError): addTwoNumbers(3, "i");
        with self.assertRaises(TypeError): addTwoNumbers(True, 7);
        with self.assertRaises(TypeError): addTwoNumbers( (4 + 1j), 7);