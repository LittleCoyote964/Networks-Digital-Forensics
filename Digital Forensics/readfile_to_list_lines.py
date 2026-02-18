#this program reads a file and shows the lines as a list
def main():
    #open a file for reading
    infile = open('cities.txt', 'r')

    #read the contents of the file into a list
    cities = infile.read()
    print(len(cities))
    print(cities)


    #close the file
    infile.close()

#call the main function
if __name__ == '__main__' :
    main()