def fun1(a,b=0, *args,**kwargs):
	print(a+b)
	print(args)
	print(kwargs)
	
fun1(5,6,'hola',55,66,0.4,name = 'gaurang',surname = 'manchekar')