import sys
import logging


def whoami():
    return sys._getframe(1).f_code.co_name

# this uses argument 1, because the call to whoami is now frame 0.
# and similarly:
def callersname():
    return sys._getframe(2).f_code.co_name


def log_label(obj=None, function_name=True):
    parts = []
    if obj:
        parts += [obj.__class__.__module__, obj.__class__.__name__]
    if function_name:
        parts += [callersname()]
    if parts[0] == '__main__':
        del parts[0]
    return '[%s]' % '.'.join(parts)


def configure_logger(level,
                     format="%(asctime)s-%(name)s-%(levelname)s:%(message)s"):
    # if someone tried to log something before basicConfig is called, Python
    # creates a default handler that
    # goes to the console and will ignore further basicConfig calls. Remove the
    # handler if there is one.
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    logging.basicConfig(level=level, format=format)


def get_log_level_parser_args(choices=('info', 'debug', 'warning', 'error',
                                      'critical'), default_level='warning'):
    '''
    Can be used with configure_logger to set the log level using a command-line
    argument.

    For example:

    >>>configure_logger(eval('logging.%s' % args.log_level.upper()))
    '''
    return ('--log_level', ), dict(choices=choices, default=default_level)
