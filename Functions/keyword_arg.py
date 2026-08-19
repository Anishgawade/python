def subject(english, hindi, marathi, history=0):
    print(f"English = {english}")
    print(f"Hindi = {hindi}")
    print(f"Marathi = {marathi}")
    print(f"History = {history}")
    print(f"Total marks  = {english + hindi + marathi + history}")

subject(20, hindi=50, marathi=20)