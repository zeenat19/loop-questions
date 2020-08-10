language=input("enetr any language:")
if language=="hindi" or language=="english" or language=="karnataka":
	print("acseapted your",language)
	pin_code=int(input("enter any any pincode:"))
	if pin_code==1347:
		print("acseapt your pincode")
		type_acount=input("enter any type_acount:")	
		if type_acount=="curunt" or type_acount=="joint":
			print("acsept your ",type_acount)
			amount=int(input("enter any amount:"))
			total_mony=6000			
			if amount>total_money or amount<=total_money:
				print("we can withdraw the ",amount)
				transaction=int(input("enter your money:"))
				if transaction<amount or transaction>amount:
					print("we can", transaction)
					print(amount-transaction)
				else:
					print("you cant transaction")
			else:
				print("we can not withdraw the account")
		else:
			print("not acseapted your",type_acount)
	else:
		print("your pin_code is not acsept")
else:
	print("not acsept your",language)

