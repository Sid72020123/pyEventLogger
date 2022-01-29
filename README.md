# pyEventLogger v1.0

pyEventLogger is a simple Python Library for making customized Logs of certain events that occur in a program. The logs can
be fully customized and can be printed in colored format or can be stored in a file.

**Note: Your software or the console in which you are going to print _colored logs_ should support the ANSI Escape
Sequences or the _colored logs_ feature may not work!**

## Installation

To install this library, type:

```bash
pip install pylogger
```

in the Command Prompt or Terminal

## Import

To import this library, use the following code:

```python
from pyEventLogger import pyLogger
```

## Logging Levels:

There are 6 different types of logs in this library. In order of increasing importance, they are:

* Debug
* Info
* Warning
* Success
* Error
* Critical

## Print basic logs:

Use the following program to print basic logs in the Console:

```python
from pyEventLogger import pyLogger  # Import the library

logger = pyLogger(colored_output=True)  # Make an object of the pyLogger Class
# Note: If your console doesn't support the ANSI Escape Sequences then use: colored_output=False

logger.debug(message="This is Debug Message!")  # Debug Log
logger.info(message="This is Information Message!")  # Information Log
logger.warn(message="This is Warning Message!")  # Warning Log
logger.success(message="This is Success Message!")  # Success Log
logger.error(message="This is Error Message!")  # Error Log
logger.critical(message="This is Critical Message!")  # Critical Log
```

## The pyLogger Class

### Parameters

The pyLogger Class has the following Parameters:

* ```colored_output``` --> Set it to ```True``` if you want colored output
* ```print_log``` --> Set it to ```True``` if you want your log to be printed out into the Console
* ```make_file``` --> Set it to ```True``` if you want your log to be stored in a file
* ```file_name``` --> If you set the ```make_file``` parameter to ```True```, then you can use this parameter to change
  the file name
* ```rewrite_file``` --> Set it to ```True``` if you want your log file to be rewritten after you run the program
* ```file_logs``` --> If you want only the specified log messages in your file then pass this parameter with a list
  containing the log types you want. Example: If you want only the errors and critical messages in file then you pass
  the value of the parameter as ```python ['ERROR', 'CRITICAL']```

## Customizing the Logs:

### Customizing the Log text:

To customize a log, use the ```format_log(log_type, format_string)``` function. For example, if you want to customize
the log type of Debug, then use the following code:

```python
from pyEventLogger import pyLogger

logger = pyLogger()

debug_format_string = "[log_type] [time] [message]"  # Define a variable for the format string

logger.format_log(log_type='DEBUG', format_string=debug_format_string)  # Use this function to format a log

logger.debug(message="This is Debug Message!")
```

See the above example. It has a variable called ```debug_format_string``` which defines how the contents of the Log
should be.

#### Rules for format strings:

The format string should have a format like ```"[time] [log_type] [message]"```. Where the contents in the squared
braces ```[]``` will be replaced with the values of the parameters you pass to that function. You can give any number of
spaces you like between the contents. Example:
```"[log_type]     [time]      [message]"```. The log will be printed in the same format and also can be written in a
file in the same format.

There are some special meanings to some parameters like ```log_type```. The program automatically adds the log type even
if the user doesn't pass that parameter's value to a function, also the ```time``` parameter will be given a default
value of the time that function is called.

You can add any number of contents in a log. Example Code:

```python
from pyEventLogger import pyLogger

logger = pyLogger()

debug_format_string = "[log_type] [time] [message] [file_name]"  # Add a 'file_name' content

logger.format_log(log_type='DEBUG', format_string=debug_format_string)

logger.debug(message="This is Debug Message!", file_name="main.py")  # Set a value to the added content
```

### Customizing the Log text color/style:

To customize a log's color, use the ```format_log_color(log_type, format_string)``` function. For example, if you want
to customize the log type of Debug, then use the following code:

```python
from pyEventLogger import pyLogger

logger = pyLogger(colored_output=True)  # Set the colored output to True

debug_format_string = "[log_type] [time] [file_name] [message]"  # Define a variable for the format string
debug_format_color = "[bold cyan black] [normal yellow black] [italic magenta black] [normal white black]"  # Define a variable for the format color

logger.format_log(log_type='DEBUG', format_string=debug_format_string)  # Format the log
logger.format_log_color(log_type='DEBUG', format_string=debug_format_color)  # Format the color

logger.debug(message="This is Debug Message!", file_name="main.py")
```

In the above example, you can see that there is a variable defined for the log color.

#### Rules for format color:

The format of color string should be the same as text string.

The contents should be seperated by space.

The first content in square braces should be the text style like ```normal```, ```bold```,```italic```,etc.

The second content should be the text color and the third should be background color. You can also use HEX values for
colors too!

These three elements should be seperated by a space.

The first content will be the style for first item in log and so on...

### Changing the format of time:

To change the format of time, use the ```format_time``` variable of the ```pyLogger``` class It should be in string
format and is the same format as used in Python ```time.strftime()``` function.

### Including error messages in error and critical log:

To include the error messages along with the log message in error and critical logs, set the ```include_error_message```
parameter of the error and critical functions to ```True```

## Example Code:

```python
import time
import random
from pyEventLogger import pyLogger

logger = pyLogger(colored_output=False, make_file=True, file_name='math', rewrite_file=True)

logger.format_log(log_type="INFO", format_string="[time] [log_type] [message] [answer]")
logger.format_log_color(log_type="INFO",
                        format_string="[bold yellow black][bold magenta black][normal #FFFFFF black][italic green black]")

while True:
    try:
        logger.debug(message="Taking two random numbers...")
        n1 = random.randint(-10, 10)
        n2 = random.randint(-10, 10)
        logger.debug(message="Successfully found two random numbers!")

        logger.info(message=f"Two numbers are {n1} and {n2}")

        logger.debug(message="Starting operations with two numbers...")
        addition = n1 + n2
        logger.info(message="Added two numbers:", answer=addition)
        subtraction = n2 - n1
        logger.info(message="Subtracted two numbers:", answer=subtraction)
        multiplication = n1 * n2
        logger.info(message="Multiplied two numbers:", answer=multiplication)
        division = n2 / n1
        logger.info(message="Divided two numbers:", answer=division)

        logger.success(message="Successfully completed operations with two numbers!")
    except ZeroDivisionError:
        logger.error(message="An Error Occurred!", include_error_message=True)
    time.sleep(10)

```

## Change Log:

* 15/01/2022(v0.1) - First made this library and updated it
* 15/01/2022(v0.1.2) - Updated and added many features
* 21/01/2022(v0.5.0) - Updated and added some other features
* 23/01/2022(v0.7) - Added Exceptions
* 27/01/2022(v0.9) - Added features to error and critical logs
* 28/01/2022(v1.0) - Added doc-strings to code\
* 29/01/2022(v1.0) - First Release!

## Thank You!
