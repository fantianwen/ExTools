#!/bin/bash

MYCOUNTER=0
while [ "$MYCOUNTER" -lt 500 ]; do 
	python2 autoFight_15.py
	let MYCOUNTER++
done
	
