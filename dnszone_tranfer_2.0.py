import subprocess  
  
def dnsrecon(targets):
    
    cmd = 'dnsrecon'

    outputlist = []
    for target in targets:
        temp = subprocess.Popen([cmd, '-d', target, '-t axfr'], stdout = subprocess.PIPE) 
        output = str(temp.communicate()) 
        outputlist.append(output)
    return outputlist
  
if __name__ == '__main__': 
    
    targets = list(open('batch2.txt'))
    for i in range(len(targets)):
        targets[i] = targets[i].strip('\n')
    outputlist = dnsrecon(targets) 
    
    print(outputlist)