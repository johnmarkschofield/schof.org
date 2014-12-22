Title: Basic Python Logging
Date: 2010-04-01 00:00
Author: schof
Category: Python Programming, Technology
Tags: documentation, logging, programming, python
Slug: basic-python-logging

I was listening to the [A Little Bit of
Python](http://advocacy.python.org/podcasts/) podcast and heard them
discuss the difficulty of logging with the standard Python logging
module. I was a little surprised, because I don't think it's THAT hard
to use. The logging module, quite frankly, requires a lot of boilerplate
code you find yourself writing over and over again -- but it's not
rocket science, either. I figured I'd provide a working example pretty
similar to code I use in production, and then walk you through how it
all goes together. I highly recommend also looking through the [logging
module documentation](http://docs.python.org/library/logging.html). So,
here's the final result:

``` {lang="python"}
def configure_logger(log_file):
  """Accepts a fully-qualified filename to the log file.
  Logs at DEBUG to file and at WARNING to stdout.
  Returns a fully-configured logger object.
  """
  logger = logging.getLogger('ProgramName')
  log_formatter = logging.Formatter(
  "%(name)s: %(asctime)s - %(levelname)s: %(message)s")
  file_handler = logging.FileHandler(log_file)
  file_handler.setFormatter(log_formatter)
  file_handler.setLevel(logging.DEBUG)
  stream_handler = logging.StreamHandler(sys.stdout)
  stream_handler.setFormatter(log_formatter)
  stream_handler.setLevel(logging.WARNING)
  logger.setLevel(logging.DEBUG)
  logger.addHandler(file_handler)
  logger.addHandler(stream_handler)
  return logger
```

I've got [this working Python
code](//github.com/johnmarkschofield/python-logging-examples/blob/master/basic_python_logging.py)
in a github repo; feel free to download and use it. Now that you've got
the overview, let's look at it piece-by-piece. The first step (after
importing the necessary modules, of course) is to create the logging
object.

``` {lang="python"}
import logging
logger = logging.getLogger('my program name')
```

Next we have to set up the logging formatter. This, as the name says,
controls the format of the lines the logging module outputs. Modify this
to fit your needs and preferences.

``` {lang="python"}
log_formatter = logging.Formatter("%(name)s: %(asctime)s - %(levelname)s: %(message)s")
```

This just defines the formatter; you'll apply it later. You'll also have
to define a handler (or more than one). Each handler determines where
the log output is written; you can specify more than one so you can, for
instance, write to both the screen and to disk.

``` {lang="python"}
stream_handler = logging.StreamHandler()
```

Then we apply the formatter to the handler:

``` {lang="python"}
stream_handler.setFormatter(log_formatter)
```

We'll also need to set to the log level of the handler. There are five
default log levels: logging.DEBUG, logging.INFO, logging.WARNING,
logging.ERROR, and logging.CRITICAL.

``` {lang="python"}
stream_handler.setLevel(logging.INFO)
```

In addition to setting the loglevel for the handler, you'll need to set
the loglevel for the logging object as a whole. This lets you, for
instance, log at different levels to the screen and to a file.

``` {lang="python"}
logger.setLevel(logging.DEBUG)
```

And then you'll need to configure the logger to use the handler:

``` {lang="python"}
logger.addHandler(stream_handler)
```

Now you've got a fully-configured logger you can use to log messages:

``` {lang="python"}
logger.debug('This is a debug message.')
logger.warning('And this is a warning message.')
```

That would give the following output:

    my program name: 2010-04-01 22:23:59,707 - WARNING: And this is a warning message.

The reason we don't see any output from the debug line is that we set
the log level of the stream handler to INFO, so a DEBUG log line (lower
than INFO) doesn't get printed. This is true even though we set the
logger itself to use DEBUG. The logger is at DEBUG, so it sends
everything at DEBUG or higher to the stream handler, but the stream
handler is at INFO, so it prints everything at INFO or higher,
discarding DEBUG level messages. The logging module can do other cool
things, like rotate log files when they get too big or too old, or
handle logging from multiple threads. NOTE: In the same way only
amateurs drink on St. Patrick's day, only the unfunny play jokes on
April Fool's Day. This page is for real.

