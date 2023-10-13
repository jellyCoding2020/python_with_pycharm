from socket import socket, AF_BLUETOOTH, BTPROTO_RFCOMM, SOCK_STREAM
from socketserver import ThreadingMixIn

socket = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)





