class Node:
	def __init__(self,data):
		self.data=data
		self.head=None
class LinkedList:
	def __init__(self):
		self.head=head
	#Print LL 
	def printList(self):
		temp=self.head
		while (temp):
			temp=temp.next 
			print (temp.data)
	#Insert node at a head of LL 
	def insertAtaHead(self,new_data):
		New_Node=Node(new_data)
		New_Node.next=self.head
		self.head=New_Node
	#Insert node at a specific position
	def insertAtaSpecificPosition(self,prev_node,new_data):
		if prev_node is None:
			return 
		new_node=Node(new_data)
		new_node.next=prev_node.next
		prev_node.next=new_node
	#Insert nodes into LL and insert node at a tail of LL 
	def append(self,new_data):
		New_Node=Node(New_Node)
		if self.head is None:
			self.head=New_Node
			return 
		last=self.head
		#Traverse till the last node
		while(last.next):
			last=last.next
		last.next=New_Node
	#Delete Node in LL (value):
	def DeleteNode(self,value):
		temp=self.head
		if (temp != None):
			if (temp.data == value):
				self.data=temp.next  
				temp=None
				return
		while (temp.next):
			if temp.data == value:
				break #Stop Traverse when meets value
			prev=temp
			temp=temp.next
		if temp == None:
			return print("Value wasnt presented in LL")
		prev.next=temp.next
		temp=None
	#Delete Node in LL (position)	
	def DeleteNodePosition(self,position):
		temp=self.head
		count=0
		if position ==0:
			return head
		else:
			while count > (position -1):
				temp=temp.next
				count +=1
			temp.next=temp.next.next
	#Reverse LL - using iteration (loop):
	def reverse(self):
		head=None
		temp=self.head
		while (temp != None):
			nextnode=temp.next
			temp.next=head
			head=temp
			temp=nextnode
		self.head=head
	#Reverse LL - using recursive:
	def reverse_recursive(self,prev_node,temp):
		if temp.next == None:
			self.head=temp
			temp.next=prev_node
			return
		#Save node for recur calls	
		next_node=next_node.next
		temp.next=prev_node
		#update node 
		self.reverse_recursive(next_node,temp)
	#Call reverse_recursive	
	def reversee(self):
		#previous node as none 
		if self.head is None:
			return
		#call reverse - search youtube for explain, head is changed 	
		self.reversee(self.head,None)
#Compare 2 LL 
def Compare_2_LL(llist1, llist2):
	while (llist1 != None or llist2 !=None):
		if llist1 == None and llist2 != None:
			return 0
		elif llist2 == None and llist1 !=None:
			return 0
		elif llist1.data != llist2.data:
			return 0
		llist1=llist1.next
		llist2=llist2.next
	return 1
#Merge 2 sorted LL 	
def Merge_2_sorted_LL(llis1,llist2):
	head1=llist1.head
	head2=llist2.head
	if head1 == None:
		return head2 
	elif head2 == None:
		return head1
	elif head1.data <= head2.data:
		head=head1
		curr1=head1.next
		curr2=head2
	else: 
		head=head2
		curr1=head1
		curr2=head2.next

	curr=head
	while True: 
		if curr1 is None: 
			curr.next=curr2
			break 
		elif curr2 is None:
			curr.next=curr1
			break 
		elif curr1.data <= curr2.data:
			curr.next=curr1
			curr1=curr1.next
		else: 
			curr.next=curr2
			curr2=curr2.next
		curr=curr.next 
	return head
#Get a Node value in LL 
def GetNodeValue_recur(head,position):
	pHead=head
	count=0
	while (head != None):
		if count > (position-1):
			pHead=pHead.next
		count +=1
		head=head.next
	return head 
def GetNodeValue_non_recur(head,position):
	count=0
	current = head 
	while (head):
		current=current.next
		count +=1
	current = head 
	while (count - position) !=0:
		count -=1
		current=current.next 
	return current.data
def GetNodeValue_recur(head,position):
	if head.next is None:
		return position,head.data 
	count=0
	current=head  
	if (head.next):
		if current > position:
			current=curent.next
		count +=1
		head=head.next
	return current.data
#Another recursive way for getting a node value - make a reference from DatNguyen1999 	
def _getNode(head, positionFromTail):
    if head.next is None:
        return positionFromTail,head.data
    else:
        positionFromTail,_val = _getNode(head.next,positionFromTail)
        print(positionFromTail)
        if positionFromTail == 1 :
            print(head.data)
            return positionFromTail - 1,head.data
        else:
            return positionFromTail - 1,_val
def getNode_stupid_recur(head, positionFromTail):
    _p,_val = _getNode(head,positionFromTail)
    return _val

#Delete Duplicate Node Value:
def removeDupVal(head):
	current=head
	if current == None:
		return head
	while current != None: 
		if current.data ==current.next.data:
			current.next =current.next.next 
		else:
			current=current.next
	return head 
#Cycle Detection 
#Cycle Detection by loop:
def Cycle_Detection_Loop(head):
	fast=head
	slow=head
	while (slow and fast and fast.next):
		slow=head.next 
		fast=head.next.next 
		if slow == fast:
			return True
	return False
#Cycle Detection by Recursion:
def Cycle_Detection_Recur(head):
	visited=[]
	while (head):
		if head in visited:
			return True
		else:
			visited.append(head)
		head=head.next 
	return False

#Find merge point of 2 LL:
def find_merge_point(head1,head2):
	temp1,temp2=head1,head2 
	count1=0
	count2=0
	while (temp1):
		temp1=temp1.next
		count +=1
	while (temp2):
		temp2=temp2.next
		count +=1 
	if (count1 - count2 )>0:
		temp=head1 
		temp_new=head2
		for i in range(count1-count2):
			temp=temp.next
	else:
		temp=head2
		temp_new=head1
		for i in range(count2-count1):
			temp=temp.next 
	while (temp or temp_new):
		if temp == temp_new:
			return temp.data
		temp=temp.next
		temp_new=temp_new.next 
	return False 

#if __name__=="__main__"":
#	llist = LinkedList()  
#    llist.push(1)  
#    llist.push(4)  
#    llist.push(1)  
#    llist.push(12)  
#    llist.push(1)  





	




		










