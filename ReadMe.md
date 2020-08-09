### Latter & Word Finder Python By NF Py Developers

##### Join Our Telegram Channel [ProgHub09](http://t.me/ProgHub09) and Also Download Our App.

![Demo Image Here](Logo.jpg)


Python File Code :

```
import os

def searchNFG(filename):
    with open (filename , "r") as f:
       filecontent = f.read()

    if val in filecontent.lower():
        return True
    else:
        return False

if __name__ == "__main__":

    dir_content  = os.listdir()
    
    val =  input("\nEnter Latter or Word to Search in Files :\n")
    
    nSearch = 0
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
```