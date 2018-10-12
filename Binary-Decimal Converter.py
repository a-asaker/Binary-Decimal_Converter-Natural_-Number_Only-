#!/usr/bin/env python3
#By : A_Asaker

def DecToBin():
	num=input("\n Enter The Decimal Number : ")
	return bin(int(num))[2:]

def BinToDec(num):
	num=int(num,2)
	return num

def IsBin():
	num=input("\n Enter The Binary Number : ")
	print("")
	bol=1
	for z in num:
		if z != "0" and z!= "1":
			bol=0
			break
		else:
			bol=1
	while bol==0:
		num=input("\n Please Enter A Binary Number : ")
		for z in num:
			if z != "0" and z!= "1":
				bol=0
				break
			else:
				bol=1
	return BinToDec(num)

def main():
	print("\n (1) Decimal To Binary","\n")
	print(" (2) Binary To Decimal","\n")
	x=input(" #===================# >( 1 || 2 ): ")
	if x == '1':
		print("\n ",DecToBin(),"\n")
	elif x == '2':
		print("\n ",IsBin(),"\n")
	else:
		print("\n Go Play Far Away ! \n")
		exit()
			
main()


''' converts from bin to deci
----------------------------------------
	Another Method (1):
	conv_num=0
	n=len(num)
	for x in num:
		n=n-1
		conv_num=conv_num+(int(x)*(2**(n)))
	print(conv_num,"\n")
-----------------------------------------
	Another Method (2):
	num = input()
	conv_num = 0
	for x in num:
	     conv_num = conv_num*2 + int(x)
	print(conv_num)
	'''
