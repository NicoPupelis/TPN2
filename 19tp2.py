class Pelicula:
    def __init__(self, titulo, estudio, anio_estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.anio_estreno = anio_estreno

def peliculas_estrenadas_en_2014(pila):
    return [pelicula.titulo for pelicula in pila if pelicula.anio_estreno == 2014]


def cantidad_peliculas_estrenadas_en_2018(pila):
    return sum(pelicula.anio_estreno == 2018 for pelicula in pila)


def peliculas_marvel_estrenadas_en_2016(pila):
    return [pelicula.titulo for pelicula in pila if pelicula.estudio == "Marvel Studios" and pelicula.anio_estreno == 2016]

peliculas = [
    Pelicula("Avengers: Age of Ultron", "Marvel Studios", 2015),
    Pelicula("Iron Man 3", "Marvel Studios", 2013),
    Pelicula("Guardians of the Galaxy", "Marvel Studios", 2014),
    Pelicula("Black Panther", "Marvel Studios", 2018),
    Pelicula("Doctor Strange", "Marvel Studios", 2016),
    Pelicula("Captain America: Civil War", "Marvel Studios", 2016),
]

peliculas_2014 = peliculas_estrenadas_en_2014(peliculas)
print("Películas estrenadas en 2014:", peliculas_2014)

cantidad_peliculas_2018 = cantidad_peliculas_estrenadas_en_2018(peliculas)
print("Cantidad de películas estrenadas en 2018:", cantidad_peliculas_2018)

peliculas_marvel_2016 = peliculas_marvel_estrenadas_en_2016(peliculas)
print("Películas de Marvel Studios estrenadas en 2016:", peliculas_marvel_2016)

