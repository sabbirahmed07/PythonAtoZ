# casefold() - Aggressive lowercasing for case-insensitive comparison
s1 = "Straße"
s2 = "strasse"
print(s1.casefold() == s2.casefold())  # True
print("HELLO".casefold())  # 'hello'
