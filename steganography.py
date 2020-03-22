import cv2
import os

HEADER_FILENAME_LENGTH = 30                                        # Length of filename to be embedded in image
HEADER_FILESIZE_LENGTH = 20                                        # Length of filesize to be embedded in image
HEADER_LENGTH = HEADER_FILENAME_LENGTH + HEADER_FILESIZE_LENGTH    # Total Header length


# ex : n: 104 ---> [011, 010, 00]
getBits = lambda n : [n>>5 , (n & 0x1C) >>2 , (n & 0x3)]           # 0x1C = 00011100

# ex : bits[011, 010, 00] ---> 104
getByte = lambda bits : ((bits[0]<<5)|(bits[1]<<2)|bits[2])

def getFileSize(fileName):
    try:
        return os.stat(fileName).st_size                           # Return the size of the file
    except:
        return 0

def generateHeader(fileName):

    qty = getFileSize(fileName)

    # fileName = d:/Myfolder/file.txt
    # split = [d:, Myfolder , file.txt]

    name = fileName.split('/')[-1]                                 # file.txt
    name = name.ljust(HEADER_FILENAME_LENGTH,'*')                  # file.txt**********************

    qty = str(qty)
    qty = qty.ljust(HEADER_FILESIZE_LENGTH, '*')                   # 409*****************

    return (name + qty)                                            # file.txt**********************409*****************


def embed(resultant_image,source_image,file_to_embed):
    # Load the image
    image = cv2.imread(source_image , cv2.IMREAD_COLOR)
    if image is None:
        print(source_image,"not found!")
        return

    file_size = getFileSize(file_to_embed)
    if(file_size == 0) :
        print(file_to_embed,"not found!")
        return

    height, width , _ = image.shape
    if(height*width < file_size + HEADER_LENGTH):
        print("Insufficient Embedding Space")
        return

    header = generateHeader(file_to_embed)

    fileHandler = open(file_to_embed,'rb')      # open file in read + binary mode

    i = 0
    cnt = 0
    data = 0
    keepEmbedding = True

    while i<height and keepEmbedding:
        j = 0

        while j < width:
            # get data
            if cnt < HEADER_LENGTH:            # either from header
                data = ord(header[cnt])
            else :                             # or from file
                data = fileHandler.read(1)     # read one byte from the file
                if (data) :
                    # as the file is opened in binary mode
                    # so we get byte objects on read. ex : b'> Reading Books (1 hr)\r\n'
                    # the byte object dont support bitwise operations
                    # hence they are to be converted to int
                    data = int.from_bytes(data, byteorder='big')

                else : #EOF
                    keepEmbedding = False
                    break

            bits = getBits(data)

            image[i,j,2] = (image[i,j,2] & ~0x7) | bits[0]  # embed in red band
            image[i,j,1] = (image[i,j,1] & ~0x7) | bits[1]  # embed in green band
            image[i,j,0] = (image[i,j,0] & ~0x3) | bits[2]  # embed in blue band

            cnt+=1
            j+=1

        i+=1

    #close the file
    fileHandler.close()

    #save back the image
    cv2.imwrite(resultant_image,image)
    print('Embedding Done!')


def extract(target_image, save_in_folder):
    # load the image
    image = cv2.imread(target_image,cv2.IMREAD_COLOR)
    if image is None:
        print(image,"not found!")
        return

    height, width , _ = image.shape

    header = ''
    fileHandler = None

    i = 0
    cnt  = 0
    keepExtracting = True

    while i<height and keepExtracting:
        j = 0
        while j<width:
            # extract the data
            bit1 = image[i,j,2] & 0x7  # extract from red band
            bit2 = image[i,j,1] & 0x7  # extract from green band
            bit3 = image[i,j,0] & 0x3  # extract from blue band

            data = getByte([bit1 , bit2 , bit3])

            # put the data
            if cnt < HEADER_LENGTH: # either into the header
                header = header + chr(data)
            else : # or in file
                if cnt == HEADER_LENGTH:
                    fileName = save_in_folder + '/' + header[:HEADER_FILENAME_LENGTH].strip('*')
                    fileSize = int(header[HEADER_FILENAME_LENGTH:].strip('*')) + cnt
                    fileHandler = open(fileName,'wb')

                if cnt< fileSize:
                    data = int.to_bytes(int(data), 1 , byteorder='big')
                    fileHandler.write(data)
                else:
                    fileHandler.close()
                    keepExtracting = False
                    break
            cnt += 1
            j += 1
        i+=1

    print('Extraction Done!')

def main():
    print("Enter your choice : ")
    print("1. Embed the document in the image ")
    print("2. Extract the document from the image")
    choice = int(input("Choice : "));

    if choice == 1 :
        resultant_image = input("Enter the path for the resultant image : ") # ex : g:/result.png
        source_image = input("Enter the path for the source image : ")       # ex : g:/Sagar/Photos/DSC_.jpg
        file_to_embed = input("Enter the path for the file to be embedd : ") # ex : G:/Sagar/Sagar/2020.txt
        embed(resultant_image, source_image , file_to_embed)

    elif choice == 2:
        target_image = input("Enter the target image : ") # i.e the image containing the embedded info. ex: g:/result.png
        save_in_folder = input("Enter the path where the extracted file to be saved : ") # ex : f:
        extract(target_image,save_in_folder)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
