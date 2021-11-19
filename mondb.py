import pymongo


def EX1(mycol):
  myquery = {}

  mydoc = mycol.find(myquery)

  for x in mydoc:
    print(x)

def EX2(mycol):
  myquery = {}
  to_show = {"restaurant_id" : 1, "name" : 1, "borough" : 1, "cuisine" : 1 }

  mydoc = mycol.find(myquery, to_show)

  for x in mydoc:
    print(x)

def EX3(mycol):
  myquery = {}
  to_show = {"restaurant_id" : 1, "name" : 1, "borough" : 1, "cuisine" : 1, "_id": 0}

  mydoc = mycol.find(myquery, to_show)

  for x in mydoc:
    print(x)

def EX4(mycol):
  myquery = {}
  to_show = {"restaurant_id" : 1, "name" : 1, "borough" : 1, "cuisine" : 1, "address.zipcode" : 1, "_id": 0}

  mydoc = mycol.find(myquery, to_show)

  for x in mydoc:
    print(x)

def EX5(mycol):
  myquery = {"borough" : "Bronx"}

  mydoc = mycol.find(myquery)

  for x in mydoc:
    print(x)

def EX6(mycol):
  myquery = {"borough" : "Bronx"}

  mydoc = mycol.find(myquery).limit(5)

  for x in mydoc:
    print(x)

def EX7(mycol):
  myquery = {"borough" : "Bronx"}

  mydoc = mycol.find(myquery).skip(5).limit(5)

  for x in mydoc:
    print(x)

def EX8(mycol):
  myquery = {"grades.score" : {"$gt": 90}}

  mydoc = mycol.find(myquery)

  for x in mydoc:
    print(x)

def EX9(mycol):
  myquery = {"grades.score" : {"$gt": 80, "$lt" : 100}}

  mydoc = mycol.find(myquery)

  for x in mydoc:
    print(x)

def EX10(mycol):
  myquery = {"address.coord" : {"$lt" : -95.754168}}

  mydoc = mycol.find(myquery)

  for x in mydoc:
    print(x)



def main():
  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  mydb = myclient["KING_LIAD_ll"]
  mycol = mydb["kingliad"]

  #EX1(mycol)

  #EX2(mycol)

  #EX3(mycol)

  #EX4(mycol)

  #EX5(mycol)

  #EX6(mycol)

  #EX7(mycol)

  #EX8(mycol)

  #EX9(mycol)

  EX10(mycol)

if __name__ == "__main__":
  main()