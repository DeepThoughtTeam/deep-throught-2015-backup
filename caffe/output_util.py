import json
import requests

#test
def testToJson(filepath, dic):
    with open(filepath) as f:
        last = False;
        for line in f:
            if last == False:
                if 'Batch' in line:
                    start = line.index('Batch')
                    [key, val] = line[start:].split(',')

                    [batch_str, num] = key.split(' ')
                    if len(num) < 2:
                        num = '0' + num
                    key = batch_str + " " + num

                    val = val[1:-1]
                    if key in dic:
                        val = val + ', ' + (dic[key])
                    dic[key] = val    
                    
                if 'Loss: ' in line:
                    indx = line.index('Loss')
                    dic["Batch Final"] = line[indx:-1]
                    last = True

            elif 'accuracy' in line:
                indx = line.index('accuracy')
                val = dic['Batch Final']
                val = val + ', ' + line[indx:-1]
                dic['Batch Final'] =  val

# train                
def processNode(node): 
    accy = node[0]
    val = accy[accy.index('accuracy'):-1]
    loss = node[1]
    val = val + ', ' + loss[loss.index('loss'):-1]
    lr = node[4]
    val = val + ', ' + lr[lr.index('lr'):-1]
    key_str = node[2]    
    key_start = key_str.index('Iteration')
    key_end = key_str.index(',')
    key = key_str[key_start: key_end]

    [batch_str, num] = key.split(' ')
    offset = 5 - len(num)
    while offset > 0:  
        num = '0' + num
        offset = offset - 1

    key = batch_str + " " + num

    return (key, val)

def trainToJson(filepath, dic):
    with open(filepath) as f:
        skip_head = True
        test = 0
        node_size = 6
        node = []
        for line in f:
            if skip_head:
                if 'Iteration' in line:
                    skip_head = False
                
            elif 'accuracy' in line: 
                node_size = 1  
            
            if node_size < 5:
                node_size += 1
                node.append(line)
                
            elif node_size == 5:
                node.append(line)
                node_size = 6
                (key, val) = processNode(node) 
                node = [] 
                dic[key] = val