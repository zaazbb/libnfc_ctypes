# by jf
# zaazbb <zaazbb@163.com>
# https://github.com/zaazbb/libnfc_ctypes

import collections

from ._nfc import *


(EXIT_SUCCESS, EXIT_FAILURE) = (0, 1)

(
    NMT_ISO14443A,
    NMT_JEWEL,
    NMT_ISO14443B,
    NMT_ISO14443BI,     # pre-ISO14443B aka ISO/IEC 14443 B' or Type B'
    NMT_ISO14443B2SR,   # ISO14443-2B ST SRx
    NMT_ISO14443B2CT,   # ISO14443-2B ASK CTx
    NMT_FELICA,
    NMT_DEP
) = range(1, 9)

(
    NBR_UNDEFINED,
    NBR_106,
    NBR_212,
    NBR_424,
    NBR_847,
) = range(5)

(
    NDM_UNDEFINED,
    NDM_PASSIVE,
    NDM_ACTIVE
) = range(3)


def nfc_version():
    return nfc_version_().decode()

def nfc_device_get_name(nfc_device):
    return nfc_device_get_name_(nfc_device).decode()

def nfc_perror(pnd, pcString):
    nfc_perror_(pnd, pcString.encode())


