while True:
	country = input("请输入你的国家")
	if country == "Taiwan" :
		age = (input("请输入你的年龄"))
		age = int(age)
		if age < 18:
			print("你还不可以考驾照")
		elif age >= 18 and age < 80:
			print("你可以考驾照")
		elif age >=80 :
			print("开车危险!")
		else:
			print("请输入年龄")
	elif country == "America":
		age = (input("请输入你的年龄"))
		age = int(age)
		if age >= 16:
			print("你可以考驾照")
		else:
			print("你还不可以考驾照")
	else :
		print(input("请输入正确国家,下次再来"))
		break


