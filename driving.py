country = input("请输入你的国家")
age = input("请输入你的年龄")
age = int(age)
if country == "Taiwan":
	if age >= 18:
		print("你可以考驾照")
	else:
		print("你还不可以考驾照")
elif country == "America":
	if age >= 16:
		print("你可以考驾照")
	else:
		print("你还不可以考驾照")
else:
	print("请输入Taiwan或America")
