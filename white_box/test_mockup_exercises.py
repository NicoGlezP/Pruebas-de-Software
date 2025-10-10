# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import sys
import unittest
from unittest.mock import MagicMock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)

sys.modules["requests"] = MagicMock()


# 01
class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Mock the requests.get method
        # with patch("requests.get") as mock_get:
        #     mock_get.return_value.status_code = 200
        #     mock_get.return_value.json.return_value = [
        #         {"id": 1, "title": "Title 1", "body": "Body 1"},
        #         {"id": 2, "title": "Title 2", "body": "Body 2"},
        #     ]

        # mock_get = patch('requests.get')
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = [
        #     {"id": 1, "title": "Title 1", "body": "Body 1"},
        #     {"id": 2, "title": "Title 2", "body": "Body 2"},
        # ]

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


# 02
class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Hello world")
    def test_read_data_from_file_success(self, mock_file):
        """
        Test successful file reading
        """
        result = read_data_from_file("testfile.txt")
        # Verifies that the content written was the right one
        self.assertEqual(result, "Hello world")
        # Verifies that open was called with the correct parameters
        mock_file.assert_called_once_with("testfile.txt", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Test non existing file reading
        """
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("nonexistingfile.txt")

        mock_file.assert_called_once_with("nonexistingfile.txt", encoding="utf-8")


# 03
class TestExecuteComand(unittest.TestCase):
    """
    Command execution in a subprocess unittest class
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Test successdul command execution
        """
        mock_process = MagicMock()
        mock_process.stdout = "Hello world\n"
        mock_run.return_value = mock_process
        # Configures mock to simulate succes
        result = execute_command(["echo", "Hello world"])
        # Validate output
        self.assertEqual(result, "Hello world\n")
        mock_run.assert_called_once_with(
            ["echo", "Hello world"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Test command execution with error
        """
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="fakecmd", output="", stderr="Command not found"
        )
        # Simulates error from subprocess.run
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["fakecmd"])


# 04
class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Action based on current time unittest class
    """

    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_perform_action_based_on_time_less_than_10(self, mock_time):
        """
        Action A when current_time < 10
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time", return_value=15)
    def test_perform_action_based_on_time_greater_or_equal_to_10(self, mock_time):
        """
        Action B when current_time >= 10
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()


# class TestPrint(unittest.TestCase):
#     """
#     fetch_data_from_api unittest class.
#     """
#
#     def test_print(self):
#         # Mock the requests.get method
#         mock_print = patch('__main__.print')
#
#         print_hello_world()
#
#         # Verify data is what we expect
#         mock_print.assert_called_once_with("Hello, World!")
