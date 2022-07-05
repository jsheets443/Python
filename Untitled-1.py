camping_list = ["tent", "sleeping bag", "raspberry pi", "knife", "hatchet", "axe", "water", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]
#lists can hold different data types, string, int, boolean, float and any other

camping_list.append("toilet paper")
camping_list.append('bidet')
#append to add a single item to list

camping_list.extend(["ethernet cable", "tarp", "fishing poles"])
#extend and [] to add new list of items to initial list
#can also be done by list name + [new list]

camping_list.insert(0, "tomahawk")
#insert[index location, "string entry"]

print(camping_list)