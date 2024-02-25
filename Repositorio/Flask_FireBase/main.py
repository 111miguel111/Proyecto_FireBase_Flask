from model import BBDD


for i in Connection.selectAll("libros"):
    print(i)