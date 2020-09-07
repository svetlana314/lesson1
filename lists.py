s = {
    "city": "Москва",
    "temperature": "20"
}
s["temperature"] = int(s["temperature"]) -+ 5
s.get("country", "Россия")
s["date"] = "27.05.2019"
print(s)
print(len(s))