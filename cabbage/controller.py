from cabbage.model import CabbageModel
import tensorflow as tf
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


