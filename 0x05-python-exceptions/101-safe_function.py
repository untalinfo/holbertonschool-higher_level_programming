#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as zdiv:
        print("Exception: {}".format(zdiv), file=sys.stderr)
    except IndexError as iderr:
        print("Exception: {}".format(iderr), file=sys.stderr)
    except:
        raise
        return None
