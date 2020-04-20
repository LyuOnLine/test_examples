package main

import (
	"fmt"
	"io/ioutil"
	pb "test"
	"github.com/golang/protobuf/proto"
)

func main() {
	var testEnum pb.TestEnum = 1
	var testInt int32 = 100
	msg := pb.TestMessage{TestEnum: &testEnum, TestInt: &testInt}
	buf, err := proto.Marshal(&msg)
	if err != nil {
		fmt.Printf("[ERROR] marshal failed! %v\n", err)
	}

	err = ioutil.WriteFile("/tmp/proto.dat", buf, 0644)
	if err != nil {
		fmt.Println("[ERROR] write to proto.dat failed!")
	}

	msg2 := &pb.TestMessage{}
	err = proto.Unmarshal(buf, msg2)
	if err != nil {
		fmt.Printf("[ERROR] unmarshal failed! %v\n", err)
	}
  fmt.Printf("message = %v\n", msg2)
}
