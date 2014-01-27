#!/usr/bin/env python
import urllib
import urllib2
import re

APIURL = "https://www.openex.pw/api.php"

def PrivTradeHistory(Pubkey, Privkey, Market, Limit):
	global PrivTradeHistory
	Method  = "&Method=GetPrivTradeHistory"
	Pubkey  = "?Pub="      + Pubkey
	Privkey = "&Priv="     + Privkey
	Market  = "&MarketId=" + Market
	Limit   = "&Limit="    + Limit
	Response         = urllib2.urlopen(APIURL + Pubkey + Privkey + Method + Market + Limit)
	PrivTradeHistory = Response.read()
	return PrivTradeHistory

def NewTrade(Pubkey, Privkey, Market, Price, Amount, Type):
	global NewTrade
	Method  = "&Method=CreateNewTrade"
	Pubkey  = "?Pub="     + Pubkey
	Privkey = "&Priv="    + Privkey
	Price   = "&Price="   + Price
	Amount  = "&Amount="  + Amount
	Type    = "&Type="    + Type
	Market  = "&MarketId=" + Market
	Response = urllib2.urlopen(APIURL + Pubkey + Privkey + Method + Price + Amount + Type + Market)
	NewTrade = Response.read()
	return NewTrade

def Balance(Pubkey, Privkey, Market):
	global Balance
	Method  = "&Method=GetBalance"
	Pubkey  = "?Pub="    + Pubkey
	Privkey = "&Priv="   + Privkey
	Market  = "&MarketId=" + Market
	Response = urllib2.urlopen(APIURL + Pubkey + Privkey + Method + Market)
	Balance  = Response.read()
	return Balance

def TradeHistory(Market, Limit):
	global TradeHistory
	Method  = "?Method=GetTradeHistory"
	Market  = "&MarketId=" + Market
	Limit   = "&Limit="    + Limit
	Response     = urllib2.urlopen(APIURL + Method + Market + Limit)
	TradeHistory = Response.read()
	return TradeHistory

def MarketData(Market):
	global MarketData
	Method  = "?Method=GetMarketData"
	Market  = "&MarketId=" + Market
	Response   = urllib2.urlopen(APIURL + Method + Market)
	MarketData = Response.read()
	return MarketData

def Conversion(Market, Amount):
	global Conversion
	Method  = "?Method=GetConversion"
	Market  = "&MarketId=" + Market
	Amount  = "&Amount="   + Amount
	Response   = urllib2.urlopen(APIURL + Method + Market + Amount)
	Conversion = Response.read()
	return Conversion