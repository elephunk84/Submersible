#!/usr/bin/python


import xbox_read

for event in xbox_read.event_stream(deadzone=12000):
        print event
