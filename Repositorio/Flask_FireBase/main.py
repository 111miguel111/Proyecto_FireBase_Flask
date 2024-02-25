from model import BBDD


for i in BBDD.selectAll("libros"):
    print(i)