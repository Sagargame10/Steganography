# Steganography
Hiding Documents inside an Image and then extracting them from the image
  
<b>REQUIREMENTS :</b>  
i)   Python3.x (Required only for GUI. CLI mode can be run on Python2.x as well)  
ii)  OpenCV  
iii) Tkinter (Optional : can also run on CLI)  
  
<b> RUN : </b>  
python index.py  
<b>Note : You can directly run steganography.py file for executing program in CLI mode => python steganography.py</b>  
  
Example:   
>> <b>Embed a file:</b>  
> Path for the resultant image => g:/result.png (Here result.png is name of the new image containing document)  
> Path for the source image => g:/Sagar/Photos/DSC_.jpg  
> path for the file to be embedd => g:/Sagar/Document/2020.txt  
  
>> <b>Extract a file:</b>  
> target image => g:/result.png  
> Path for extracted file => F: (or f:/myDoc  , plz note : don't specify '/' after the path)  
  
<b>Note 2 : Use '/' while specifying path. Don't use '\\' </b>
