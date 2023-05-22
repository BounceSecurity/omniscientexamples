
class CallService:
    
    def SendTransactionOld(self, account, value, msg):
        print("Sent to '" + account + "'")
        
    def SendTransaction(self, account, value, msg, checksum = None):
        
        if (checksum == None):
            self.SendTransactionOld(account, value, msg)
        else:
            print("Sent to '" + account + "', but safely!")
        

def main():
    
    clientCall = CallService()
    clientCall.Name = "HacmeBank"
    
    accountNum = "12146123"
    msg = "Invoice 24234"
    someChecksum = "D97EA6CA"
    
    # ruleid: wrong_overload
    clientCall.SendTransaction(accountNum, 4489, "Invoice 78896")

    # ruleid: wrong_overload
    clientCall.SendTransaction("12146123", 4489, msg)
    
    # ruleid: wrong_overload
    clientCall.SendTransaction(accountNum, 4342, msg)

    # ruleid: ok
    clientCall.SendTransaction(accountNum, 4489, "Invoice 78896", someChecksum)

    # ruleid: ok
    clientCall.SendTransaction("12146123", 4489, msg, "ABCD4123")

    # ruleid: ok
    clientCall.SendTransaction(accountNum, 4342, msg, "DEFA3456")


main()
