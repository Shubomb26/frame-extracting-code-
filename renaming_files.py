import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir('C:\\Users\\singh\\OneDrive\\Desktop\\exact images\\')):
        dst ="tencent_" + str(count) + ".jpg"
        src ='C:\\Users\\singh\\OneDrive\\Desktop\\exact images\\'+ filename
        dst ='C:\\Users\\singh\\OneDrive\\Desktop\\exact images\\img_'+ dst
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
