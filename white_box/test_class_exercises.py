# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
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
        Checks password with length less than 8
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


class TestCalculateOrderTotal(unittest.TestCase):
    """
    Exercise #04
    """

    def test_calculate_order_total_empty_items(self):
        """
        Checks total_price for no items / no quantity
        """
        items = []
        self.assertEqual(calculate_order_total(items), 0)

    def test_calculate_order_total_between_1_and_5_no_1(self):
        """
        Checks total_price for quantity = 1
        """
        items = [{"quantity": 1, "price": 10}]
        self.assertEqual(calculate_order_total(items), 10)

    def test_calculate_order_total_between_1_and_5_no_2(self):
        """
        Checks total_price for quantity = 5
        """
        items = [{"quantity": 5, "price": 10}]
        self.assertEqual(calculate_order_total(items), 5 * 10)

    def test_calculate_order_total_between_6_and_10_no_1(self):
        """
        Checks total_price for quantity = 6
        """
        items = [{"quantity": 6, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0.95 * 6 * 10)

    def test_calculate_order_total_between_6_and_10_no_2(self):
        """
        Checks total_price for quantity = 10
        """
        items = [{"quantity": 10, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0.95 * 10 * 10)

    def test_calculate_order_total_greater_than_10(self):
        """
        Checks total_price for quantity > 10
        """
        items = [{"quantity": 11, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0.9 * 11 * 10)

    def test_calculate_order_total_different_quantities(self):
        """
        Checks total_price for different items with different quantities
        """
        items = [
            {"quantity": 2, "price": 5},
            {"quantity": 8, "price": 10},
            {"quantity": 20, "price": 2},
        ]
        output = (2 * 5) + (0.95 * 8 * 10) + (0.9 * 20 * 2)
        self.assertEqual(calculate_order_total(items), output)

    #
    # Preguntar al profe si para el ejercicio 4 y 5 incluyo testcases para cunado items está vacía
    # o quantity/weight = 0
    #


class TestCalculateItemsShippingCost(unittest.TestCase):
    """
    Exercise #05
    """

    def test_calculate_items_shipping_cost_standard_less_or_equal_to_5(self):
        """
        Checks shipping_cost for standard shipping method and total_weight <= 5
        """
        items = [{"weight": 5}]
        shipping_method = "standard"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 10)

    def test_calculate_items_shipping_cost_standard_between_5_and_10_no_1(self):
        """
        Checks shipping_cost for standard shipping method and 5 < total_weight <= 10
        """
        items = [{"weight": 5.01}]
        shipping_method = "standard"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 15)

    def test_calculate_items_shipping_cost_standard_between_5_and_10_no_2(self):
        """
        Checks shipping_cost for standard shipping method and 5 < total_weight <= 10
        """
        items = [{"weight": 10}]
        shipping_method = "standard"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 15)

    def test_calculate_items_shipping_cost_standard_greater_than_10(self):
        """
        Checks shipping_cost for standard shipping method and total_weight > 10
        """
        items = [{"weight": 10.01}]
        shipping_method = "standard"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 20)

    def test_calculate_items_shipping_cost_express_less_or_equal_to_5(self):
        """
        Checks shipping_cost for express shipping method and total_weight <= 5
        """
        items = [{"weight": 5}]
        shipping_method = "express"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 20)

    def test_calculate_items_shipping_cost_express_between_5_and_10_no_1(self):
        """
        Checks shipping_cost for express shipping method and 5 < total_weight <= 10
        """
        items = [{"weight": 5.01}]
        shipping_method = "express"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 30)

    def test_calculate_items_shipping_cost_express_between_5_and_10_no_2(self):
        """
        Checks shipping_cost for express shipping method and 5 < total_weight <= 10
        """
        items = [{"weight": 10}]
        shipping_method = "express"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 30)

    def test_calculate_items_shipping_cost_express_greater_than_10(self):
        """
        Checks shipping_cost for express shipping method and total_weight > 10
        """
        items = [{"weight": 10.01}]
        shipping_method = "express"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 40)

    #
    # Preguntar al profe si para el ejercicio 5 incluyo test cases para suma de pesos
    #


class TestValidateLogin(unittest.TestCase):
    """
    Exercise #06
    """

    def test_validate_login_username_in_range_and_password_in_range(self):
        """
        Checks login for 5 <= username <= 20 and 8 <= password <= 15
        """
        self.assertEqual(validate_login("nicolas", "password"), "Login Successful")

    def test_validate_login_username_in_range_and_password_not_in_range_no_1(self):
        """
        Checks login for 5 <= username <= 20 and password < 8
        """
        self.assertEqual(validate_login("nicol", "passwor"), "Login Failed")

    def test_validate_login_username_in_range_and_password_not_in_range_no_2(self):
        """
        Checks login for 5 <= username <= 20 and password > 15
        """
        self.assertEqual(
            validate_login("nicolasGonzalezPerez", "password12345678"), "Login Failed"
        )

    def test_validate_login_username_not_in_range_and_password_in_range_no_1(self):
        """
        Checks login for 8 <= password <= 15 and username < 5
        """
        self.assertEqual(validate_login("nicol", "passwor"), "Login Failed")

    def test_validate_login_username_not_in_range_and_password_in_range_no_2(self):
        """
        Checks login for 8 <= password <= 15 and username > 20
        """
        self.assertEqual(
            validate_login("nicolasGonzalezPerez1", "password1234567"), "Login Failed"
        )


class TestVerifyAge(unittest.TestCase):
    """
    Exercise #07
    """

    def test_verify_age_between_18_and_65_no_1(self):
        """
        Checks for 18 <= age <= 65
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_between_18_and_65_no_2(self):
        """
        Checks for 18 <= age <= 65
        """
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_less_than_18(self):
        """
        Checks for age < 18
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_greater_than_65(self):
        """
        Checks for age > 65
        """
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """
    Exercise #08
    """

    def test_categorize_product_category_a_no_1(self):
        """
        Checks for 10 <= price <= 50
        """
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_category_a_no_2(self):
        """
        Checks for 10 <= price <= 50
        """
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b_no_1(self):
        """
        Checks for 51 <= price <= 100
        """
        self.assertEqual(categorize_product(51), "Category B")

    def test_categorize_product_category_b_no_2(self):
        """
        Checks for 51 <= price <= 100
        """
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_category_c_no_1(self):
        """
        Checks for 101 <= price <= 200
        """
        self.assertEqual(categorize_product(101), "Category C")

    def test_categorize_product_category_c_no_2(self):
        """
        Checks for 101 <= price <= 200
        """
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_category_d_no_1(self):
        """
        Checks for price < 10
        """
        self.assertEqual(categorize_product(9), "Category D")

    def test_categorize_product_category_d_no_2(self):
        """
        Checks for price > 200
        """
        self.assertEqual(categorize_product(201), "Category D")


class TestValidateEmail(unittest.TestCase):
    """
    Exercise #09
    """

    def test_validate_email_correct_email(self):
        """
        Checks for email with 5 <= length <= 50, @ and .
        """
        self.assertEqual(validate_email("email@test.com"), "Valid Email")

    def test_validate_email_wrong_length(self):
        """
        Checks for email with length out of range
        """
        self.assertEqual(validate_email("em@."), "Invalid Email")

    def test_validate_email_no_at(self):
        """
        Checks for email with no @
        """
        self.assertEqual(validate_email("email.test"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """
        Checks for email with no .
        """
        self.assertEqual(validate_email("email@test"), "Invalid Email")

    #
    # Preguntar al profe si para el ejercicio 9 está bien el límite de length
    #


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Exercise #10
    """

    def test_celsius_to_fahrenheit_between_minus_100_and_100_no_1(self):
        """
        Checks for -100 <= celsius <= 100
        """
        self.assertEqual(celsius_to_fahrenheit(-100), (-100 * 9 / 5) + 32)

    def test_celsius_to_fahrenheit_between_minus_100_and_100_no_2(self):
        """
        Checks for -100 <= celsius <= 100
        """
        self.assertEqual(celsius_to_fahrenheit(100), (100 * 9 / 5) + 32)

    def test_celsius_to_fahrenheit_less_than_minus_100(self):
        """
        Checks for celsius < -100
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_greater_than_minus_100(self):
        """
        Checks for celsius > 100
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Exercise #22 Vending Machine unit tests.
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


class TestTrafficLight(unittest.TestCase):
    """
    Exercise #23
    """

    def setUp(self):
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_traffic_light_change_state_success(self):
        """
        Checks the correct light change
        """
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Green")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Yellow")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_traffic_light_change_state_failed(self):
        """
        Checks the wrong light change
        """
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Green")

        self.traffic_light.state = "Red"

        self.traffic_light.change_state()
        self.assertIsNot(self.traffic_light.state, "Yellow")
