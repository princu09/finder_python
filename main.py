import os

# Function For Read File 

def searchNFG(filename):
    with open (filename , "r") as f:
       filecontent = f.read()

    if val in filecontent.lower():
        return True
    else:
        return False

if __name__ == "__main__":

    # List All Files and Direcatory
    dir_content  = os.listdir()

    # Get Input From User    
    val =  input("\nEnter Latter or Word to Search in Files :\n")
    
    nSearch = 0
    
    # Search Word in Files
    for item in dir_content:
        if item.endswith('txt'):
            print(f"Detecting {val} in {item}")
            flag =  searchNFG(item)
            if (flag):
                print(f"{val} found in {item} \n" )
                nSearch +=1
            else:
                print(f"{val} not found in {item} \n")

    print(f"{nSearch} Latter found with {val} Hidden into them")