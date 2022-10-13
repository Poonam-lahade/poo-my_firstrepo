

############################### OR #######################################

def minimum(a, n):
  
    minpos = a.index(min(a))     
    # printing the position 
    print ("The minimum is at position", minpos + 1)
      
# driver code
a = [3, 4, 1, 3, 4, 5] 
minimum(a, len(a))

