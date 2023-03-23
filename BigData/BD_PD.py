#판다스 임포트
import pandas as pd
#1차원 = 시리즈, 2차원 = 데이터프레임

data1 = [1,2,3,4,5]
data2 = ['1반','2반','3반','4반','5반']

#1차원 시리즈로 만들기 / 괄호안에 직접 넣기도 가능 
sr1 = pd.Series(data1)
sr2 = pd.Series(data2)
#데이터 타입 object == String 

#인덱스 명시 변환
sr3 = pd.Series(data1,index=[1000,1001,1002,1003,1004])

#인덱스를 시리즈로 넣기
sr4 = pd.Series(data1, index=data2)
# 반대로도 가능
# 인덱스에 시리지를 넣는것도 가능 -> 인덱스로 들어간 시리즈의 값을 가져오는것도 가능

#슬라이싱 동일하다
#print(sr4[1:4])

#sr4.index / sr4.values => 인덱스와 값 구하기

#sr1 + sr4 => 시리즈간의 연산 가능

data_dic = {
    'yesar': [2019,2019,2020],
    'sales': [350, 480, 200]
}

#2차원의 데이터 프레임 만드는중
df1 = pd.DataFrame(data_dic)
print(df1)

# pd.DataFrame(값, index= [인덱스, 인덱스],columns=data2[0:3])
# 원하는 포맷으로 변경을 자유자재로 가능하다

#head() / tail() => 해당되는거 개수만큼 가져오겠다

#csv 파일로 변경 후 생성
#df1.to_csv('df1.csv')

#csv 파일로 읽기
df3 = pd.read_csv('df1.csv')