import unittest
from unittest.mock import patch

class TestBmsSenderClass(unittest.TestCase):
    """ this class contains methods to test methods in bms_sender """
    def test_send_to_console(self):
        """ this test case is to test send_to_console method """
        from bms_code.bms_sender import send_to_console
        with patch('builtins.print') as mock_print:
            send_to_console("Hello")
            mock_print.assert_called_once_with('Hello')       

    def test_bms_generate_format_send(self):
        """ this test case is to test bms_sender method sending one message to console """
        from bms_code.bms_sender import send_to_console
        with patch('builtins.print') as mock_print:
            send_to_console("Hello")
            mock_print.assert_called_once()        