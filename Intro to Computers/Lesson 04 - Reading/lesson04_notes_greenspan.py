10.32.64.130/1
127.64.128.134/1
#/1 is the sider of the subnet mask
#the first piece is the network address, the other piece is the host (device?) address
#/1 means the first bit is the host address 

2^8, 2^7, 2^6, 2^5, 2^5, 2^4, 2^3, 2^2, 2^1
#10.32.64.130/1 
00001010.00100000.0100000.1000010 #from 10.32.64.130 
10000000.00000000.0000000.0000000 #turn on number of bits (from the left) from sider
#and them together
0|000000.00000000.0000000.0000000 #this becomes my network address
#the result is 
# 0.0.0.0
#the only other possible network address with /1 is
128.0.0.0

#exercise
127.64.128.134/1
01111111.0000000.00000000.00000000
1|0000000.0000000.0000000.0000000
0|0000000.00000000.00000000.00000000
0.0.0.0 #127.64.128.134/1 is on the same network as 10.32.64.130/1 

10.32.64.130/2
00001010.00100000.01000000.10000010
11000000.00000000.00000000.00000000
00000000.00000000.00000000.00000000
0.0.0.0
127.64.128.134/2
01111111.01000000.10000000.10000110
11000000.00000000.00000000.00000000
01000000.00000000.00000000.00000000
64.0.0.0
#10.32.64.130/2 is on a different number than 127.64.128.134/2

#the first IP address of the net is the network address, the last IP is the broadcast address



#there are user experience guides on how to trigger good error messages
#http:200 okay
#http:? dns 

wsl
az network --help | more
man ls
which man
man ls
ls -a -l
ls -l hello/
ls --help       #different than man ls
man ls          #different than ls --help

#w3schools, geeks for geeks
#official documentation (typically most up-to-date)
#official docs
#official tutorials
#online tutorials / guides

az --help | grep virtual
