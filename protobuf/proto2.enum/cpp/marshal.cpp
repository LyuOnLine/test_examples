#include <stdio.h>
#include <string>
#include "test.pb.h"
using namespace test;
using namespace std;

int main(int argc, char *argv[])
{
	TestMessage msg;
	string buf;
	msg.set_testenum(TestEnum(100));
	msg.set_testint(20);
	msg.SerializeToString(&buf);

	FILE *fl = fopen("/tmp/proto.dat", "wb+");
	if (fl == NULL)
	{
		printf("open proto.dat failed!\n");
		return -1;
	}
	fwrite(buf.c_str(), 1, buf.length(), fl);
	fclose(fl);

	TestMessage msg2;
	buf[1] = 100;
	msg2.ParseFromString(buf);
	printf("message: enum=%d, int=%d\n", msg2.testenum(), msg2.testint());
	return 0;
}