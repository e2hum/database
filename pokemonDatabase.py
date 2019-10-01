# Evan Hum

import csv

class Pokemon:

    def __init__(self):

        self._pokemon = self._openFile()
        self._newPokemon = None
        

    @classmethod
    def _openFile(cls):
        with open("pokemon.csv", encoding = "utf-8") as fileIn:
            reader = csv.DictReader(fileIn)

            pokeDict = []

            for line in reader:
                pokeDict.append(line)
                
        return pokeDict

    def pokemonType(self, pokemonType):

        myType = []
        for line in self._pokemon:
            if line["type1"] == pokemonType or line["type2"] == pokemonType:
                myType.append(line)

        self._newPokemon = myType
        return myType

    def pokemonGeneration(self, generation):

        gen = []
        for line in self._pokemon:
            if int(line["generation"]) == generation:
                gen.append(line)
        self._newPokemon = gen
        return gen
    
    def happiness(self, low):

        happy = []
        for line in self._newPokemon:
            if int(line["base_happiness"]) >= low:
                happy.append(line)

        self._newPokemon = happy

        return happy
    
    def HPmin(self, low):

        HP = []
        for line in self._newPokemon:
            if int(line["hp"]) >= low:
                HP.append(line)

        self._newPokemon = HP
                
        return HP
    
    def weightMin(self, low):

        weight = []
        for line in self._newPokemon:
            #The Try and except is used since some pokemon have no weight
            #This way the program doesn't crash when trying to convert
            #nothing into a float
            try:
                if float(line["weight_kg"]) >= float(low):
                    weight.append(line)
                    
            except ValueError:
                pass


        self._newPokemon = weight

        return weight

    def legendary(self):
        legends = []
        for line in self._newPokemon:
            if int(line["is_legendary"]) == 1:
                legends.append(line)

        self._newPokemon = legends

        return legends

    def printPokemon(self):
        pokemonList = []
        for line in self._newPokemon:
            pokemonList.append(line["name"])

        print(pokemonList)

        info = input("\nIf you would like to see all the information for these Pokemon"
                     " type \"Yes\"\n")
        if info == "Yes":
            print(self._newPokemon)
        
        
class menu:

    @staticmethod
    def intro():
        print("This is the Pokemon Filter!\n"
              "Follow instructions below to start filtering.")

        choice1, option1 = menu.filter1()

        choice2, option2 = menu.filter2()

        legendary = menu.filter3()
        
        return choice1, option1, choice2, option2, legendary

        
    @staticmethod
    def filter1():
        choice = int(input("\nOption 1:\n1. Types\n2. Generations\n"))
        if choice == 1:
            option = input("\nPlease select a type (water, flying, ice, etc.):\n")

        elif choice == 2:
            option = int(input("\nPlease select a generation (1-7):\n"))

        return choice, option
    
    @staticmethod
    def filter2():
        print("\nSelect a second filter: ")
        choice2 = int(input("Option 2:\n1. HP Minimum\n2. Happiness Minimum\n"
                    "3. Weight Minimum\n"))

        #For testing purposes, try using a lower value since the upper
        #limit is the maximum value
        if choice2 == 1:
            option2 = int(input("\nEnter a minimum from 1 - 255:\n"))

        elif choice2 == 2:
            option2 = int(input("\nEnter a minimum from 0 - 140:\n"))

        elif choice2 == 3:
            option2 = int(input("\nEnter a minimum from 1 - 500:\n"))

        return choice2, option2

    @staticmethod
    def filter3():
        print("\nWould you like to turn on the legendary filter?")
        choice3 = int(input("1. Yes\n2. No\n"))
        if choice3 == 1:
            legendary = True
        else:
            legendary = False
        return legendary

def main():
                        
    start = menu()
    choice1, option1, choice2, option2, legendary = start.intro()

    team = Pokemon()

    if choice1 == 2:
        round1 = team.pokemonGeneration(option1)

    else:
        round1 = team.pokemonType(option1)

    if choice2 == 1:
        round2 = team.HPmin(option2)

    elif choice2 == 2:
        round2 = team.happiness(option2)

    elif choice2 == 3:
        round2 = team.weightMin(option2)

    if legendary == True:
        legends = team.legendary()
 
    team.printPokemon()

main()
    



        






