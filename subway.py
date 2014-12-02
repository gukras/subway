from pylab import *
from numpy import *

def makeGraph(elems, labelsX):

	for elem in elems:
		plot(elem[0],elem[1], elem[2], label=elem[3])
		
	plt.xlabel('Estaciones')
	plt.ylabel('#Personas')
	plt.grid(True)
	plt.xticks(elems[0][0], labelsX, rotation=90 )
	plt.legend()
	show()


def run():

	stationsPre = ["", "", "", "Los Incas", "Tronador", "F.Lacroze", "Dorrego", "Malabia", "A.Gallardo", "Medrano", "C.Gardel", "Pueyrredon", "Pasteur", "Callao", "Uruguay", "C.Pellegrini", "Florida", "Alem"]
	stationsPost = ["", "Rosas", "Echeverria", "Los Incas", "Tronador", "F.Lacroze", "Dorrego", "Malabia", "A.Gallardo", "Medrano", "C.Gardel", "Pueyrredon", "Pasteur", "Callao", "Uruguay", "C.Pellegrini", "Florida", "Alem"]

	InAl300 = np.array([0.0, 0.0, 0.0, 6.0, 12.0, 18.0, 24.0, 30.0, 36.0, 42.0, 44.0, 46.0, 44.0, 42.0, 38.0, 18.0, 8.0, 0.0])
	RoAl300 = np.array([0.0, 6.0, 12.0, 18.0, 24.0, 30.0, 36.0, 42.0, 48.0, 54.0, 56.0, 58.0, 56.0, 54.0, 49.0, 21.0, 10.0, 0.0])

	InAl330 = InAl300 * (7.0/6.0)
	RoAl230 = RoAl300 * (4.0/5.0)

	X = np.arange(len(stationsPost))

	makeGraph([(X, InAl300, 'b', 'Los Incas-Alem, 3:00 Frec')],  stationsPre)
	makeGraph([(X, InAl300, 'b', 'Los Incas-Alem, 3:00 Frec'), (X, InAl330, 'r', 'Los Incas-Alem, 3:30 Frec')],  stationsPre)
	makeGraph([(X, InAl300, 'b', 'Los Incas-Alem, 3:00 Frec'), (X, RoAl300, 'k', 'Rosas-Alem, 3:00 Frec')],  stationsPost)
	makeGraph([(X, InAl300, 'b', 'Los Incas-Alem, 3:00 Frec'), (X, RoAl300, 'k', 'Rosas-Alem, 3:00 Frec'), (X, RoAl230, 'g', 'Rosas-Alem, 2:25 Frec')],  stationsPost)


run()

