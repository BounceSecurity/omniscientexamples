
# OLD VERSION OF CLASS STARTS ---------------------------------

class CallService:
    def send_transaction(self, cat, value, msg):
        # Do transaction sending stuff
        print("Sent to '" + cat + "'")

# OLD VERSION OF CLASS ENDS ---------------------------------

# NEW VERSION OF CLASS STARTS ---------------------------------

class CallService:
    def send_transaction_old(self, cat, value, msg):
        # Do transaction sending stuff
        print("Sent to '" + cat + "'")

    def send_transaction(self, cat, value, msg, checksum=None):
        if checksum == None:
            self.send_transaction_old(cat, value, msg)
        else:
            # Do transaction sending stuff but this time
            # with a checksum
            print("Sent to '" + cat + "', but safely!")

# NEW VERSION OF CLASS ENDS ---------------------------------

def main():

    CatRequest = CallService()
    CatRequest.name = "HacmeBank"

    cat_num = "12146123"
    msg = "Invoice 24234"
    some_checksum = "D97EA6CA"

    # ruleid: wrong_overload
    CatRequest.send_transaction(cat_num, 4489, msg)

    # ruleid: ok
    CatRequest.send_transaction(cat_num, 4489, msg, some_checksum)

    # ruleid: wrong_overload
    CatRequest.send_transaction("12146123", 4489, msg)

    # ruleid: wrong_overload
    CatRequest.send_transaction(accountNum, 4342, msg)

    # ruleid: ok
    CatRequest.send_transaction(accountNum, 4489, "Invoice 78896", someChecksum)

    # ruleid: ok
    CatRequest.send_transaction("12146123", 4489, msg, "ABCD4123")

    # ruleid: ok
    CatRequest.send_transaction(accountNum, 4342, msg, "DEFA3456")


main()
