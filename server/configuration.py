import socket
import sys

MASK_ERRORS = True
AFINN_FILE = '/usr/local/metaLayer-sentiment/resources/AFINN.txt'

ERROR_NOTEXT = {'status':'failed', 'code':101, 'error':'The required POST field \'text\' was not supplied' }

if socket.gethostname() == 'matt-griffiths':
    MASK_ERRORS = False
    AFINN_FILE = '/home/matt/code/metaLayer/sentiment/resources/AFINN.txt'
