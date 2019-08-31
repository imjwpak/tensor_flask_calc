# 모델을 만든다는 것은 그냥 tensorflow를 한다고 보면 된다
import tensorflow as tf
import pandas as pd
import numpy as np

class CabbageModel:
    def __init__(self):
       pass

    def create_model(self):
        model = tf.global_variables_initializer()
        data = pd.read_csv('./data/price_data.csv', sep=',')
        xy = np.array(data, dtype=np.float32)
        x_data = xy[:, 1:-1] # feature
        y_data = xy[:,[-1]] # 가격
        # 대문자는 확률 변수이다
        # a = 3 : 일반적인 변수는 a로 들어갈 값이 딱 정해져있음
        # 확률변수 : A = {1, 2, 3} 1~3 중 하나가 들어가는데 어떤 값이 들어갈지는 모른다는 의미
        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        # 아래 줄은 y = WX + b 와 같다고 보면 됨
        # 미래에 대해 정해지지 않은 값(가설)
        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        # 여기까지가 식을 만든 것이고

        # 이제부터 러닝
        for step in range(100000):
            # 임시 변수
            _cost, _hypo, _ = sess.run([cost, hypothesis, train],
                                       feed_dict = {X: x_data, Y: y_data})
            if step % 500 == 0:
                print('# %d 손실비용 : %d' % (step, _cost))
                print('- 배추가격 : %d' % (_hypo[0]))

        # 러닝이 끝나면 저장
        saver = tf.train.Saver()
        saver.save(sess, 'saved_model/saved.ckpt')
        print('저장완료')



        




