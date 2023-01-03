import unittest

#Binary Search Tree


#왼쪽은 더 작고 오른쪽이 더 크다
# = 이진트리

#트리는 노드들의 구성체이다.

class Node: #트리를 노드로 생성

    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

#이진 트리 설정

class BinaryTree:  #이진트리 클래스 설정
    def __init__(self): #self = 이진트리 인스턴스 자신
        self.head = Node(None) # 기본으로는 0으로 설정

        #test purpose lists
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def search(self, item): #item으로 받은 숫자를 검색
        if self.head.val is None: #비었을경우 false 출력
            return False
        else:
            return self.__search_node(self.head, item) # 아닐경우 검색 메소드 실행

    def __search_node(self, cur, item): 
        if cur.val == item: #가장 첫번째 노드랑 같을 경우
            return True
        else:
            if cur.val >= item: #노드보다 작은 경우
                if cur.left is not None: # 좌측 아들 노드가 없지 않을때
                    return self.__search_node(cur.left, item) # 재귀
                else:
                    return False # 찾는값 없음
            else: 
                if cur.right is not None: #더 큰 노드가 있을 경우
                    return self.__search_node(cur.right, item) #재귀
                else:
                    return False # 찾는값이 없다

    def add(self, item): # 노드 추가
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item) #추가2 

    def __add_node(self, cur, item): #탐색 하면서 추가
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)
