

country = "Germany"

if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown country")
    
match country:
    case "United States" | "USA":
        print("US")
    case "India" | "ind":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown country")

