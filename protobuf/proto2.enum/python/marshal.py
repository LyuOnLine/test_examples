import test_pb2

if __name__ == "__main__":
    msg = test_pb2.TestMessage()
    msg.testEnum = 1
    msg.testInt = 100
    buf = msg.SerializeToString()
    
    with open("/tmp/proto.dat", "wb+") as fl:
        fl.write(buf)

    msg2 = test_pb2.TestMessage()
    msg2.ParseFromString(buf)
    print(msg2)
