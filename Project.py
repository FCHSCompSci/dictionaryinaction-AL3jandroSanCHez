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



def sum_movies(movies):
    return sum(movies)
    

def buy_movie(movies):
    account= money - sum(movies)
    return account
money_movies=[]

while True:
    movies_question= input("Do you want to [b]uy, or [r]ent a movie?")


    if movies_question.strip() == "b":
        movie_mine = movie_store
    
        for k,v in movie_store.items():
            print(k,": $",v)
        break
        
    elif movies_question.strip() == "r":
        movie_mine = movie_rent
    
        for k,v in movie_rent.items():
            print(k,": $",v)
        break
       
    else:
        print("That is not valid input!")
    
money = float(input("How much money do you have?"))


while True:
       
    movies_bought=input("Type one movie you want to buy or rent, press [s] to stop buying movies and get your receive.")
    
    
    if movies_bought != "s":
        money_movies.append(movie_mine[movies_bought.title().strip()])
    else:
        print("Your receive is $%.2f, and you have now $%.2f." %(sum_movies(money_movies), buy_movie(money_movies)))
        break







# Ask user for movies they want to buy AND if they want to stop buying movies, type X
# Everytime the user enters a movie, append movie to a list.
# inside your function then use list, to loop over, and get dictionary values as you loop through the list of movies







