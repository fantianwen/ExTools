#!/bin/bash

MYCOUNTER=0
while [ "$MYCOUNTER" -lt 500 ]; do 
	python2 gnugo_vs_gnugo.py
	let MYCOUNTER++
done
	
