midiccionario = {
	1:"hola",
	2:"que",
	3:"ase",
	"nombre":"Israel",
	"blog":"uno de piera",
	"lista":[1,2,3,4],
	"tupla":(1,2,3,4,5,6,7,8),
	"diccionario_tupla":{"tupla":[1,2,3,4]},
	"diccionario_lista":{"lista":(1,2,3,4,5,6,7,8)}
}

for d in midiccionario:
	if d == "tupla":
		for l in midiccionario[d]:
			print("%s %d" % ("lista valor",l))
	elif d == "tupla":
		for t in midiccionario[d]:
			print("%s %d" % ("tupla valor",t))
	else:
		print(midiccionario[d])
