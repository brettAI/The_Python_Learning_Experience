# Python Logging

## Default LogRecord for for my projects

The default LogRecord format for my projects will be:

    {date} [{thread name}] [{severity}] [{module name}:{function name}:{lineno})] - {message}

The following is the default logging configuration file `logging.json` to be used for my python projects.

```json
{
  "version": 1,
  "disable_existing_loggers": false,
  "formatters": {
    "simple": {
        "class": "logging.Formatter",
        "datefmt": "%I:%M:%S",
        "format": "%(asctime)s [%(threadName)s]  [%(levelname)s] %(module)s:%(funcName)s;%(lineno)d: - %(message)s"
    }
  },

  "handlers": {
    "console": {
      "class": "logging.StreamHandler",
      "level": "DEBUG",
      "formatter": "simple",
      "stream": "ext://sys.stdout"
    },

    "file": {
      "class": "logging.handlers.RotatingFileHandler",
      "level": "DEBUG",
      "formatter": "simple",
      "filename": "AppName.log",
      "maxBytes": 10485760,
      "backupCount": 20,
    }
  },

  "loggers": {
    }
    "root": {
      "level": "DEBUG",
        "handlers": ["console", "file"]
    }
}
```

## Notes

- The default logging level is WARNING
- The Logging module provides:
  - loggers - exposes the interface for application code
  - handlers - sends log records to an appropriate destination
  - filters - fine grained control regarding which log records are output
  - formatters - specify the layout of the log records
- Log information is passed internally in a `LogRecord` instance
- Loggers can have their own name and a hierarchy using dots as separators e.g. 'scan' is the parent of 'scan.text'
- Logs can be written to a variety of locations including:
  - files
  - HTTP GET/POST locations
  - email via SMTP
  - queues
  - OS specific locations (syslog or Windows Event Log)
- `Logger.exception()` is similar to `Logger.error()` but it will also dump a stack trace. This should only be used from an exception handler.
- `getLogger()` returns a reference to a logger instance - pass in the name of a logger to access an existing logger reference.
- Child loggers with use their parent *handlers*.
- The Logging module works with multiple threads

*Loggers* have 3 main jobs:

1. expose methods to log messages at runtime
2. determine which log messages to act upon
3. pass relevant log records to interested handlers

*Handlers* are responsible for sending log records to their required destination.  Handlers can be defined for different severity levels and destinations through `addHandler()`. For example, all messages to a log file and critical errors to an email address.

There are a number handler classes to assist with defining the destination for Log records. Notable handler classes are:
- `RotatingFileHandler` - sends messages to disk files with support for maximum log file size and log file rotation
- `SMTPHandler` - sen messages to a designated email address

*Formatters* configure the order, structure and contents of log messages.

## Best Practice

- Use module-level loggers e.g `logger = logging.getLogger(__name__)`. This ensures messages can be displayed with additional meaningful information regarding where this log record was raised.
- Each logger should have an explicit severity level set, else the logging module needs to traverse the logging tree to determine the *effective level*.
- If the message to be outputted includes expensive methods as part of the message preparation, the `isEnabledFor()` can be used to check if the calls need to be made based on the logging level.  

```python
if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Message with %s, %s', expensive_func1(), expensive_func2())
```

- **Note: ** the call to `isEnablesFor()` can be expensive, if this needs to be called multiple times, store in a local variable instead of calling the method each time.
- When naming a logger use `logger = logging.getLogger(__name__)` as the name of the logger will now match the module (python file) that called this code.
- Use `disable_existing_loggers` else module level loggers may not work as expected.
- Use a JSON logging configuration file

## Logging Configuration

There are 3 configuration options:

1. from Python code
2. from a logging config file read using the `fileConfig()` function
3. a dictionary of configuration information read by the `dictConfig()` function

## Examples

### Example 1 - Logging variable data

To log variable data, use a format string append the variable data as arguments.

```python
import logging
logging.warning('%s before you %s', 'Look', 'leap!')
```

*Note:* The Python logging module uses the old style of % of string formatting. `str.format()` is still available.

### Example 2 - Format of displayed messages

The format of the message can be modified, a full list of options is available from the [LogRecord attributes](https://docs.python.org/3.8/library/logging.html#logrecord-attributes). The following same limits the output to *levelname* severity and *message*.

#### Example 2a - asctime & message

 ```python
 import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
```

*Output:*

```text
2010-12-12 11:41:42,612 is when this event was logged.
```

#### Example 2b - formatted asctime & message

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
```

*Output:*

```text
12/12/2010 11:46:36 AM is when this event was logged.
```

### Example 3 - Logging config from code

The following shows an example of configuring logging through code. THis example:

- defines a logger
- sets the loggers *effective logging level*
- defines a handler that will output to the console
- set the handlers *effective logging level*  **Remember: different handlers can set different levels**
- defines a formatter
- adds the formatter to the handler
- adds the handler to the logger

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

*Output:*

```text
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
2005-03-19 15:10:26,620 - simple_example - INFO - info message
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
2005-03-19 15:10:26,697 - simple_example - ERROR - error message
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
```

### Example 4 - Logging config from 'logging.conf' file

The following shows an example of configuring logging through a 'logging.conf' file and the python module required to access the file.

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

The 'logging.conf' file:

```conf
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

### Example 5 - Using a custom rotator and name to customise log rotation

```python
def namer(name):
    return name + ".gz"

def rotator(source, dest):
    with open(source, "rb") as sf:
        data = sf.read()
        compressed = zlib.compress(data, 9)
        with open(dest, "wb") as df:
            df.write(compressed)
    os.remove(source)

rh = logging.handlers.RotatingFileHandler(...)
rh.rotator = rotator
rh.namer = namer
```


## Logging Levels

| Level    | When it’s used                                                                                                                                                         |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DEBUG    | Detailed information, typically of interest only when diagnosing problems.                                                                                             |
| INFO     | Confirmation that things are working as expected.                                                                                                                      |
| WARNING  | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected. |
| ERROR    | Due to a more serious problem, the software has not been able to perform some function.                                                                                |
| CRITICAL | A serious error, indicating that the program itself may be unable to continue running.                                                                                 |

## References

- [Python Logging Cookbook](https://docs.python.org/3.8/howto/logging-cookbook.html?highlight=logging)
- [Python Logging HowTo](https://docs.python.org/3.8/howto/logging.html?highlight=logging)
