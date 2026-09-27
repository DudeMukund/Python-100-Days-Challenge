country_capitals = {
    "france": "parise",
    "Germany": "Berlin",
    "india" : "new delhi"

}

# nested lited in dictionary
travel_log = {
    "india" : ["delhi", "bihar", "chattisgarh","utterpradesh"]

}
print(travel_log["india"][1]) # bihar

#nested list in list
nested_list = ["A","B",["c","D"]]
#print C
print(nested_list[2][0])


#nested dictionary in disctionary:
travel_log = {
    "india" : {"delhi":3, "bihar":50, "chattisgarh" : 4,"utterpradesh" :2
    },
    "China":{"shanghai":2}
}
 # print how many time you vist chattisgarh:
print(f"{travel_log["india"]["chattisgarh"]} times")


