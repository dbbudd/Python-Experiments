#!/bin/bash

/opt/vc/bin/raspivid -vf -fps 5 -o - -w 640 -h 360 -t 0 | nc.traditional 192.168.100.76 5000
