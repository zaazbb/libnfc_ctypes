
from sys import argv
from signal import signal, SIGINT
from ctypes import POINTER, byref

try:
    from libnfc.nfc import *
    from libnfc.utils.nfc_utils import print_nfc_target
except ImportError:
    import sys
    sys.path.append('..')
    from libnfc.nfc import *
    from utils.nfc_utils import print_nfc_target


pnd = POINTER(nfc_device)()
context = POINTER(nfc_context)()


def stop_polling(sig):
    if pnd:
        nfc_abort_command(pnd)
    else:
        nfc_exit(context)
        exit(EXIT_FAILURE)

def print_usage(progname):
    print("usage: %s [-v]\n" % progname)
    print("  -v\t verbose display\n")

def ERR(msg):
    print(msg)

def print_nfc_target(pnt, verbose):
    s = c_char_p()
    str_nfc_target(byref(s), pnt, verbose)
    print(s.value.decode(encoding='ascii'))
    nfc_free(s)


if __name__ == '__main__':
    argc = len(argv)
    verbose = False
    
    signal(SIGINT, stop_polling)
    acLibnfcVersion = nfc_version()
    print("%s uses libnfc %s\n" % (argv[0], acLibnfcVersion))
    if argc != 1:
        if argc == 2 and argv[1] == '-v':
            verbose = True
        else:
            print_usage(argv[0])
            exit(EXIT_FAILURE)

    uiPollNr = 20
    uiPeriod = 2
    nmModulations = (nfc_modulation * 5)(
        nfc_modulation(nmt=NMT_ISO14443A, nbr=NBR_106),
        nfc_modulation(nmt=NMT_ISO14443B, nbr=NBR_106),
        nfc_modulation(nmt=NMT_FELICA, nbr=NBR_212),
        nfc_modulation(nmt=NMT_FELICA, nbr=NBR_424),
        nfc_modulation(nmt=NMT_JEWEL, nbr=NBR_106))
    szModulations = len(nmModulations)
    
    nt = nfc_target()
    res = 0

    nfc_init(byref(context))
    if not context:
        ERR("Unable to init libnfc (malloc)")
        exit(EXIT_FAILURE)

    pnd = nfc_open(context, None)

    if not pnd:
        ERR("Unable to open NFC device.")
        nfc_exit(context)
        exit(EXIT_FAILURE)

    if nfc_initiator_init(pnd) < 0:
        nfc_perror(pnd, "nfc_initiator_init")
        nfc_close(pnd)
        nfc_exit(context)
        exit(EXIT_FAILURE)
        
    print("NFC reader: %s opened\n" % nfc_device_get_name(pnd))
    print(("NFC device will poll during"
          " %ld ms (%u pollings of %lu ms for %i modulations)\n") % \
          (uiPollNr * szModulations * uiPeriod * 150,
           uiPollNr,
           uiPeriod * 150, szModulations))
    res = nfc_initiator_poll_target(pnd,
                                    nmModulations,
                                    szModulations,
                                    uiPollNr,
                                    uiPeriod,
                                    byref(nt))
    if res < 0:
        nfc_perror(pnd, "nfc_initiator_poll_target")
        nfc_close(pnd)
        nfc_exit(context)
        exit(EXIT_FAILURE)

    if res > 0:
        print_nfc_target(byref(nt), verbose);
    else:
        print("No target found.\n")

    print("Waiting for card removing...")
    while (0 == nfc_initiator_target_is_present(pnd, None)):
        pass
    nfc_perror(pnd, "nfc_initiator_target_is_present")
    print("done.\n")

    nfc_close(pnd)
    nfc_exit(context)
    exit(EXIT_SUCCESS)
