#language:python

import hashlib, binascii                                                          #import the hashlib and binascii for hashing
import DateTime                                                                   #import the datatime modeule for timestamp 
import random                                                                     #import the random module for generating the random number
node_number = 0
class Util:                                                                       #class defined for the hashing purpose
  def hashing(self,*args, *kwrgs):                                                #function takes the argument as args and kwargs
    pass = b''                                                                    #stores the empty string
    r = b ''
    for x in range(10):
      r = r + str(random.randint(1,100))
    for i in args:
      pass = pass + str(i)
    dk = hashlib.pbkdf2_hmac('sha256', b'pass', b'r, 100000)                      #hashes the given owner details and the node details
    return binascii.hexlify(dk)                                                   #returns the hashed value
    
    
class Node:                                                                       #class for creation of the node.
  def time_stamp(self,time):                                                      #method for setting the time.
    self.timestamp = time
  def initilize_node_data(self,object):                                           #method for setting the node value
    self.node_value = object
    
  def nodeNumber(self,num):                                                       #method for setting the node number
    self.node_no = num
    
  def nodeId(self,node_id):                                                       #method for setting the node id
    self.nodeId = node_id
    
  def referenceNodeId(self,refNodeId):                                            #method for setting the reference node id of parent
    self.referenceNodeId = refNodeId
    
  def child_reference_node_id(self, add_of_child):                                #method for setting the child reference number of the child
    self.reference_of_node = add_of_child
    
  
class NodeValue:                                                                  #class for the information of the node value
  def node_id(self,id):                                                           #method for setting the node id
    self.Id = id
  def get_node_id(self):                                                          #to return the node id
    return self.id
   def node_value(self,value):                                                    #method to set the node_value
    self.value = value
   def get_node_value(self):
    return self.value
   def node_owner_name(self,name):                                                #method to set the owner of the node
    self.name = name
   def get_node_owner_name(self):
    return self.name
   def node_owner_id(self,owner_id):                                             #method to set the owner id of the node
    self.owner_id = owner_id
   def get_node_owner_id(self):
    return self.owner_id
   
   
   
  if __name__ == __main__:                                                      #main function to allow the users to interact
    select = input("select among the following/n1.Create/n2.Exit")
    if(select == 1):
      owner_name = input("Enter the name of the owner")
      owner_id = input("Enter the owner id")
      commit = input("1.Create/n2.Exit")
     if(commit == 1):
      data = NodeValue()
      data.node_value()
      data.node_owner_name()
      data.node_owner_id()
      data.node_id()
      node_owner_id += 1
      data.HASH_VALUE = Util().hash(data.get_node_value(),data.get_owner_id, data.get_owner_name())
     else:
     exit()
