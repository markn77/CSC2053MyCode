alist = [10,20,30,40,50]

alist.append(5)
alist.append(6)
alist.append(7)
print(alist)

alist.remove(50)
alist.pop(2)
print(alist)
alist.sort()
print(alist)

empty = [0] * 10
empty[0] = 10
print(empty)

dog = "dog"
dogs = dog *3
print(dogs)

empty=[]
for value in alist:
    if value >= 7 and value <= 20:
        empty.append(value)
print(empty)

squares = []
for i in range(1,10):
    squares.append(i*i)

print(squares)
squares_copy = squares
# squares[0] = 9000
print(squares_copy)

squares_copy = [value for value in squares if value > 9]
squares[0]=9000
print(squares_copy)

even_num = [i for i in range(2,101) if i % 2 == 0]
print(even_num)

# Sets
aset = {1,2,700,5,6,100}
print(aset)

dups = [1,2,2,3,3,6,6,7,7,1]
no_dups = set(dups)
print(no_dups)
# no_dups[0]=100
no_dups.add(8)
print(no_dups)

fav_foods = {"kathleen" : "pizza", "george" : "lobster",
             "nick" : "pasta bolognese", "kai" : "alfredo"}

kai_ff = fav_foods["kai"]
print(kai_ff)
print(fav_foods)

# kim_ff = fav_foods["kim"]
if "kim" in fav_foods:
    print(fav_foods["kim"])
else:
    fav_foods["kim"] = "cereal"

for key in fav_foods:
    print(key, "fav food is", fav_foods[key])

# for key, value in fav_foods.items():

cities = {}
cities[19333] = "Devon"
city = cities[19333]
print(city)