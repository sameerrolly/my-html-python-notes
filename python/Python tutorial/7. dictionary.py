marks={ "key" : "value" }
print(type(marks))

# creating empty dictionary
dictNew={}
print("empty dictionary: " ,dictNew)

age={
    "sam":24,
    "rolly":10,
    "lucky":30
}
print("age is ",age)
print("items is ",age.items())
print("keys is ",age.keys())
print("Value is ",age.values())
# update method 
age.update({"lucky":20})
print("updated age :",age)
# most imp methods :
print("main topic: 1.get(key),2.[]key")
#print key from dict using 1.[] ,2..get method
print(age["sam"])
print(age.get("sam"))
print("major difference is that if key is not listed :\n 1. .get will show none output \n 2.age[key] : will show error")
# pop method
x=age.pop("sam")
print(age)
# add new value
age["newAge"]=100
print(age)