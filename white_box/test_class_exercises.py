# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestCheckNumberStaus(unittest.TestCase):
    """
    Exercise #01
    """

    def test_check_number_status_positive(self):
        """
        Checks positive number.
        """
        self.assertEqual(check_number_status(2), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks negative number.
        """
        self.assertEqual(check_number_status(-2), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks number 0.
        """
        self.assertEqual(check_number_status(0), "Zero")


class TestValidatePassword(unittest.TestCase):
    """
    Exercise #02
    """

    def test_validate_password_correct_password(self):
        """
        Checks password with everything
        """
        self.assertTrue(validate_password("Password@123"))

    def test_validate_password_wrong_length(self):
        """
        Checks password with length lower than 8
        """
        self.assertFalse(validate_password("Pass@1"))

    def test_validate_password_no_uppercase(self):
        """
        Checks password with no uppercase
        """
        self.assertFalse(validate_password("password@123"))

    def test_validate_password_no_lowercase(self):
        """
        Checks password with no lowercase
        """
        self.assertFalse(validate_password("PASWORD@123"))

    def test_validate_password_no_digit(self):
        """
        Checks password with no digits
        """
        self.assertFalse(validate_password("Password@"))

    def test_validate_password_no_special_char(self):
        """
        Checks password with no special characters
        """
        self.assertFalse(validate_password("password123"))


class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Exercise #03
    """

    def test_calculate_total_discount_less_than_100(self):
        """
        Checks discount for total_amount < 100
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_between_100_and_500_no_1(self):
        """
        Checks discount for total_amount = 100
        """
        self.assertEqual(calculate_total_discount(100), 0.1 * 100)

    def test_calculate_total_discount_between_100_and_500_no_2(self):
        """
        Checks discount for total_amount = 500
        """
        self.assertEqual(calculate_total_discount(500), 0.1 * 500)

    def test_calculate_total_discount_greater_than_500(self):
        """
        Checks discount for total_amount > 500
        """
        self.assertEqual(calculate_total_discount(501), 0.2 * 501)


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")
