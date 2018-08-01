import PokeAPI as po
from tkinter import *

#create a new GUI window
window = Tk()
window.title("Pokedex")

def showPokemonData():
    #get the number typed into the entry box
    pokemonNumber = txtPokemonNo.get()

    #use the function in the 'pokeapi.py' file to get pokemon data
    pokemonDictionary = get_Pokemon(pokemonNumber)

    #get the data from the dictionary and add it to the labels
    lblNameValue.configure(text = pokemonDictionary["name"])
    # lblHPValue.configure(text = pokemonDictionary["hp"])


#a label
lblInstructions = Label(window,text="Enter number 1 and 718:")
lblInstructions.pack()

#an 'entry' textbox
txtPokemonNo = Entry(window)
txtPokemonNo.pack()

#a button
btnGetInfo = Button(window,text="Get Data!", command=showPokemonData)
btnGetInfo.pack()

#labels for the pokemon name
lblNameText = Label(window,text="Name:")
lblNameText.pack()
lblNameValue = Label(window,text="???")
lblNameValue.pack()

lblHPText = Label(window,text="HP:")
lblHPText.pack()
lblHPValue = Label(window,text="0")
lblHPValue.pack()

lblAttackText = Label(window,text="Attack:")
lblAttackText.pack()
lblAttackValue = Label(window,text="0")
lblAttackValue.pack()

lblDefenseText = Label(window,text="Defense:")
lblDefenseText.pack()
lblDefenseValue = Label(window,text="0")
lblDefenseValue.pack()

lblSpeedText = Label(window,text="Speed:")
lblSpeedText.pack()
lblSpeedValue = Label(window,text="0")
lblSpeedValue.pack()








window.mainloop()
