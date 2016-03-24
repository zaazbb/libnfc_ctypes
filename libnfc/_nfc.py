# by jf
# zaazbb <zaazbb@163.com>
# https://github.com/zaazbb/libnfc_ctypes

from ctypes import *


_libnfc = CDLL('/usr/lib/libnfc.so')


DEVICE_NAME_LENGTH = 256
NFC_BUFSIZE_CONNSTRING = 1024

nfc_connstring = c_char * NFC_BUFSIZE_CONNSTRING


class nfc_user_defined_device(Structure):
    _fields_ = [('name', c_char_p * DEVICE_NAME_LENGTH),
                ('connstring', nfc_connstring),
                ('optional', c_bool)]

class nfc_context(Structure):
     _fields_ = [('allow_autoscan', c_bool),
                 ('allow_intrusive_scan', c_bool),
                 ('log_level', c_uint32),
                 ('user_defined_devices', nfc_user_defined_device),
                 ('user_defined_device_count', c_uint)]

class nfc_device(Structure):
    pass
nfc_device._fields_ = [('context', POINTER(nfc_context)),
                       ('driver', POINTER(nfc_device)),
                       ('deiver_data', c_void_p),
                       ('chip_data', c_void_p),
                       ('name', c_char * DEVICE_NAME_LENGTH),
                       ('connstring', nfc_connstring),
                       ('bCrc', c_bool),
                       ('bPar', c_bool),
                       ('bEasyFraming', c_bool),
                       ('bInfiniteSelect', c_bool),
                       ('bAutoIso14443_4', c_bool),
                       ('btSupportByte', c_uint8),
                       ('last_error', c_int)]

class nfc_modulation(Structure):
    _fields_ = [('nmt', c_int), ('nbr', c_int)]

class nfc_iso14443a_info(Structure):
    _fields_ = [('abtAtqa', c_uint8 * 2),
                ('btSak', c_uint8),
                ('szUidLen', c_size_t),
                ('abtUid', c_uint8 * 10),
                ('szAtsLen', c_size_t),
                ('abtAts', c_uint8 * 254)]
    
class nfc_felica_info(Structure):
    _fields_ = [('szLen', c_size_t),
                ('btResCode', c_uint8),
                ('abtId', c_uint8 * 8),
                ('abtPad', c_uint8 * 8),
                ('abtSysCode', c_uint8 * 2)]

class nfc_iso14443b_info(Structure):
    _fields_ = [('abtPupi', c_uint8 * 4),
                ('abtApplicationData', c_uint8 * 4),
                ('abtProtocolInfo', c_uint8 * 3),
                ('ui8CardIdentifier', c_uint8)]

class nfc_iso14443bi_info(Structure):
    _fields_ = [('abtDIV', c_uint8 * 4),
                ('btVerLog', c_uint8),
                ('btConfig', c_uint8),
                ('szAtrLen', c_size_t),
                ('abtAtr', c_uint8 * 33)]

class nfc_iso14443b2sr_info(Structure):
    _fields_ = [('abtUID', c_uint8 * 8)]

class nfc_iso14443b2ct_info(Structure):
    _fields_ = [('abtUID', c_uint8 * 4),
                ('btProdCode', c_uint8),
                ('btFabCode', c_uint8)]

class nfc_jewel_info(Structure):
    _fields_ = [('btSensRes', c_uint8 * 2),
                ('btId', c_uint8 * 4)]

class nfc_dep_info(Structure):
    _fields_ = [('abtNFCID3', c_uint8 * 10),
                ('btDID', c_uint8),
                ('btBS', c_uint8),
                ('btBR', c_uint8),
                ('btTO', c_uint8),
                ('btPP', c_uint8),
                ('abtGB', c_uint8 * 48),
                ('szGB', c_size_t),
                ('ndm', c_int)]
    
class nfc_target_info(Union):
    _fields_ = [('nai', nfc_iso14443a_info),
                ('nfi', nfc_felica_info),
                ('nbi', nfc_iso14443b_info),
                ('nii', nfc_iso14443bi_info),
                ('nsi', nfc_iso14443b2sr_info),
                ('nci', nfc_iso14443b2ct_info),
                ('nji', nfc_jewel_info),
                ('ndi', nfc_dep_info)]

    
class nfc_target(Structure):
    _fields_ = [('nti', nfc_target_info), ('nm', nfc_modulation)]


nfc_init = _libnfc.nfc_init
nfc_init.restype = None
nfc_init.argtypes = [POINTER(POINTER(nfc_context))]

nfc_exit = _libnfc.nfc_exit
nfc_exit.restype = None
nfc_exit.argtype = [POINTER(nfc_context)]


nfc_open = _libnfc.nfc_open
nfc_open.restype = POINTER(nfc_device)
nfc_open.argtype = [POINTER(nfc_context), nfc_connstring]

nfc_close  = _libnfc.nfc_close
nfc_close.restype = None
nfc_close.argtype = [POINTER(nfc_device)]

nfc_abort_command = _libnfc.nfc_abort_command
nfc_abort_command.restype = c_int
nfc_abort_command.argtype = [POINTER(nfc_device)]


nfc_initiator_init = _libnfc.nfc_initiator_init
nfc_initiator_init.restype = c_int
nfc_initiator_init.argtype = [POINTER(nfc_device)]

nfc_initiator_poll_target = _libnfc.nfc_initiator_poll_target
nfc_initiator_poll_target.restype = c_int
nfc_initiator_poll_target.argtype = [POINTER(nfc_device),
                                     POINTER(nfc_modulation),
                                     c_size_t,
                                     c_uint8,
                                     c_uint8,
                                     POINTER(nfc_target)]

nfc_initiator_target_is_present = _libnfc.nfc_initiator_target_is_present
nfc_initiator_target_is_present.restype = c_int
nfc_initiator_target_is_present.argtype = [POINTER(nfc_device),
                                            POINTER(nfc_target)]


nfc_perror_ = _libnfc.nfc_perror
nfc_perror_.restype = None
nfc_perror_.argtype = [POINTER(nfc_device), c_char_p]


nfc_device_get_name_  = _libnfc.nfc_device_get_name
nfc_device_get_name_.restype = c_char_p
nfc_device_get_name_.argtype = [POINTER(nfc_device)]


nfc_version_ = _libnfc.nfc_version
nfc_version_.restype = c_char_p
nfc_version_.argtypes = []

nfc_free = _libnfc.nfc_free
nfc_free.restype = None
nfc_free.argtypes = [c_void_p]


str_nfc_target = _libnfc.str_nfc_target
str_nfc_target.restype = c_int
str_nfc_target.argtypes = [POINTER(c_char_p), POINTER(nfc_target), c_bool]



