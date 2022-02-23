#Inteligencia Artificial
#Tarea2
#Gabriel Quiroz
#Jose Pablo Ponce
#Guido Padila
#Oscar Paredez


class Arista:
	def __init__(self, primero, segundo):
		self.primero = primero
		self.segundo = segundo


class Vertice:

	def __init__(self, numVertice):	
		self.numVertice = numVertice
		self.hijo = []

	def anadirHijo(self, destVertice, distancia):
		p = Arista(destVertice, distancia)
		self.hijo.append(p)
	
def dijkstra(g, s, camino):

	dist = [infi for i in range(len(g))]

	recorrido = [False for i in range(len(g))]
	
	for i in range(len(g)):	
		camino[i] = -1
	dist[s] = 0
	camino[s] = -1
	actual = s

	sett = set()	
	while (True):

		recorrido[actual] = True
		for i in range(len(g[actual].hijo)):
			v = g[actual].hijo[i].primero;		
			if (recorrido[v]):
				continue

			sett.add(v)
			alt = dist[actual] + g[actual].hijo[i].segundo

			if (alt < dist[v]):	
				dist[v] = alt
				camino[v] = actual
		if actual in sett:		
			sett.remove(actual)
		if (len(sett) == 0):
			break

		minDist = infi
		index = 0

		for a in sett:	
			if (dist[a] < minDist):		
				minDist = dist[a]
				index = a;		
		actual = index
	return dist

infi = 1000000000

def printcamino(camino, i, s):
	if (i != s):
		
		if (camino[i] == -1):	
			print("camino not found!!")
			return;	
		printcamino(camino, camino[i], s)
		print(camino[i]+1)

lista = []
with open("lab2.txt","r") as archivo:
    for linea in archivo:
        lista.append([n for n in linea.strip().split(' ')])
	
v = []
n = int(lista[0][0])


origen = int(input("Ingresa el nodo de origen \n")) -1
fin = int(input("Ingresa el nodo de destino\n")) -1


for i in range(n):
    a = Vertice(i)
    v.append(a)

for i in range(2,len(lista)):
	v[int(lista[i][0])-1].anadirHijo(int(lista[i][1])-1,int(lista[i][2]))

camino = [0 for i in range(len(v))]
dist = dijkstra(v, origen, camino)

print("La distancia al vertice {} desde el vertice inicial {} es: {}".format(
				fin+1, origen+1, dist[fin]))

print("\nCamino optimo para llegar al nodo destino es:")
printcamino(camino, fin, origen)

