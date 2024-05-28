import sys
from tkinter import Tk, simpledialog, messagebox

# read country and capital from file
def read_from_file():
    with open('worldcapital.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n') # remove newline character
            country, capital = line.split('/') # split the line into country and capital
            country = country.capitalize() # capitalize = capital character
            capital = capital.capitalize()
            world_capital[country] = capital

# write country and capital to file
def write_to_file(country_name, capital_name):
    with open('worldcapital.txt', 'a') as file:
        file.write('\n')
        file.write(country_name + '/' + capital_name)  
        file.close()

# main program
root = Tk() # create a window
root.withdraw() # hide the window
world_capital = {} # create an empty dictionary
while True:
    read_from_file()
    simpledialog.askstring
    query_country = simpledialog.askstring('Country', 'Enter the country name: ')
    query_country = query_country.capitalize()
    if query_country in world_capital: # check if the country is in the dictionary
        result = world_capital[query_country]
        messagebox.showinfo('Answer', 'The capital of ' + query_country + ' is ' + result + '!')
    else: # if the country is not in the dictionary
        new_capital = simpledialog.askstring('Teach me', 'I don\'t know the answer. Please teach me. What is the capital of ' + query_country + '?')
        messagebox.showinfo('Thanks', 'Thank you for teaching me. I will definitely know it next time!')
        write_to_file(query_country, new_capital)
    answer = simpledialog.askstring('Continue', 'Do you want to continue? (y/n): ')  
    if answer == 'n':
        messagebox.showinfo('Thanks', 'Thank you for using the program. Goodbye!')
        root.destroy()
        sys.exit()