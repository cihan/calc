#!/usr/bin/env python
#-*- coding: utf-8 -*-

def topla(a,b):
	sonuc= a+b
	return sonuc

def cikar(a,b):
	sonuc= a-b
	return sonuc

def carp(a,b):
	sonuc=a*b
	return sonuc

def bol(a,b):
	sonuc=a/b
	return sonuc

a= int(raw_input("İlk sayıyı giriniz: "))
b= int(raw_input("İkinci sayıyı giriniz: "))
islem = raw_input("İşlem: \ntopla-cikar-carp-bol\n")

if islem == "topla":
	print topla(a,b)
elif islem == "cikar":
	print cikar(a,b)
elif islem == "carp":
	print carp(a,b)
elif islem == "bol":
	print bol(a,b)
else:
	print "İşlemi yanlış girdiniz..."
	
