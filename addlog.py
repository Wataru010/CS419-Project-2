import sys, os
from datetime import datetime
import base64
import hashlib

args = sys.argv

if len(args) < 2:
    print("Supply an argument for log string!")
    sys.exit()
elif len(args) > 2:
    print("Too many arguments!")
    sys.exit()

log_string = args[1]

try:
    log = open("log.txt")
    log.close()

    try: # both log.txt and loghead.txt exist
        if os.path.getsize("loghead.txt") == 0:
            print("loghead.txt is empty!")
            sys.exit()
        else:
            loghead = open("loghead.txt", "r")
            hash_head_pointer = loghead.readline()
            hash_head_pointer = hash_head_pointer.strip()
            date_time = str(datetime.now())
            new_log = "".join(list(date_time)[:19]) + " - " + hash_head_pointer + " " + log_string.replace("\n", " ")
            loghead.close()
            
            loghead = open("loghead.txt", "w")
            hash_str = hashlib.sha256(new_log.encode("ascii")).hexdigest()
            base64_str = base64.b64encode(hash_str.encode("ascii")).decode("ascii")
            loghead.write(base64_str)
            loghead.close()

            log = open("log.txt", "a")
            log.write(new_log + "\n")
            log.close()

    except FileExistsError: # only log.txt exist
        print("loghead.txt is missing!")
        sys.exit()

except FileNotFoundError:
    # try: # only loghead.txt exist

    date_time = str(datetime.now())
    new_log = "".join(list(date_time)[:19]) + " - " + "begin" + " " + log_string.replace('\n', ' ')

    loghead = open("loghead.txt", "w")
    hash_str = hashlib.sha256(new_log.encode("ascii")).hexdigest()
    base64_str = base64.b64encode(hash_str.encode("ascii")).decode("ascii")
    loghead.write(base64_str)
    loghead.close()

    log = open("log.txt", "a")
    log.write(new_log + "\n")
    log.close()

    # except FileExistsError: # neither log.txt and loghead.txt exist
    #     print()