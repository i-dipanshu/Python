f = open('Chapter 9\sample_write.txt', 'w') # Overrides the prev. data and writes
f.write("Please write to the file") 
f = open('Chapter 9\sample_write.txt', 'a') # adds text at end of file
f.write(". I am appending")
f.close()