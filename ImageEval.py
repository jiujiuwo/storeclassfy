[2018-05-08 22:06:02.160][3676][5][lsp]Basic info,uin=166353299
[2018-05-08 22:06:02.160][3676][5][lsp]will accelerate game process:League of Legends.exe, log level:4
[2018-05-08 22:06:02.160][3676][5][lsp]game_id=26, zone_id=1026, net_mode=0x01030018, acc_mode=1, manual_mode=false, accelerate£º TCP UDP
[2018-05-08 22:06:02.160][3676][5][lsp][Route][LoadRoute] open route table from shared memory success!
[2018-05-08 22:06:02.161][3676][5][lsp][Route][LoadBlacklistTableFromMem] blacklist entries count(9)!
[2018-05-08 22:06:02.161][3676][5][lsp][LoadRailIplistTableFromMem] rail iptable entries count(778)!
[2018-05-08 22:06:02.168][3676][5][lsp][Route][LoadIpTableFromMem] success ip count(20440), level=0!
[2018-05-08 22:06:02.168][3676][5][lsp][Route][Load] try to read route success, wait_route=success, try time=1, try interval_ms=100 ms, game vip level=0
[2018-05-08 22:06:02.171][3676][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=17, socket=716, token=1
[2018-05-08 22:06:02.171][7392][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=17, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=17, socket=916, token=2
[2018-05-08 22:06:02.172][7392][4][lsp]WSPBind: ret=0, err=0, port=7944, socket=916, token=2
[2018-05-08 22:06:02.172][7392][5][lsp][UDP] AdjustSocketBuff, previous send_buf=65536, new send_buf=65536, socket=916
[2018-05-08 22:06:02.172][7392][5][lsp][UDP] AdjustSocketBuff, previous recv_buf=65536, new recv_buf=65536, socket=916
[2018-05-08 22:06:02.172][7392][5][lsp][UDP] UdpProvider::OnCreateLocalServer success, port=7944
[2018-05-08 22:06:02.172][7392][4][lsp]RelayMgr::InternalInit, UDP init is true
[2018-05-08 22:06:02.172][7392][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=920, token=3
[2018-05-08 22:06:02.172][7392][4][lsp]WSPBind: ret=0, err=0, port=30108, socket=920, token=3
[2018-05-08 22:06:02.172][7392][5][lsp][UDP] AdjustSocketBuff, previous send_buf=65536, new send_buf=65536, socket=920
[2018-05-08 22:06:02.172][7392][5][lsp][UDP] AdjustSocketBuff, previous recv_buf=65536, new recv_buf=65536, socket=920
[2018-05-08 22:06:02.173][7392][4][lsp][TCP] OnCreateLocalServer listen return=0, err=0
[2018-05-08 22:06:02.173][7392][4][lsp]RelayMgr::InternalInit, TCP init is true
[2018-05-08 22:06:02.181][3676][4][lsp]RelayMgr::CheckAndInit, initialization is 0
[2018-05-08 22:06:02.181][3676][4][lsp][Route][NeedRelay] IP(125.39.245.221:8081) is not in ip table, socket=716, token=1
[2018-05-08 22:06:02.181][3676][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=125.39.245.221:8081, relay=false, socket=716, token=1
[2018-05-08 22:06:02.221][3400][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1052, token=4
[2018-05-08 22:06:02.221][3400][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1052, token=4
[2018-05-08 22:06:02.221][3400][4][lsp]WSPConnect:protocol=6, type=1, socket=1052, token=4
[2018-05-08 22:06:02.221][3400][4][lsp][Route][NeedRelay] IP(125.39.6.155:80) is not in ip table, socket=1052, token=4
[2018-05-08 22:06:02.221][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1060, token=5
[2018-05-08 22:06:02.221][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1060, token=5
[2018-05-08 22:06:02.221][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1060, token=5
[2018-05-08 22:06:02.221][3676][4][lsp][Route][NeedRelay] IP(125.39.6.155:80) is not in ip table, socket=1060, token=5
[2018-05-08 22:06:02.221][3400][5][lsp]WSPConnect: ret=-1, err=10035, dest=125.39.6.155:80, local port=0, udp_connect_mode=false, socket=1052, token=4
[2018-05-08 22:06:02.221][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=125.39.6.155:80, local port=0, udp_connect_mode=false, socket=1060, token=5
[2018-05-08 22:06:02.250][3400][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1052, token=4
[2018-05-08 22:06:02.250][3400][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1052, token=6
[2018-05-08 22:06:02.251][3400][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1052, token=6
[2018-05-08 22:06:02.251][3400][4][lsp]WSPConnect:protocol=6, type=1, socket=1052, token=6
[2018-05-08 22:06:02.251][3400][4][lsp][Route][NeedRelay] IP(14.204.74.147:80) is not in ip table, socket=1052, token=6
[2018-05-08 22:06:02.251][3400][5][lsp]WSPConnect: ret=-1, err=10035, dest=14.204.74.147:80, local port=0, udp_connect_mode=false, socket=1052, token=6
[2018-05-08 22:06:02.280][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1060, token=5
[2018-05-08 22:06:02.281][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1060, token=7
[2018-05-08 22:06:02.281][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1060, token=7
[2018-05-08 22:06:02.281][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1060, token=7
[2018-05-08 22:06:02.281][3676][4][lsp][Route][NeedRelay] IP(42.236.95.108:80) is not in ip table, socket=1060, token=7
[2018-05-08 22:06:02.281][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=42.236.95.108:80, local port=0, udp_connect_mode=false, socket=1060, token=7
[2018-05-08 22:06:02.331][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1060, token=7
[2018-05-08 22:06:02.368][3400][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1052, token=6
[2018-05-08 22:06:03.009][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1120, token=8
[2018-05-08 22:06:03.009][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1120, token=8
[2018-05-08 22:06:03.009][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1120, token=8
[2018-05-08 22:06:03.009][3676][4][lsp][Route][NeedRelay] IP(125.39.6.155:80) is not in ip table, socket=1120, token=8
[2018-05-08 22:06:03.009][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=125.39.6.155:80, local port=0, udp_connect_mode=false, socket=1120, token=8
[2018-05-08 22:06:03.036][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1120, token=8
[2018-05-08 22:06:03.036][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1120, token=9
[2018-05-08 22:06:03.036][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1120, token=9
[2018-05-08 22:06:03.036][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1120, token=9
[2018-05-08 22:06:03.036][3676][4][lsp][Route][NeedRelay] IP(157.255.128.35:80) is not in ip table, socket=1120, token=9
[2018-05-08 22:06:03.037][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=157.255.128.35:80, local port=0, udp_connect_mode=false, socket=1120, token=9
[2018-05-08 22:06:03.139][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1120, token=9
[2018-05-08 22:06:03.909][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1128, token=10
[2018-05-08 22:06:03.909][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1128, token=10
[2018-05-08 22:06:03.909][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1128, token=10
[2018-05-08 22:06:03.909][3676][4][lsp][Route][NeedRelay] IP(125.39.6.155:80) is not in ip table, socket=1128, token=10
[2018-05-08 22:06:03.909][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=125.39.6.155:80, local port=0, udp_connect_mode=false, socket=1128, token=10
[2018-05-08 22:06:03.943][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1128, token=10
[2018-05-08 22:06:03.944][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=1128, token=11
[2018-05-08 22:06:03.944][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1128, token=11
[2018-05-08 22:06:03.944][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=1128, token=11
[2018-05-08 22:06:03.944][3676][4][lsp][Route][NeedRelay] IP(113.200.90.158:80) is not in ip table, socket=1128, token=11
[2018-05-08 22:06:03.944][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=113.200.90.158:80, local port=0, udp_connect_mode=false, socket=1128, token=11
[2018-05-08 22:06:04.012][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1128, token=11
[2018-05-08 22:06:04.599][6880][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1460, token=12
[2018-05-08 22:06:04.600][6880][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1460, token=12
[2018-05-08 22:06:04.603][6880][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1460, token=13
[2018-05-08 22:06:04.603][6880][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1460, token=13
[2018-05-08 22:06:04.603][6880][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1460, token=13
[2018-05-08 22:06:04.603][6880][4][lsp][Route][NeedRelay] IP(125.39.6.15:80) is not in ip table, socket=1460, token=13
[2018-05-08 22:06:04.603][6880][5][lsp]WSPConnectEx: ret=0, err=997, dest=125.39.6.15:80, port=0, socket=1460, token=13
[2018-05-08 22:06:04.615][7920][4][lsp]WSPGetPeerName: ret=0, err=0, peer=125.39.6.15:80, socket=1460, token=13
[2018-05-08 22:06:04.655][6880][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1556, token=14
[2018-05-08 22:06:04.655][6880][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1556, token=14
[2018-05-08 22:06:04.656][6880][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1556, token=15
[2018-05-08 22:06:04.656][6880][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1556, token=15
[2018-05-08 22:06:04.656][6880][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1556, token=15
[2018-05-08 22:06:04.656][6880][4][lsp][Route][NeedRelay] IP(140.207.234.45:80) is not in ip table, socket=1556, token=15
[2018-05-08 22:06:04.656][6880][5][lsp]WSPConnectEx: ret=0, err=997, dest=140.207.234.45:80, port=0, socket=1556, token=15
[2018-05-08 22:06:04.689][6880][4][lsp]WSPGetPeerName: ret=0, err=0, peer=140.207.234.45:80, socket=1556, token=15
[2018-05-08 22:06:04.741][6880][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1580, token=16
[2018-05-08 22:06:04.741][6880][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1580, token=16
[2018-05-08 22:06:04.741][6880][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1580, token=17
[2018-05-08 22:06:04.741][6880][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1580, token=17
[2018-05-08 22:06:04.741][6880][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1580, token=17
[2018-05-08 22:06:04.741][6880][4][lsp][Route][NeedRelay] IP(125.211.204.19:80) is not in ip table, socket=1580, token=17
[2018-05-08 22:06:04.741][6880][5][lsp]WSPConnectEx: ret=0, err=997, dest=125.211.204.19:80, port=0, socket=1580, token=17
[2018-05-08 22:06:04.773][6880][4][lsp]WSPGetPeerName: ret=0, err=0, peer=125.211.204.19:80, socket=1580, token=17
[2018-05-08 22:06:05.123][6880][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1720, token=18
[2018-05-08 22:06:05.123][6880][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1720, token=18
[2018-05-08 22:06:05.123][6880][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1720, token=19
[2018-05-08 22:06:05.123][6880][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1720, token=19
[2018-05-08 22:06:05.123][6880][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1720, token=19
[2018-05-08 22:06:05.123][6880][4][lsp][Route][NeedRelay] IP(112.80.27.22:80) is not in ip table, socket=1720, token=19
[2018-05-08 22:06:05.123][6880][5][lsp]WSPConnectEx: ret=0, err=997, dest=112.80.27.22:80, port=0, socket=1720, token=19
[2018-05-08 22:06:05.202][10696][4][lsp]WSPGetPeerName: ret=0, err=0, peer=112.80.27.22:80, socket=1720, token=19
[2018-05-08 22:06:05.243][9256][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1840, token=20
[2018-05-08 22:06:05.243][9256][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1840, token=20
[2018-05-08 22:06:05.250][10696][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1864, token=21
[2018-05-08 22:06:05.250][10696][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1864, token=21
[2018-05-08 22:06:05.250][10696][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1864, token=21
[2018-05-08 22:06:05.250][10696][4][lsp][Route][NeedRelay] IP(125.39.6.15:80) is not in ip table, socket=1864, token=21
[2018-05-08 22:06:05.250][10696][5][lsp]WSPConnectEx: ret=0, err=997, dest=125.39.6.15:80, port=0, socket=1864, token=21
[2018-05-08 22:06:05.263][7920][4][lsp]WSPGetPeerName: ret=0, err=0, peer=125.39.6.15:80, socket=1864, token=21
[2018-05-08 22:06:05.263][10696][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=1848, token=22
[2018-05-08 22:06:05.263][10696][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=1848, token=22
[2018-05-08 22:06:05.264][10696][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1848, token=23
[2018-05-08 22:06:05.264][10696][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1848, token=23
[2018-05-08 22:06:05.264][10696][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1848, token=23
[2018-05-08 22:06:05.264][10696][4][lsp][Route][NeedRelay] IP(27.221.54.193:80) is not in ip table, socket=1848, token=23
[2018-05-08 22:06:05.264][10696][5][lsp]WSPConnectEx: ret=0, err=997, dest=27.221.54.193:80, port=0, socket=1848, token=23
[2018-05-08 22:06:05.278][9256][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=1856, token=24
[2018-05-08 22:06:05.278][9256][4][lsp]WSPBind: ret=0, err=0, port=0, socket=1856, token=24
[2018-05-08 22:06:05.278][9256][4][lsp]WSPConnectEx: protocol=6, type=1, socket=1856, token=24
[2018-05-08 22:06:05.278][9256][4][lsp][Route][NeedRelay] IP(220.194.223.34:80) is not in ip table, socket=1856, token=24
[2018-05-08 22:06:05.278][9256][5][lsp]WSPConnectEx: ret=0, err=997, dest=220.194.223.34:80, port=0, socket=1856, token=24
[2018-05-08 22:06:05.283][3760][4][lsp]WSPGetPeerName: ret=0, err=0, peer=27.221.54.193:80, socket=1848, token=23
[2018-05-08 22:06:05.294][10696][4][lsp]WSPGetPeerName: ret=0, err=0, peer=220.194.223.34:80, socket=1856, token=24
[2018-05-08 22:06:05.498][7504][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=2112, token=25
[2018-05-08 22:06:05.498][7504][4][lsp][Route][NeedRelay] IP(111.161.54.80:8080) is not in ip table, socket=2112, token=25
[2018-05-08 22:06:05.498][7504][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=111.161.54.80:8080, relay=false, socket=2112, token=25
[2018-05-08 22:06:05.499][7504][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=0, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=2116, token=26
[2018-05-08 22:06:05.499][7504][4][lsp]WSPConnect:protocol=0, type=1, socket=2116, token=26
[2018-05-08 22:06:05.499][7504][5][lsp][Route][NeedRelay] game server IP(111.161.112.107) IDC(2006), will relay socket=2116, token=26
[2018-05-08 22:06:05.499][7504][5][lsp]BindRandomPort bind, port=57714, socket=2116
[2018-05-08 22:06:05.499][7504][4][lsp][TCP]RequestTcpRelaySession: port=57714, socket=2116, token=26
[2018-05-08 22:06:05.499][7504][4][lsp][TCP]RequestTcpRelaySession: CreateNewSession succeed, socket=2116, token=26
[2018-05-08 22:06:05.499][7504][4][lsp]WSPConnect: RequestTcpRelaySession is relayed. relay=127.0.0.1:30108, socket=2116, token=26
[2018-05-08 22:06:05.499][7504][5][lsp]WSPConnect: ret=-1, err=10035, dest=111.161.112.107:80, local port=57714, udp_connect_mode=false, socket=2116, token=26
[2018-05-08 22:06:05.500][7392][4][lsp]WSPAccept: err=0, accept_socket=2124, listen socket=920, token=27
[2018-05-08 22:06:05.500][7392][4][lsp][TCP]OnLocalServerAcceptable. peer_port=57714, local_port=30108, socket=2124, token=26
[2018-05-08 22:06:05.500][7392][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=2128, token=28
[2018-05-08 22:06:05.500][7392][4][lsp][Route][RefineByGltRouteInfo] game launch test route info will not be used!decision=2, game_launch_test_use=true
[2018-05-08 22:06:05.500][7392][4][lsp][Route][FillAccDecisionInfo] route info founded£ºDECISION_NOT_ACCE_SAME_ISP, game IDC(2006), direct delay(12), direct lost(0), proxy IDC(502), t1 delay(2), t1 lost(0), t2 delay(4), t2 lost(0), last_node(1)
[2018-05-08 22:06:05.500][7392][4][lsp][TCP]DecideRemoteAddr.use_acc_=false, ip=111.161.112.107, port=80, socket=2128, token=26
[2018-05-08 22:06:05.500][7392][4][lsp][TCP]ConnectToRemoteServer remote socket=2128, token=26
[2018-05-08 22:06:05.500][7392][5][lsp]WSPConnect: ret=-1, err=10035, dest=111.161.112.107:80, local port=0, udp_connect_mode=false, socket=2128, token=28
[2018-05-08 22:06:05.513][7392][4][lsp][TCP]TcpSession::HandleRemoteWritable, connection is successful. token=26
[2018-05-08 22:06:05.862][9624][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=2464, token=29
[2018-05-08 22:06:05.862][9624][4][lsp][Route][NeedRelay] IP(123.126.47.236:8081) is not in ip table, socket=2464, token=29
[2018-05-08 22:06:05.862][9624][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=123.126.47.236:8081, relay=false, socket=2464, token=29
[2018-05-08 22:06:05.862][9624][4][lsp]WSPSendTo: ret=-1, err=10022, dst=123.126.47.236:8081, relay_send=false, pbuf=0DE6E180, buf_cnt=1, sent_bytes=96059424, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e5c8, socket=2464, token=29
[2018-05-08 22:06:05.862][9624][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=2464, token=29
[2018-05-08 22:06:05.863][9624][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=2464, token=30
[2018-05-08 22:06:05.863][9624][4][lsp][Route][NeedRelay] IP(123.126.47.236:8081) is not in ip table, socket=2464, token=30
[2018-05-08 22:06:05.863][9624][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=123.126.47.236:8081, relay=false, socket=2464, token=30
[2018-05-08 22:06:05.973][8320][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=2484, token=31
[2018-05-08 22:06:05.973][8320][4][lsp][Route][NeedRelay] IP(123.126.47.236:8080) is not in ip table, socket=2484, token=31
[2018-05-08 22:06:05.973][8320][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=123.126.47.236:8080, relay=false, socket=2484, token=31
[2018-05-08 22:06:08.511][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=4024, token=32
[2018-05-08 22:06:08.511][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=4024, token=32
[2018-05-08 22:06:08.511][3676][4][lsp][Route][NeedRelay] inner IP(127.0.0.1), socket=4024, token=32
[2018-05-08 22:06:08.512][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=127.0.0.1:52677, local port=0, udp_connect_mode=false, socket=4024, token=32
[2018-05-08 22:06:08.691][3676][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=4348, token=33
[2018-05-08 22:06:08.691][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=4348, token=33
[2018-05-08 22:06:08.691][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=4348, token=33
[2018-05-08 22:06:08.691][3676][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=4348, token=34
[2018-05-08 22:06:08.691][3676][4][lsp]WSPBind: ret=0, err=0, port=0, socket=4348, token=34
[2018-05-08 22:06:08.700][5200][5][lsp][Route][NeedRelay] game server IP(125.39.255.152) IDC(2006), will relay socket=4348, token=34
[2018-05-08 22:06:08.700][5200][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=125.39.255.152:5270, relay=true, socket=4348, token=34
[2018-05-08 22:06:08.700][5200][5][lsp][UDP] RequestUdpRelay begin, socket=4348, token=34
[2018-05-08 22:06:08.700][5200][5][lsp]ProtoRelayOpen, sock_send_buf_size=262144, sock_recv_buf_size=262144, socket=4348, token=34
[2018-05-08 22:06:08.700][7392][5][lsp][UDP] UdpSession CreateRemoteSession game_server=125.39.255.152:5270, token=34
[2018-05-08 22:06:08.700][7392][4][lsp]RealRouteRecentCycleData::RealRouteRecentCycleData, lost_calc_cycle=5, real_route_cycle_size_=1000, max_high_freq_test_count_=3, watching_time_span_=30000
[2018-05-08 22:06:08.700][7392][4][lsp]RealRouteRecentCycleData::RealRouteRecentCycleData, lost_calc_cycle=5, real_route_cycle_size_=1000, max_high_freq_test_count_=3, watching_time_span_=30000
[2018-05-08 22:06:08.700][7392][5][lsp][UDP] UdpRemoteSession::UdpRemoteSession, data_link_short_cycle_pkg_=20, data_link_short_cycle_lost_=10, data_link_long_cycle_pkg_=30, data_link_long_cycle_lost_=5, max_real_route_lost_=20
[2018-05-08 22:06:08.701][7392][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=17, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=17, socket=4028, token=35
[2018-05-08 22:06:08.701][7392][4][lsp]WSPBind: ret=0, err=0, port=28689, socket=4028, token=35
[2018-05-08 22:06:08.701][7392][5][lsp][UDP] AdjustSocketBuff, previous send_buf=65536, new send_buf=262144, socket=4028
[2018-05-08 22:06:08.701][7392][5][lsp][UDP] AdjustSocketBuff, previous recv_buf=65536, new recv_buf=262144, socket=4028
[2018-05-08 22:06:08.701][7392][5][lsp][UDP] UdpRemoteSession::Init success, remote_ip=125.39.255.152, token=34
[2018-05-08 22:06:08.701][7392][5][lsp][UDP] UdpProvider::ResponseCreateSessionResult ok, addr=127.0.0.1:51184, success=true, ev_result=1, ev_error=0, socket=916, token=34
[2018-05-08 22:06:08.701][5200][5][lsp]RequestUdpRelay success: relay_addr(127.0.0.1:28689), wait_result=0, socket=4348,token=34
[2018-05-08 22:06:08.701][7392][4][lsp][Route][RefineByGltRouteInfo] game launch test route info will not be used!decision=2, game_launch_test_use=true
[2018-05-08 22:06:08.701][7392][4][lsp][Route][FillAccDecisionInfo] route info founded£ºDECISION_NOT_ACCE_SAME_ISP, game IDC(2006), direct delay(12), direct lost(0), proxy IDC(502), t1 delay(2), t1 lost(0), t2 delay(4), t2 lost(0), last_node(1)
[2018-05-08 22:06:08.701][7392][5][lsp][UDP] UdpRemoteSession::DecideAccl result=direct, socket=4028, token=34
[2018-05-08 22:06:10.250][756][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=4612, token=36
[2018-05-08 22:06:10.250][756][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=4612, token=36
[2018-05-08 22:06:10.967][3676][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=4988, token=37
[2018-05-08 22:06:10.967][3676][4][lsp]WSPConnect:protocol=6, type=1, socket=4988, token=37
[2018-05-08 22:06:10.967][3676][4][lsp][Route][NeedRelay] inner IP(127.0.0.1), socket=4988, token=37
[2018-05-08 22:06:10.967][3676][5][lsp]WSPConnect: ret=-1, err=10035, dest=127.0.0.1:52677, local port=0, udp_connect_mode=false, socket=4988, token=37
[2018-05-08 22:06:10.979][1040][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=5000, token=38
[2018-05-08 22:06:10.979][1040][4][lsp]WSPConnect:protocol=6, type=1, socket=5000, token=38
[2018-05-08 22:06:10.979][1040][4][lsp][Route][NeedRelay] inner IP(127.0.0.1), socket=5000, token=38
[2018-05-08 22:06:10.979][1040][5][lsp]WSPConnect: ret=-1, err=10035, dest=127.0.0.1:52677, local port=0, udp_connect_mode=false, socket=5000, token=38
[2018-05-08 22:06:11.065][5196][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=5052, token=39
[2018-05-08 22:06:11.065][5196][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=5052, token=39
[2018-05-08 22:06:11.082][3176][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=0, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=5064, token=40
[2018-05-08 22:06:11.082][3176][4][lsp]WSPConnect:protocol=0, type=1, socket=5064, token=40
[2018-05-08 22:06:11.082][3176][4][lsp][Route][NeedRelay] IP(34.211.204.86:443) is not in ip table, socket=5064, token=40
[2018-05-08 22:06:11.082][3176][5][lsp]WSPConnect: ret=-1, err=10035, dest=34.211.204.86:443, local port=0, udp_connect_mode=false, socket=5064, token=40
[2018-05-08 22:06:11.309][3176][4][lsp]WSPGetPeerName: ret=0, err=0, peer=34.211.204.86:443, socket=5064, token=40
[2018-05-08 22:06:11.993][3176][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=1, socket=5064, token=40
[2018-05-08 22:06:14.751][8224][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=5880, token=41
[2018-05-08 22:06:14.751][8224][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=5880, token=41
[2018-05-08 22:06:20.721][7920][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=5680, token=42
[2018-05-08 22:06:20.721][7920][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=5680, token=42
[2018-05-08 22:06:20.724][7920][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=6, lppro_info=0x05ba235c, group=0, flag=129, downcall_type=6, socket=5680, token=43
[2018-05-08 22:06:20.724][7920][4][lsp]WSPBind: ret=0, err=0, port=0, socket=5680, token=43
[2018-05-08 22:06:20.724][7920][4][lsp]WSPConnectEx: protocol=6, type=1, socket=5680, token=43
[2018-05-08 22:06:20.724][7920][4][lsp][Route][NeedRelay] IP(123.125.110.17:80) is not in ip table, socket=5680, token=43
[2018-05-08 22:06:20.724][7920][5][lsp]WSPConnectEx: ret=0, err=997, dest=123.125.110.17:80, port=0, socket=5680, token=43
[2018-05-08 22:06:20.731][7920][4][lsp]WSPGetPeerName: ret=0, err=0, peer=123.125.110.17:80, socket=5680, token=43
[2018-05-08 22:07:04.572][9908][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=6296, token=44
[2018-05-08 22:07:04.572][9908][4][lsp][Route][NeedRelay] IP(111.161.54.80:8080) is not in ip table, socket=6296, token=44
[2018-05-08 22:07:04.572][9908][4][lsp]IsAllowUdpRelayed SaveRelayRecord, addr=111.161.54.80:8080, relay=false, socket=6296, token=44
[2018-05-08 22:07:05.499][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1856, token=24
[2018-05-08 22:07:05.695][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1864, token=21
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=5680, token=43
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=5680, token=43
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=1848, token=23
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1848, token=23
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=1720, token=19
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1720, token=19
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=1580, token=17
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1580, token=17
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=1556, token=15
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1556, token=15
[2018-05-08 22:07:54.593][3760][4][lsp]WSPRecv: ret=0, err=0, buf_len=1, buf_cnt=1, recv_bytes=0, flag=0, ol=0x00000000, crt=0x00000000, pthd=0x0839e838, socket=1460, token=13
[2018-05-08 22:07:54.593][3760][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=1460, token=13
[2018-05-08 22:08:37.057][1696][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=9080, token=45
[2018-05-08 22:08:37.057][1696][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=9080, token=45
[2018-05-08 22:08:37.074][3176][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=0, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=8636, token=46
[2018-05-08 22:08:37.074][3176][4][lsp]WSPConnect:protocol=0, type=1, socket=8636, token=46
[2018-05-08 22:08:37.075][3176][4][lsp][Route][NeedRelay] IP(34.209.187.10:443) is not in ip table, socket=8636, token=46
[2018-05-08 22:08:37.075][3176][5][lsp]WSPConnect: ret=-1, err=10035, dest=34.209.187.10:443, local port=0, udp_connect_mode=false, socket=8636, token=46
[2018-05-08 22:08:37.299][3176][4][lsp]WSPGetPeerName: ret=0, err=0, peer=34.209.187.10:443, socket=8636, token=46
[2018-05-08 22:08:38.891][3176][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=1, socket=8636, token=46
[2018-05-08 22:10:37.958][10452][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=6864, token=47
[2018-05-08 22:10:37.958][10452][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=6864, token=47
[2018-05-08 22:10:37.975][3176][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=0, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=2896, token=48
[2018-05-08 22:10:37.975][3176][4][lsp]WSPConnect:protocol=0, type=1, socket=2896, token=48
[2018-05-08 22:10:37.975][3176][4][lsp][Route][NeedRelay] IP(52.24.255.158:443) is not in ip table, socket=2896, token=48
[2018-05-08 22:10:37.975][3176][5][lsp]WSPConnect: ret=-1, err=10035, dest=52.24.255.158:443, local port=0, udp_connect_mode=false, socket=2896, token=48
[2018-05-08 22:10:38.201][3176][4][lsp]WSPGetPeerName: ret=0, err=0, peer=52.24.255.158:443, socket=2896, token=48
[2018-05-08 22:10:39.114][3176][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=1, socket=2896, token=48
[2018-05-08 22:11:49.515][3676][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=7052, token=49
[2018-05-08 22:11:49.516][3676][4][lsp]WSPConnect:protocol=0, type=2, socket=7052, token=49
[2018-05-08 22:11:49.516][3676][4][lsp][Route][NeedRelay] IP(123.126.122.27:8000) is not in ip table, socket=7052, token=49
[2018-05-08 22:11:49.517][3676][5][lsp]WSPConnect: ret=0, err=0, dest=123.126.122.27:8000, local port=0, udp_connect_mode=false, socket=7052, token=49
[2018-05-08 22:11:57.224][1040][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=5000, token=38
[2018-05-08 22:11:57.225][3676][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=6, type=1, socket=4988, token=37
[2018-05-08 22:11:58.149][828][4][lsp]WSPSocket: err=0, af=2,type=UDP, overlapped=true, protocol=0, lppro_info=0x05ba27fc, group=0, flag=1, downcall_type=6, socket=8720, token=50
[2018-05-08 22:11:58.149][828][4][lsp]WSPCloseSocket: ret=0, err=0, protocol=0, type=2, socket=8720, token=50
[2018-05-08 22:11:58.167][3176][4][lsp]WSPSocket: err=0, af=2,type=TCP, overlapped=true, protocol=0, lppro_info=0x05ba235c, group=0, flag=1, downcall_type=6, socket=3120, token=51
[2018-05-08 22:11:58.167][3176][4][lsp]WSPConnect:protocol=0, type=1, socket=3120, token=51
[2018-05-08 22:11:58.167][3176][4][lsp][Route][NeedRelay] IP(52.26.91.201:443) is not in ip table, socket=3120, token=51
[2018-05-08 22:11:58.167][3176][5][lsp]WSPConnect: ret=-1, err=10035, dest=52.26.91.201:443, local port=0, udp_connect_mode=false, socket=3120, token=51
[2018-05-08 22:11:58.419][3176][4][lsp]WSPGetPeerName: ret=0, err=0, peer=52.26.91.201:443, socket=3120, token=51
