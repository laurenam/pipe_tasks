from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def qaTimeout(timeout = 60, errMsg = os.strerror(errno.ETIME)):

    def decorator(func):

        def _timeoutHandler(signalNumber, frame):
#            if errMsg is None:
#                errMsg = 'Timeout (%d sec) has been detected' % (timeout)
            raise TimeoutError(errMsg)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _timeoutHandler)
            signal.alarm(timeout)

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)

            return result

        return wraps(func)(wrapper)

    return decorator


