#!/usr/bin/python3
# Shawn Pang

import re

# The two regex strings
regex1 = r'GET /forum_S2hpxwQ/\w{12}/\w{4,12}\.(html|swf|mp3)'
regex2 = r'GET /forum_S2hpxwQ/showthread\.php\?id=\d+'

# A few samples
patterns = [
    'GET /forum_S2hpxwQ/showthread.php?id=7991937328',
    'GET /forum_S2hpxwQ/70jT7XJ0lysv/Uhg2F49WHwXu.html',
    'GET /forum_S2hpxwQ/I3Pg9p7IEM5v/Uhg2F49WHwXu.html',
    'GET /forum_S2hpxwQ/70jT7XJ0lysv/test.mp3',
    'GET /forum_S2hpxwQ/70jT7XJ0lysv/ICIMPh7jWGyz.swf',
]

def check(regex, patterns):
    print('\nTesting Regex: {}'.format(regex))
    for pattern in patterns:
        print('   MATCH -' if re.match(regex, pattern) else 'NO MATCH -', pattern)

check(regex1, patterns)
check(regex2, patterns)
