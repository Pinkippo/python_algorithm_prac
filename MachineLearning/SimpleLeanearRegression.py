import numpy as np # 사용할 라이브러리들을 import
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

class SimpleLinearRegression: # [조건] --> SimpleLinearRegression( ) 클래스 생성
  def __init__(self,learning_rate=0.001):

    self.w=None # 기울기
    self.b=None # 절편 
    x_data = np.array([[]]) # 넘파이 2차 배열 형태로 변환
    y_data = np.array([]) # 넘파이 형태로 변환

    self.lr=learning_rate # 모델의 학습률
    self.losses=[] # 에포크마다 저장할 손실값 변화량 리스트
    self.weight_history=[] # 에포크마다 저장할 기울기 변화량 리스트
    self.bias_history=[] # 에포크마다 저장할 절편 변화량 리스트

  def forward(self,x): # 예측값을 계산하여 리턴하는 메서드
    y_pred=self.w*x+self.b 
    return y_pred 


  def loss(self,x,y): # 예측 값 이용하여 추정 오차(loss) 값 구하기
    y_pred=self.forward(x) #
    return (y_pred-y)**2


  def gradient(self,x,y): # 변화량 구하기
    y_pred=self.forward(x)
    w_grad=2*x*(y_pred-y)
    b_grad=2*(y_pred-y)
    return w_grad,b_grad 


  def predict(self, pnum): # [조건] --> predict 메소드 == 예상 값 구하기
    result= self.w * pnum[0][0] + self.b # 직접 계산
    plt.scatter(x_data, y_data)
    plt.scatter(pnum,result) # 산점도 그래프와 예측선 그래프
    plt.plot(x_data, self.w * x_data + self.b,'r') 
    plt.show()
    return print('예측값 {:.10f}, 기울기: {:.10f}, 절편:{:.10f}'.format(result,self.w, self.b)) 
  

  def score(self, x_data, y_data): # [조건] --> score 메소드 == r2_score을 이용한 점수 추출
    hypothesis = x_data * self.w + self.b 
    return print('평균점수 {:.10f} '.format(r2_score(y_data, hypothesis))) 


  def fit(self,x_data,y_data,epochs=3000): # [조건] --> fit 메소드 == 에포크 지정하여 모델을 학습
    self.w=1.0 # 기울기와 절편 초기화
    self.b=0.0
    x_data = x_data.ravel() # x_data 2차원 배열을 1차원으로 변환

    for epoch in range(epochs): # 에포크 반복
      l=0 # 손실
      w_grad=0 # 경사하강법 기울기의 변화량
      b_grad=0 # 경사하강법 절편의 변화량
      for x,y in zip(x_data,y_data):
        l+=self.loss(x,y) 
        w_i,b_i=self.gradient(x,y) 
        w_grad+=w_i # w값 누적
        b_grad+=b_i # b값 누적

      self.w-=self.lr*(w_grad/len(y_data)) # 가울기 없데이트
      self.b-=self.lr*(b_grad/len(y_data)) # 절편 업데이트
      self.losses.append(l/len(y_data)) # 매 에포크마다 손실 값 기록
      self.weight_history.append(self.w) # 매 에포크마다 기울기 값 기록
      self.bias_history.append(self.b) # 매 에포크마다 절편 값 기록
      print('Epoch ({:10d}/{:10d}) MSE: {:.10f}, 기울기: {:.10f}, 절편:{:.10f}'
      .format(epoch, epochs, l/len(y_data), self.w, self.b))


# [1] 데이터 준비
x_data = np.array([ [1], [2], [3], [4] ]) # 실제 Feature 값 입력 받음
y_data = np.array([ 2, 5, 7, 9 ]) # 실제 Target 값 입력 받음
# [2] 모델 생성
slr=SimpleLinearRegression(learning_rate=0.1)
# [3] 모델 학습
slr.fit(x_data,y_data) 
# [4] 모델 평가
slr.score(x_data, y_data)
# [4] 모델 이용 예측 + 기울기, 절편 확인 + [5] Matplotlib 산점도 그래프와 예측선 그래프
slr.predict([[5]])


# 에포크에 따른 손실값 변화량 리스트
plt.plot(slr.losses)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()


# 에포크에 따른 기울기 변화량 리스트
plt.plot(slr.weight_history)
plt.xlabel('epoch')
plt.ylabel('weight')
plt.show()

# 에포크에 따른 절편 변화량 리스트
plt.plot(slr.bias_history)
plt.xlabel('epoch')
plt.ylabel('bias')
plt.show()