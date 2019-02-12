#!/bin/bash

MYCOUNTER=0
while [ "$MYCOUNTER" -lt 500 ]; do 
	python2 autoFight_25.py
	let MYCOUNTER++
done
	
