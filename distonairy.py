u = {'sezan':43,"HOQU":84,"rewqan":54,"MR":44,"mango":97}
print(len(u))
print(u.keys())
print(u.values())
print(type(u))
x = 1
while (x <= 10):
    print("sezan",x)
    x += 1

i = 0
while(i <= 10):
    print(i)
    i+=1

i = 0 
while ( i <= 30):
    print(i,"sezan")
    i+=1
for i in range( 5,9 ):
    print(i,"sezan")

# new dictonary 

students_scores = {
    "Alice": {"Math": 85, "Economics": 90, "Physics": 78},
    "Bob": {"Math": 92, "Economics": 88, "Physics": 84},
    "Charlie": {"Math": 80, "Economics": 75, "Physics": 89}
}
 

print(len(students_scores))

print(students_scores.keys())
print(students_scores.values())
del(students_scores["Bob"]["Math"])
# students_scores["Alice"]["Economics"] = 100
print(students_scores)

students_scores.update({"sezan":{"math": 100,"economics": 93}})
print(students_scores)