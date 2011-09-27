import socket
import sys

MASK_ERRORS = True

if socket.gethostname() == 'matt-griffiths':
    MASK_ERRORS = False
