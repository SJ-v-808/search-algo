#server

import database

#your data base
mydata = database.lyrics

#your search algorithm
def search_algo(user_input):
    print("")
    print("[searching.........]")
    #<algo>
    #{put ur algo here}
    #</algo>
    print("[searched completed]")
    print("")
    print("> you searched for",user_input)
    result = "> here is ur lyrics search result" #return your search result here
    return result
