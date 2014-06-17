import redis
import base64
import md5
import math
import os

BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48

PREFIX = os.getenv("PREFIX", "shortend:") 

class SimpleUrlShortener:

    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get_ord(self, char):

        ''' Takes a char and turns it into an integer with base 62 '''

        if char.isdigit():
            return ord(char) - DIGIT_OFFSET
        elif 'a' <= char <= 'z':
            return ord(char) - LOWERCASE_OFFSET
        elif 'A' <= char <= 'Z':
            return ord(char) - UPPERCASE_OFFSET
        else:   
            raise ValueError('%s is not a valid character' % char)


    def get_char(self, integer):

        ''' Takes an integer with base 62 and turns it into a character '''

        if integer < 10:
            return chr(integer + DIGIT_OFFSET)
        elif 10 <= integer <= 35:
            return chr(integer + UPPERCASE_OFFSET)
        elif 36 <= integer < 62:
            return chr(integer + LOWERCASE_OFFSET)
        else:
            raise ValueError("%d is not a valid integer in the range of base %d" % (integer, BASE))

    def to_integer(self, string):

        _sum = 0
        reversed_str = string[::-1]
        for index, char in enumerate(reversed_str):
            _sum += self.get_ord(char) * int(math.pow(BASE, index))

        return _sum

    def from_integer(self, integer):

        if integer == 0:
            return '0'

        _str = ""

        while integer > 0:
            remainder = integer % BASE
            _str += self.get_char(remainder)
            integer /= BASE

        return _str

    def shorten(self, url):

        shortened = base64.b64encode(md5.new(url).digest()[-5:])
        sanitized = shortened.replace('=','').replace('/','_')

        # set santized code + Redis in redis as key, and the url as the value

        try:
            print "santiized " + sanitized
            self.redis.set(PREFIX + sanitized, url)
            return {   
                        'success': True,
                        'url': url,
                        'code': sanitized,
                        'shorturl': 'http://localhost:5000/' + sanitized
                    }
        except:
            return { 'success': False }

    def lookup(self, code):

        try:
            print "trying"
            self.redis.get(PREFIX + code)

        except:
            return None
