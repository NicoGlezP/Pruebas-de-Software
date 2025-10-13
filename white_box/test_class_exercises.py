# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
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
        items = [{"weight": 5}, {"weight": 5}, {"weight": 1}]
        shipping_method = "express"
        self.assertEqual(calculate_items_shipping_cost(items, shipping_method), 40)


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


class TestValidateCreditCard(unittest.TestCase):
    """
    Exercise #11
    """

    def test_validate_credit_card_valid(self):
        """
        Checks for card_number digit between 13 and 16
        """
        self.assertEqual(validate_credit_card("33452845681245"), "Valid Card")

    def test_validate_credit_card_invalid_no_1(self):
        """
        Checks for card_number digit and not between 13 and 16
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_invalid_no_2(self):
        """
        Checks for card_number not digit
        """
        self.assertEqual(validate_credit_card("This is invalid"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """
    Exercise #12
    """

    def test_validate_date_valid(self):
        """
        Checks for date with correct year, month and day
        """
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_invalid_no_1(self):
        """
        Checks for date with correct month and day and wrong year
        """
        self.assertEqual(validate_date(1899, 1, 1), "Invalid Date")

    def test_validate_date_invalid_no_2(self):
        """
        Checks for date with correct year and day and wrong month
        """
        self.assertEqual(validate_date(1900, 13, 1), "Invalid Date")

    def test_validate_date_invalid_no_3(self):
        """
        Checks for date with correct year and month and wrong day
        """
        self.assertEqual(validate_date(1900, 1, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """
    Exercise #13
    """

    def test_check_flight_eligibility_eligible_no_1(self):
        """
        Checks for age between 18 and 65 and not frequent flyer
        """
        self.assertEqual(
            check_flight_eligibility(18, frequent_flyer=False), "Eligible to Book"
        )

    def test_check_flight_eligibility_eligible_no_2(self):
        """
        Checks for age not between 18 and 65 and frequent flyer
        """
        self.assertEqual(
            check_flight_eligibility(17, frequent_flyer=True), "Eligible to Book"
        )

    def test_check_flight_eligibility_not_eligible(self):
        """
        Checks for age not between 18 and 65 and not frequent flyer
        """
        self.assertEqual(
            check_flight_eligibility(66, frequent_flyer=False), "Not Eligible to Book"
        )


class TestValidateUrl(unittest.TestCase):
    """
    Exercise #14
    """

    def test_validate_url_valid_no_1(self):
        """
        Checks for url <= 255 and with http://
        """
        self.assertEqual(validate_url("http://testurl"), "Valid URL")

    def test_validate_url_valid_no_2(self):
        """
        Checks for url <= 255 and with https://
        """
        self.assertEqual(validate_url("https://testurl"), "Valid URL")

    def test_validate_url_invalid_no_1(self):
        """
        Checks for url <= 255 and not with http:// or https://
        """
        self.assertEqual(validate_url("http:/testurl"), "Invalid URL")

    def test_validate_url_invalid_no_2(self):
        """
        Checks for url > 255
        """
        url = "http://testurl"
        i = 0
        while i < 255:
            url += "0"
            i += 1
        self.assertEqual(validate_url(url), "Invalid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """
    Exercise #15
    """

    def test_calculate_quantity_discount_no_discount(self):
        """
        Checks for quantity between 1 and 5
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5(self):
        """
        Checks for quantity between 6 and 10
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10(self):
        """
        Checks for quantity > 10
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """
    Exercise #16
    """

    def test_check_file_size_valid(self):
        """
        Checks for size_in_bytes between 0 and 1048576
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_invalid(self):
        """
        Checks for size_in_bytes not between 0 and 1048576
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """
    Exercise #17
    """

    def test_check_loan_eligibility_not_eligible(self):
        """
        Checks for income < 30000
        """
        self.assertEqual(check_loan_eligibility(29999, 700), "Not Eligible")

    def test_check_loan_eligibility_standard_no_1(self):
        """
        Checks for income between 30000 and 60000 and credit_score > 700
        """
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_check_loan_eligibility_secured(self):
        """
        Checks for income between 30000 and 60000 and credit_score <= 700
        """
        self.assertEqual(check_loan_eligibility(60000, 700), "Secured Loan")

    def test_check_loan_eligibility_premium(self):
        """
        Checks for income > 60000 and credit_score > 750
        """
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")

    def test_check_loan_eligibility_standard_no_2(self):
        """
        Checks for income > 60000 and credit_score <= 750
        """
        self.assertEqual(check_loan_eligibility(60001, 750), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """
    Exercise #18
    """

    def test_calculate_shipping_cost_5(self):
        """
        Checks for weight <= 1 and length <= 10 and width <= 10 and height <= 10
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_10(self):
        """
        Checks for 1 < weight <= 5 and any dimension between 11 and 30
        """
        self.assertEqual(calculate_shipping_cost(1.01, 11, 11, 11), 10)

    def test_calculate_shipping_cost_20(self):
        """
        Checks for weight > 5 or any dimension > 30
        """
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30.01), 20)


class TestGradeQuiz(unittest.TestCase):
    """
    Exercise #19
    """

    def test_grade_quiz_pass(self):
        """
        Checks for correct_answers >= 7 and incorrect_answers <= 2
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_cond_pass(self):
        """
        Checks for correct_answers >= 5 and incorrect_answers <= 3
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """
        Checks for correct_answers < 5 or incorrect_answers > 3
        """
        self.assertEqual(grade_quiz(10, 4), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """
    Exercise #20
    """

    def test_authenticate_user_admin(self):
        """
        Checks for username = admin and password = admin123
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_user(self):
        """
        Checks for username >= 5 and password >= 8
        """
        self.assertEqual(authenticate_user("user1", "pass5678"), "User")

    def test_authenticate_user_invalid(self):
        """
        Checks for username < 5 or password < 8
        """
        self.assertEqual(authenticate_user("user", "pass5678"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """
    Exercise #21
    """

    def test_get_weather_advisory_stay_hydrated(self):
        """
        Checks for temperature > 30 and humidity > 70
        """
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_bundle_up(self):
        """
        Checks for temperature < 0
        """
        self.assertEqual(get_weather_advisory(-0.01, 71), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_no_advisory(self):
        """
        Checks for temperature >= 0 and <= 30 or humidity <= 70
        """
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Exercise #22
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


class TestUserAuthentication(unittest.TestCase):
    """
    Exercise #24
    """

    def setUp(self):
        self.user_authentication = UserAuthentication()
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_user_authentication_success(self):
        """
        Checks the correct login and logout
        """
        self.assertEqual(self.user_authentication.login(), "Login successful")
        self.assertEqual(self.user_authentication.state, "Logged In")
        self.assertEqual(
            self.user_authentication.login(), "Invalid operation in current state"
        )

        self.assertEqual(self.user_authentication.logout(), "Logout successful")
        self.assertEqual(self.user_authentication.state, "Logged Out")
        self.assertEqual(
            self.user_authentication.logout(), "Invalid operation in current state"
        )


class TestDocumentEditingSystem(unittest.TestCase):
    """
    Exercise #25
    """

    def setUp(self):
        self.document_editing_system = DocumentEditingSystem()
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_document_editing_system_success(self):
        """
        Checks the correct savind and editing of document
        """
        self.assertEqual(
            self.document_editing_system.save_document(), "Document saved successfully"
        )
        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(
            self.document_editing_system.save_document(),
            "Invalid operation in current state",
        )

        self.assertEqual(
            self.document_editing_system.edit_document(), "Editing resumed"
        )
        self.assertEqual(self.document_editing_system.state, "Editing")
        self.assertEqual(
            self.document_editing_system.edit_document(),
            "Invalid operation in current state",
        )


class TestElevatorSystem(unittest.TestCase):
    """
    Exercises #26
    """

    def setUp(self):
        self.elevator_system = ElevatorSystem()
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_elevator_system_success(self):
        """
        Checks the correct moving up, down and stoping
        """
        self.assertEqual(self.elevator_system.move_up(), "Elevator moving up")
        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(
            self.elevator_system.move_up(), "Invalid operation in current state"
        )
        self.assertEqual(
            self.elevator_system.move_down(), "Invalid operation in current state"
        )

        self.assertEqual(self.elevator_system.stop(), "Elevator stopped")
        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(
            self.elevator_system.stop(), "Invalid operation in current state"
        )

        self.assertEqual(self.elevator_system.move_down(), "Elevator moving down")
        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(
            self.elevator_system.move_down(), "Invalid operation in current state"
        )
        self.assertEqual(
            self.elevator_system.move_up(), "Invalid operation in current state"
        )

        self.assertEqual(self.elevator_system.stop(), "Elevator stopped")
