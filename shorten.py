import redis
import base64
import md5
# import config
import sys

BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48

class SimpleUrlShortener:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=5000, db=0)

    def get_ord(self, char):

        ''' Takes a char and turns it into an integer with base 62 '''

        if char.isDigit():
            return ord(char) - DIGIT_OFFSET
        elif 'a' <= char <= 'z':
            return ord(char) - LOWERCASE_OFFSET
        elif 'A' <= char <= 'Z':
            return ord(char) - UPPERCASE_OFFSET
        else:   
            raise ValueError('%s is not a valid character' % char)

