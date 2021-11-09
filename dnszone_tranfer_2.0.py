import subprocess  
  
def dnsrecon(targets):
    
    # The command you want to execute   
    cmd = 'dnsrecon'
  
    # send one packet of data to the host 
    # this is specified by '-c 1' in the argument list 
    outputlist = []
    # Iterate over all the servers in the list and ping each server
    for target in targets:
        temp = subprocess.Popen([cmd, '-d', target, '-t axfr'], stdout = subprocess.PIPE) 
        # get the output as a string
        output = str(temp.communicate()) 
    # store the output in the list
        outputlist.append(output)
    return outputlist
  
if __name__ == '__main__': 
    
    # Get the list of servers from the text file
    targets = list(open('batch2.txt'))
    # Iterate over all the servers that we read from the text file
    # and remove all the extra lines. This is just a preprocessing step
    # to make sure there aren't any unnecessary lines.
    for i in range(len(targets)):
        targets[i] = targets[i].strip('\n')
    outputlist = dnsrecon(targets) 
    
    # Uncomment the following lines to print the output of successful servers
    print(outputlist)