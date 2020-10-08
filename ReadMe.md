## Latter & Word Finder Python By NF Py Developers

##### 📫 Connect with me here:<br />
 <br />
 <p>
  <a target="_blank" href="https://www.instagram.com/princu.09">
    <img src="https://img.shields.io/badge/princu.09-386938188?style=flat&logo=instagram&color=black">
  </a> &nbsp; 
  <a target="_blank" href="https://twitter.com/princu09">
    <img src="https://img.shields.io/badge/@princu09-30302f?style=flat&logo=twitter&color=black">
  </a>&nbsp; 
  <a target="_blank" href="https://github.com/princu09">
    <img src="https://img.shields.io/badge/@princu09-30302f?style=flat&logo=github&color=black">
  </a>&nbsp;
    <a target="_blank" href="https://www.t.me/proghub09">
    <img src="https://img.shields.io/badge/ProgHub09-386938188?style=flat&logo=telegram&color=black">
  </a>
</p>


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
