#!/bin/bash

MYCOUNTER=0
while [ "$MYCOUNTER" -lt 30 ]; do 
	python2 autoFight.py
	let MYCOUNTER++
done
	
