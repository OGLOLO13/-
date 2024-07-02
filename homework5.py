immutable_var = (13,5.1,"Hello world", False)
print(immutable_var)
#immutable_var[3] = "HI"
#print(immutable_var)

mutable_list = ["Iphone","Samsung","Xiaomi"]
print(mutable_list)
mutable_list[0] = "Sony"
mutable_list.append("Honor")
print(mutable_list)
mutable_list.extend(["Realme"])
print(mutable_list)
