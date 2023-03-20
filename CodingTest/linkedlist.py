#한방향 vs 양방향


#한방향 리스트 - Linked List 만들어보기
class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
    def __str__(self): #프린트에 노드를 넣었을때 str으로 자동으로 변환해줌
        return str(self.key)
    
a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c