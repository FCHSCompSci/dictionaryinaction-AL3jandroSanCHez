movie_store={
    'Avengers Infinity War': 19.99,
    'Finding Nemo': 10.49,
    'Titanic': 10.49,
    'Avatar': 12.99,
    'Mission Impossible 6': 19.99,
    'Black Panther': 14.99,
    'Split': 7.49,
    'Murder on the Orient Express': 7.49,
    'Die Hard': 7.49,
    'Terminator 2': 7.49,
    }

movie_rent={
    'Avengers Infinity War': 7.99,
    'Finding Nemo': 5.49,
    'Titanic': 5.49,
    'Avatar': 5.99,
    'Mission Impossible 6': 7.99,
    'Black Panther': 6.99,
    'Split': 6.49,
    'Murder on the Orient Express': 6.49,
    'Die Hard': 6.49,
    'Terminator 2': 6.49,
    }



money = float(input("How much money do you have?"))
movies_question= input("Do you want to [b]uy, or [r]ent a movie? If you want to exit, press x.")
if movies_question.strip() == "b":
    for k,v in movie_store.items():
        print(k,":",v)
    while True:
        movies_bought= input("What movie do you want to buy? If you want to stop buying movies, press s.")
        if movies_bought.strip()== "s":
             break
    
    
