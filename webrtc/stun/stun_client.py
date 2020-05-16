#!/usr/bin/env python
import asyncio
import aioice
import socket
from dataclasses import dataclass
from aioice import stun
from typing import Dict, List, Optional, Set, Text, Tuple, Union, cast


class StunProtocol(asyncio.DatagramProtocol):
    """StunProtocol: protocol class of Stun protocol.
    
    functions needed by stun.Transaction:
    send_stun() : send stun message to stun server.

    override functions:
        connection_made()  :  callback of connection made.
        connection_lost()  :  callback of connection lost.
        datagram_received() :  callback of datagram received.
        error_received()    :  callback of error received.
    """

    def __init__(self):
        self.transport: Optional[asyncio.DatagramTransport] = None
        self.transactions: Dict[bytes, stun.Transaction] = {}

    def connection_made(self, transport) -> None:
        self.transport = transport

    def connection_lost(self, exc: Exception) -> None:
        print("[Error] connection losted due to(%s)" % (exc))

    def datagram_received(self, data: Union[bytes, Text], addr: Tuple) -> None:
        addr = (addr[0], addr[1])
        data = cast(bytes, data)

        try:
            msg = stun.parse_message(data)
            print("[Info] Recv pkt from %s: %s" %
                  (repr(addr), "".join("0x%02x," % c for c in data)[:-1]))
        except:
            print("[Error] packet parse error! pkt = " +
                  "".join("0x%02x," % c for c in data))
            return
        if msg.message_class == stun.Class.RESPONSE or msg.message_class == stun.Class.ERROR:
            if msg.transaction_id in self.transactions:
                trans = self.transactions[msg.transaction_id]
                trans.response_received(msg, addr)
            else:
                print("[Info] not expected message: %s" % (repr(msg)))

    def error_received(self, exc: Exception) -> None:
        print("[Error] excepton received %s" % (repr(exc)))

    def send_stun(self, msg: stun.Message, addr: Tuple[str, int]) -> None:
        print("[Info] Send pkt to %s: %s" %
              (repr(addr), "".join("0x%02x," % c for c in bytes(msg))[:-1]))
        #self.transactions[msg.transaction_id] =
        self.transport.sendto(bytes(msg), addr)

    async def request(self, cmd: stun.Message, addr: Tuple[str, int], retransmissions=None) -> Tuple[stun.Message, Tuple[str, int]]:
        trans = stun.Transaction(cmd, addr, self, retransmissions)
        self.transactions[cmd.transaction_id] = trans
        try:
            return await trans.run()
        except Exception as e:
            print("[ERROR] Exception: " + str(e))
            return None, None
        finally:
            del self.transactions[cmd.transaction_id]


def getLocalIP():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


async def stunTest(protocol: StunProtocol, server_ip: Tuple[str, int], change_ip: bool, change_port: bool) -> Tuple[bool, Tuple[str, int]]:
    cmd = stun.Message(message_method=stun.Method.BINDING,
                       message_class=stun.Class.REQUEST)
    if change_ip:
        cmd.attributes["CHANGE-REQUEST"] = 0x4
    if change_port:
        cmd.attributes["CHANGE-REQUEST"] = 0x2
    try:
        ack, _ = await protocol.request(cmd, server_ip, retransmissions=3)
        if ack:
            return True, ack.attributes["XOR-MAPPED-ADDRESS"]
    except Exception as e:
        print("[ERROR] %s" % str(e))
    return False, None

if __name__ == "__main__":
    # List of Google-provided STUN servers.
    GOOGLE_SERVER_LIST = [
        ('stun.l.google.com', 19302),
        ('stun1.l.google.com', 19302),
        ('stun2.l.google.com', 19302),
        ('stun3.l.google.com', 19302),
        ('stun4.l.google.com', 19302),
    ]
    # # Some non-Google-provided STUN servers, not used by default.
    # # copied from:
    # # http://code.google.com/p/natvpn/source/browse/trunk/stun_server_list
    EXTRA_SERVER_LIST = [
        #('stun01.sipphone.com', 3478),
        ('stun.ekiga.net', 3478),
        #('stun.fwdnet.net', 3478),
        ('stun.ideasip.com', 3478),
        #('stun.iptel.org', 3478),
        ('stun.rixtelecom.se', 3478),
        ('stun.schlund.de', 3478),
        ('stunserver.org', 3478),
        ('stun.softjoys.com', 3478),
        ('stun.voiparound.com', 3478),
        ('stun.voipbuster.com', 3478),
        ('stun.voipstunt.com', 3478),
        ('stun.voxgratia.org', 3478),
        ('stun.xten.com', 3478),
    ]

    WAIT_TIMEOUT = 3

    @dataclass
    class StunTest:
        name: str
        server: Tuple[str, int]
        change_ip: bool
        change_port: bool
        result: bool = False
        map_addr: Tuple[str, int] = None

    tests = [
        StunTest("test1: binding normal IP",
                 GOOGLE_SERVER_LIST[1], False, False),
        StunTest("test2: change IP", GOOGLE_SERVER_LIST[1], True, False),
        StunTest("test3: change port", GOOGLE_SERVER_LIST[1], False, True),
        StunTest("test4: binding another IP",
                 GOOGLE_SERVER_LIST[2], False, False),
    ]

    async def main():
        loop = asyncio.get_event_loop()
        _, protocol = await loop.create_datagram_endpoint(StunProtocol, local_addr=(getLocalIP(), 0))
        for t in tests:
            ip = socket.gethostbyname(t.server[0])
            t.result, t.map_addr = await asyncio.wait_for(stunTest(protocol, (ip, t.server[1]), t.change_ip, t.change_port), WAIT_TIMEOUT)
            print("%s %s" % ("[OK]" if t.result else "[FAIL]", t.name))

    asyncio.run(main())

    print("\n[RESULT]")
    if not tests[0].result or not tests[3].result:
        print("TEST failed, stun server is down?")
    if tests[0].map_addr == tests[3].map_addr:
        print("Independent mapping")
    else:
        print("IP dependent mapping")

    if tests[1].result:
        print("Independent Filter")
    elif tests[2].result:
        print("address dependent filtering")
    else:
        print("address and port dependent filtering")
