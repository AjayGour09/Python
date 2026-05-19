userName = input("What is Your Name : ")
print(f"Good Morning {userName}");

letter = '''
Dear <|Name|> ,
you are selected !
<|Date|>'''
print(letter.replace("<|Name|>","Ajay").replace("<|Date|>","18 Aug"))

sub ="I am the leader of this World"
newSub = sub.find("am");
print(newSub)