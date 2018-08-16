import datetime
import subprocess

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
DELIMITER = '-'
TIMEOUT = 600
SIGN_EXEC = 'cpp/signmessage'
VERIFY_EXEC = 'cpp/verifymessage'


# Returns a hexdump string of the message and its signature
def generateID(privateKeyFile):
    timestamp = datetime.datetime.utcnow()
    message = timestamp.strftime(TIMESTAMP_FORMAT)
    callArgs = (SIGN_EXEC, message, privateKeyFile)
    proc = subprocess.Popen(callArgs, stdout=subprocess.PIPE)
    results = proc.communicate()
    signature = results[0][:-1].decode('utf-8')
    idString = message.encode('utf-8').hex() + DELIMITER + signature
    return idString


# Returns True for valid and False for invalid
def validateIDFromHex(message, publicKeyFile):
    # Read in the given message and split up the message
    messageList = message.split(DELIMITER)
    timestamp = bytes.fromhex(messageList[0]).decode('utf-8')
    signature = messageList[1]
    # Verify the message is not stale
    messageTime = datetime.datetime.strptime(timestamp, TIMESTAMP_FORMAT)
    currentTime = datetime.datetime.utcnow()
    difference = (currentTime - messageTime).seconds
    if difference > TIMEOUT:
        return False
    # Verify the RSA signature
    callArgs = (VERIFY_EXEC, timestamp, signature, publicKeyFile)
    proc = subprocess.Popen(callArgs, stdout=subprocess.PIPE)
    results = proc.communicate()
    retVal = (results[0][:-1].decode('utf-8') == '1')
    return retVal
