import tensorflow as tf
import numpy as np

# Controller에서는 저장된 모델을 불러와서 사용
class CabbageController:
    def __init__(self, avg_temp, min_temp, max_temp, rain_fall):
        self._avg_temp = avg_temp
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._rain_fall = rain_fall

    def service(self):
        X = tf.placeholder(tf.float32, shape=[None, 4]) # 4개의 열을 가진 빈 공간

        # 내부에 가중치를 주는 건데 공식이 정해져있음
        W = tf.Variable(tf.random_normal([4, 1]), name = 'weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()
        # 세션 공간을 만들어서 이 공간 안에서 실행된다고 보면 됨
        # 저장하는 것은 상대경로
        # 불러오는 것은 절대경로
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, 'cabbage/saved_model/saved.ckpt')
            # 4개의 값이 1개의 행으로 여러 열이 있는 구조(매트릭스 구조)
            data = [[self._avg_temp, self._min_temp, self._max_temp, self._rain_fall], ]
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X, W) + b, {X: arr[0:4]})

        # dict가 Y 값이라 보면됨
        return int(dict[0])
            


