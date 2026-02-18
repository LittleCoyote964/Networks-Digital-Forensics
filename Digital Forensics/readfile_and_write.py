#this program reads a file and writes the content to another file
def main():
    #open a file for reading
    infile = open('cities.txt', 'r')

    #read the contents of the file into a list
    cities = infile.readlines()

    #close the file
    infile.close()


    #strip the endline from each element
    for index in range(len(cities)):
        cities[index] = cities[index].rstrip('\n')

    #print the contents of the list
    print(cities)

#call the main function
if __name__ == '__main__':
    main()