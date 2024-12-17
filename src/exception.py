import sys
import os
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # File name where the error occurred
    line_number = exc_tb.tb_lineno  # Line number where the error occurred
    error_message = "Error occurred in python script name [{0}] line no [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


# if __name__ == '__main__':
#     try:
#         a = 1 / 0  # Intentional error
#     except Exception as e:
#         logging.info("Logging started")
#         raise CustomException(e, sys)
