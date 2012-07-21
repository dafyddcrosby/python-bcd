#!/bin/python/
# Copyright 2012 Dafydd Crosby <dafydd@dafyddcrosby.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

"""
Methods to translate to and from binary coded decimal
"""


def bcd_to_int(x):
    """
    This translates binary coded decimal into an integer
    TODO - more efficient algorithm

    >>> bcd_to_int(4)
    4

    >>> bcd_to_int(159)
    345
    """

    if x < 0:
        raise ValueError("Cannot be a negative integer")

    binstring = ''
    while True:
        q, r = divmod(x, 10)
        nibble = bin(r).replace('0b', "")
        while len(nibble) < 4:
            nibble = '0' + nibble
        binstring = nibble + binstring
        if q == 0:
            break
        else:
            x = q

    return int(binstring, 2)


def int_to_bcd(x):
    """
    This translates an integer into
    binary coded decimal

    >>> int_to_bcd(4)
    4

    >>> int_to_bcd(34)
    22
    """

    if x < 0:
        raise ValueError("Cannot be a negative integer")

    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4
    return int(bcdstring)
