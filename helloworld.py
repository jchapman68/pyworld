import os

#os.environ["GREETING"] = "Hello Rob"
#myvar = os.environ["GREETING"]
#if myvar == "Hello Rob":
#    print ("success")
#else:
#    print("fail")

#print os.environ["GREETING"]
#print("Goodbye, World!")

def test_greeting(message):
    if message == "foobar":
        return message
    else:
        return "Hello {}".format(message)

