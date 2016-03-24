
from ctypes import c_char_p, byref

from libnfc.nfc import str_nfc_target, nfc_free


def print_nfc_target(pnt, verbose):
    s = c_char_p()
    str_nfc_target(byref(s), pnt, verbose)
    print(s.value.decode(encoding='ascii'))
    nfc_free(s)
