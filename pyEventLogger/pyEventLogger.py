"""
The Main File
"""
import time
import traceback

import pyTextColor
from pyEventLogger import Exceptions

pytxtc = pyTextColor.pyTextColor()
color = pytxtc.color
style = pytxtc.style
bg = pytxtc.background
reset = pytxtc.reset

_logging_levels = ['DEBUG', 'INFO', 'WARN', 'SUCCESS', 'ERROR', 'CRITICAL']

_default_log_format = {
    'DEBUG': "[time] [log_type] [message]",
    'INFO': "[time] [log_type] [message]",
    'WARN': "[time] [log_type] [message]",
    'SUCCESS': "[time] [log_type] [message]",
    'ERROR': "[time] [log_type] [message]",
    'CRITICAL': "[time] [log_type] [message]",
}
_default_log_format_color = {
    'DEBUG': "[normal yellow black][bold cyan black][normal white black]",
    'INFO': "[bold yellow black][bold magenta black][normal #FFFFFF black]",
    'WARN': "[bold yellow black][bold yellow black][bold black yellow]",
    'SUCCESS': "[bold yellow black][bold green black][bold #FFFFFF black]",
    'ERROR': "[bold #FF0000 black][bold red black][bold #FF0000 black]",
    'CRITICAL': "[bold #FF0000 yellow][bold #FF0000 yellow][bold #FF0000 yellow]",
}


class pyLogger:
    def __init__(self, colored_output=False, print_log=True, make_file=False, file_name="events", rewrite_file=False,
                 file_logs=None):
        """
        The pyLogger Class
        :param colored_output: Set it to True if you want colored output
        :param print_log: Set it to True if you want your log to be printed out into the Console
        :param make_file: Set it to True if you want your log to be stored in a file
        :param file_name: If you set the 'make_file' parameter to True, then you can use this parameter to change the file name
        :param rewrite_file: Set it to True if you want your log file to be rewritten after you run the program
        :param file_logs: If you want only the specified log messages in your file then pass this parameter with a list containing the log types you want. Example: If you want only the errors and critical messages in file then you pass the value of the parameter as ['ERROR', 'CRITICAL']
        """
        self.colored_output = colored_output
        self.print_log = print_log
        self.make_file = make_file
        self.file_name = file_name
        self.rewrite_file = rewrite_file
        if file_logs is None:
            self.file_logs = _logging_levels
        else:
            self.file_logs = file_logs

        self.format_time = "%Y-%m-%d %H:%M:%S"

        self.log_format = {
            'DEBUG': {'Format': [], 'Color': []},
            'INFO': {'Format': [], 'Color': []},
            'WARN': {'Format': [], 'Color': []},
            'SUCCESS': {'Format': [], 'Color': []},
            'ERROR': {'Format': [], 'Color': []},
            'CRITICAL': {'Format': [], 'Color': []},
        }

        if self.make_file and self.rewrite_file:
            file = open(f"{self.file_name}.log", "w")
            file.close()

    def debug(self, **logs):
        """
        Debug Log
        """
        if self.print_log:
            print(self._make_log(lt='DEBUG', file=False, **logs))
        if self.make_file and 'DEBUG' in self.file_logs:
            self._write_file(fn=f"{self.file_name}.log", s=self._make_log(lt='DEBUG', file=True, **logs))
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def info(self, **logs):
        """
        Information Log
        """
        if self.print_log:
            print(self._make_log(lt='INFO', file=False, **logs))
        if self.make_file and 'INFO' in self.file_logs:
            self._write_file(fn=f"{self.file_name}.log", s=self._make_log(lt='INFO', file=True, **logs))
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def warn(self, **logs):
        """
        Warning Log
        """
        if self.print_log:
            print(self._make_log(lt='WARN', file=False, **logs))
        if self.make_file and 'WARN' in self.file_logs:
            self._write_file(fn=f"{self.file_name}.log", s=self._make_log(lt='WARN', file=True, **logs))
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def success(self, **logs):
        """
        Success Log
        """
        if self.print_log:
            print(self._make_log(lt='SUCCESS', file=False, **logs))
        if self.make_file and 'SUCCESS' in self.file_logs:
            self._write_file(fn=f"{self.file_name}.log", s=self._make_log(lt='SUCCESS', file=True, **logs))
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def error(self, include_error_message=False, **logs):
        """
        Error Log
        :param include_error_message: Set it to True if you want the error message to be printed out along with the log. Also setting this to True will include the error message in file too
        """
        if self.print_log:
            print(self._make_log(lt='ERROR', file=False, **logs))
            if include_error_message:
                traceback.print_exc()
        if self.make_file and 'ERROR' in self.file_logs:
            exception = ""
            if include_error_message:
                exception = "\n\t" + traceback.format_exc().replace("\n", "\n\t")
            self._write_file(fn=f"{self.file_name}.log",
                             s=self._make_log(lt='ERROR', file=True, **logs) + exception)
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def critical(self, include_error_message=False, **logs):
        """
        Critical Log
        :param include_error_message: Set it to True if you want the error message to be printed out along with the log. Also setting this to True will include the error message in file too
        """
        if self.print_log:
            print(self._make_log(lt='CRITICAL', file=False, **logs))
            if include_error_message:
                traceback.print_exc()
        if self.make_file and 'CRITICAL' in self.file_logs:
            exception = ""
            if include_error_message:
                exception = "\n\t" + traceback.format_exc().replace("\n", "\n\t")
            self._write_file(fn=f"{self.file_name}.log", s=self._make_log(lt='CRITICAL', file=True, **logs) + exception)
        elif not (self.print_log or self.make_file):
            raise Exceptions.LogOptionException(
                "One of the 'print_log' or 'make_file' parameters of the pyLogger class should be True.")

    def format_log(self, log_type, format_string):
        """
        Format the Log
        :param log_type: The log type. Input multiple log types in a list to change at once!
        :param format_string: The format string
        """
        if not type(log_type) is list:
            log_type = [log_type]
        for item in log_type:
            if item in _logging_levels:
                self.log_format[item]['Format'] = self._parse_format_log_text(format_string, False)
            else:
                raise Exceptions.LogTypeException(f"Invalid log type given. Use one from {_logging_levels}")

    def format_log_color(self, log_type, format_string):
        """
        Format the Log Color
        :param log_type: The log type. Input multiple log types in a list to change at once!
        :param format_string: The format string
        """
        if not type(log_type) is list:
            log_type = [log_type]
        for item in log_type:
            if item in _logging_levels:
                self.log_format[item]['Color'] = self._parse_format_log_text(format_string, True)
            else:
                raise Exceptions.LogTypeException(f"Invalid log type given. Use one from {_logging_levels}")

    def _make_log(self, lt, file, **commands):
        """
        DON'T USE THIS
        """
        if len(self.log_format[lt]['Format']) == 0:
            self.format_log(log_type=lt, format_string=_default_log_format[lt])
        if len(self.log_format[lt]['Color']) == 0 and self.colored_output is True:
            self.format_log_color(log_type=lt, format_string=_default_log_format_color[lt])
        format = list(self.log_format[lt]['Format'])

        if self.colored_output and not file:
            c = list(self.log_format[lt]['Color'])
            log = ""
            index = 0
            for i in format:
                for j in commands:
                    if i == j:
                        s, tc, bgc = c[index].split(" ")
                        log += f"{bg(bgc)}{color(tc)}{style(s)}{commands[j]}{reset()}{bg(bgc)}"
                        index += 1
                if i == " ":
                    log += " "
                elif i == "time" and "time" not in commands:
                    temp_format = list(format)
                    for i in range(0, temp_format.count(" ")):
                        temp_format.remove(" ")
                    s, tc, bgc = c[temp_format.index("time")].split(" ")
                    log += f"{bg(bgc)}{color(tc)}{style(s)}{time.strftime(self.format_time)}{reset()}{bg(bgc)}"
                    index += 1
                elif i == "log_type" and "log_type" not in commands:
                    temp_format = list(format)
                    for i in range(0, temp_format.count(" ")):
                        temp_format.remove(" ")
                    s, tc, bgc = c[temp_format.index("log_type")].split(" ")
                    log += f"{bg(bgc)}{color(tc)}{style(s)}{lt}{reset()}{bg(bgc)}"
                    index += 1
            return log
        else:
            log = ""
            for i in format:
                for j in commands:
                    if i == j:
                        log += str(commands[j])
                if i == " ":
                    log += " "
                elif i == "time" and "time" not in commands:
                    log += str(time.strftime(self.format_time))
                elif i == "log_type" and "log_type" not in commands:
                    log += str(lt)
            return log

    def _parse_format_log_text(self, ft, c):
        """
        DON'T USE THIS
        """
        text = list(ft)
        result = []
        i = 0
        while i < len(text):
            if text[i] == "[":
                temp_str = ""
                for j in text[i + 1:]:
                    if j == "]":
                        result.append(temp_str.strip())
                        i += 1
                        break
                    else:
                        temp_str += j
                    i += 1
            elif text[i] == " " and c is False:
                result.append(text[i])
            i += 1
        return result

    def _write_file(self, fn, s):
        """
        DON'T USE THIS
        """
        file = open(fn, "a+")
        file.write(f"{s}\n")
        file.close()
