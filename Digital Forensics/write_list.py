# this program saves a list of strings to a file

def main():
    #Create a list of strings
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Brownsville']

    #step 1: open a file for writing.
    outfile = open('cities.txt', 'w')

    #step 2: write the list of string to the file.
    for items in cities: 
        outfile.write(items + '\n')

    #step 3: close the file.
    outfile.close()

#call the main function.
if __name__ == '__main__':
    main()