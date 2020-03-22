# Steganography
Hiding Documents inside an Image and then extracting them from the image

<b>REQUIREMENTS :</b>  
i)   Python3.x (Can also work with Python2.x only change is to made in import tkinter to import Tkinter)  
ii)  OpenCV  
iii) Tkinter (Optional : can also run on CLI)  

<b> RUN : </b>  
python index.py  
  
EX:   
>> Embed a file:  
> Path for the resultant image => g:/result.png (Here result.png is name of the new image containing document)  
> Path for the source image => g:/Sagar/Photos/DSC_.jpg  
> path for the file to be embedd => g:/Sagar/Document/2020.txt  
  
>> Extract a file:
> target image => g:/result.png  
> Path for extracted file => f: (or f:/myDoc , plz note : don't specify '/' after the path)  
  
<b>Note 1 : You can directly run steganography.py file for executing program in CLI mode</b>  
<b>Note 2 : Use '/' while specifying path. Don't use '\' </b>
