#!/usr/bin/env python

#Import time
import time

#Used to get information
import openex
import urllib2
import urllib
import re

#Import to convert
from decimal import *

#Configure loops
MainLoop    = 8
TickerLoop  = 1

#Configure sleep
MainSleep    = 1
TickerSleep  = 10

#Configure Openex API
Pubkey  = "input public api key here"
Privkey = "input private api key here"
Market  = "92"
Limit   = "10"
Price   = "1"
Amount  = "1"
Type	= "SELL"

#Get Conversion and convert to readable data
Conv = openex.Conversion(Market, Amount)
ConvFind = Conv.find("Total");
ConvRes = Conv[ConvFind + 8:];
Conversion = ConvRes[0 : 0 +10];

#Get Balance and convert to readable data
Bala = openex.Balance(Pubkey, Privkey, Market)
BalaFind = Bala.find("Balance");
BalaRes = Bala[BalaFind + 10:];
Balance = BalaRes[0 : 0 + 10];

#Grab BTC price
BTCURL = urllib2.urlopen("http://data.mtgox.com/api/1/BTCUSD/ticker")
BTC = BTCURL.read()
BTCFind = BTC.find("last_all")
BTCRes = BTC[BTCFind + 20:]

#Convert to USD and EUR
StringUSD = BTCRes[0 : 0 +6]
StringEUR = BTCRes[0 : 0 +6]

#Convert Balance and Conversion to Decimal and Multiply
BalaDec = Decimal(Balance)
ConvDec = Decimal(Conversion)
ConvUSD = Decimal(StringUSD)

MultBIC = BalaDec * ConvDec
TotalBTC = Decimal(MultBIC)
MultUSD = TotalBTC * ConvUSD

USD = str(MultUSD)
TBTC = str(TotalBTC)

def main(seconds): #Main thread
#Initialise the screen
	print("BLACKBINARY")
	print("Start Ticker")
	print("Version 1.0")
	print("Copyright 2014")
	print("R3H4Bit")

#Starting in 3 seconds
	print("1.")
	time.sleep(MainSleep)
	print("2.")
	time.sleep(MainSleep)
	print("3.")
	time.sleep(MainSleep)
	print("4.")
	time.sleep(MainSleep)
	print("5.")
	time.sleep(MainSleep)

#Display info
	print("Initialised")
	time.sleep(MainSleep)

#Start looping
	for loop in range(MainLoop):
		ticker(MainLoop)
	exit()
	
def ticker(seconds): #Ticker
	for loop in range(TickerLoop):
		print("BINARYCOIN")
		print(Conversion + " BTC")
		print("BIC " + Balance)
		print("BTC " + TBTC)
		print("USD " + USD)

	time.sleep(TickerSleep)
	
if __name__ == "__main__":
#Start main loop
	main(MainLoop)
