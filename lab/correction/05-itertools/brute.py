import hashlib
import itertools
import string
import sys

from zipfile import ZipFile

# Write a module that cracks Rao's zip archive. You know that the password is
# between 6 and 8ascii lowercase characters long and that it's md5sum is the
# following:
zip_hash = '79d67a2cba9c0aae75c36c79bcaeb736'

# Don't forget to do the extracting in Python, Rao has logs of all unzip
# commands run by the Citizens of Rao!

zf = ZipFile('secret.zip')
for length in xrange(6, 8):
    for combo in itertools.product(string.ascii_lowercase, repeat=length):
        password = ''.join(combo)
        pass_hash = hashlib.md5(password).hexdigest()

        if pass_hash == zip_hash:
            try:
                zf.extractall(pwd=password)
                print password
                sys.exit(0)
            except RuntimeError:
                continue