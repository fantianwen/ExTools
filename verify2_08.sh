#!/bin/bash

MYCOUNTER=0
while [ "$MYCOUNTER" -lt 500 ]; do 
	python2 autoFight_08.py
	let MYCOUNTER++
done
	
