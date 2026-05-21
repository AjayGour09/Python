marks ={
    "Ajay" :100,
    "Nitish":43,
    "Arun":43,
    "vinode":90,
}
print(type(marks))
print(marks["Ajay"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ajay":99})
print(marks)
print(marks.get("Ajay"))