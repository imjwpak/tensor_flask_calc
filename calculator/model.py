import tensorflow as tf

class CalculatorModel:
    def __init__(self):
        pass

    def create_add_model(self):
        # tf.placeholder 변수 처리 하는 곳. 실수가 기본
        # 변수 2개를 준것이라고 보면 됨
        # placeholder가 변수이다
        w1 = tf.placeholder(tf.float32, name = 'w1')
        w2 = tf.placeholder(tf.float32, name = 'w2')
        # 값을 공급
        feed_dict = {'w1' : 8.0, 'w2' : 2.0} # dummy값으로 초기화 하는 작업으로 보면 됨
        # op_add라는 이름의 모델을 만든 것
        r = tf.add(w1, w2, name='op_add')
        sess = tf.Session()
        # Variable은 tensorflow 내부에서 사용하는 변수
        _ = tf.Variable(initial_value='fake_variable') # _는 임시 변수라고 보면 됨
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver() # 저장 작업을 먼저 해야 저장된 것으로 학습을 하니 우선적으로 수행
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 덧셈결과: {}'.format(result))
        # 1000번을 실행해서 모델이 이게 덧셈이라는 것을 이해하도록 함
        saver.save(sess, './saved_add_model/model', global_step=1000)

    def create_sub_model(self):
        # tf.placeholder 변수 처리 하는 곳. 실수가 기본
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # 값을 공급
        feed_dict = {'w1': 8.0, 'w2': 2.0}  # dummy값으로 초기화 하는 작업으로 보면 됨
        # op_sub라는 이름의 모델을 만든 것
        r = tf.subtract(w1, w2, name='op_sub')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _는 임시 변수라고 보면 됨
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()  # 저장 작업을 먼저 해야 저장된 것으로 학습을 하니 우선적으로 수행
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 뺄셈결과: {}'.format(result))
        saver.save(sess, './saved_sub_model/model', global_step=1000)

    def create_mul_model(self):
        # tf.placeholder 변수 처리 하는 곳. 실수가 기본
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # 값을 공급
        feed_dict = {'w1': 8.0, 'w2': 2.0}  # dummy값으로 초기화 하는 작업으로 보면 됨
        # op_sub라는 이름의 모델을 만든 것
        r = tf.multiply(w1, w2, name='op_mul')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _는 임시 변수라고 보면 됨
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()  # 저장 작업을 먼저 해야 저장된 것으로 학습을 하니 우선적으로 수행
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 곱셈결과: {}'.format(result))
        saver.save(sess, './saved_mul_model/model', global_step=1000)

    def create_div_model(self):
        # tf.placeholder 변수 처리 하는 곳. 실수가 기본
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        # 값을 공급
        feed_dict = {'w1': 8.0, 'w2': 2.0}  # dummy값으로 초기화 하는 작업으로 보면 됨
        # op_sub라는 이름의 모델을 만든 것
        r = tf.divide(w1, w2, name='op_div')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # _는 임시 변수라고 보면 됨
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()  # 저장 작업을 먼저 해야 저장된 것으로 학습을 하니 우선적으로 수행
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        print('TF 나눗셈결과: {}'.format(result))
        saver.save(sess, './saved_div_model/model', global_step=1000)