a = [1,2,1,1,4,5]
print(list(set(a)))

f = open('test.txt', 'r')
body = f.read()
f.close
body = body.replace('java', 'python')

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2 == 1]