import logging


def log_label(obj=None, function_name=True):
    parts = []
    if obj:
        parts += [obj.__class__.__module__, obj.__class__.__name__]
    if function_name:
        parts += [callersname()]
    if parts[0] == '__main__':
        del parts[0]
    return '[%s]' % '.'.join(parts)


def configure_logger(level):
    # if someone tried to log something before basicConfig is called, Python
    # creates a default handler that
    # goes to the console and will ignore further basicConfig calls. Remove the
    # handler if there is one.
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    logging.basicConfig(level=level,
                        format="%(asctime)s-%(name)s-%(levelname)s:%(message)s")
