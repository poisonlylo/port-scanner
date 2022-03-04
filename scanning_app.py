#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:47:31 2022

@author: poison_lylo
"""
from scapy.all import *

ports = [25, 80, 53, 443, 8080, 8443]

def SynScan(host) : 
    ans, unans = sr(IP(dst = host) / TCP(sport=5555, dport= ports, flags='S'), timeout = 2, verbose=0)
    print("open port of %s are  : " %host )
    for(s,r,) in ans :
        if (s[TCP].dport == r[TCP].sport) :
            print( s[TCP].dport)
            
def DNSScan(host) : 
    ans,unans = ((IP(dst = host) / UDP(sport=5555, dport= 53 ) / DNS(rd = 1, qd = DNSQR(qname="google.com")),timeout = 2, verbose=0)    
    if (ans) : 
        print("DNS server at %s " %host)             

host = "8.8.8.8"

SynScan(host)
DNSScan(host)