from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import re
from calculator.controller import CalculatorController
#from cabbage.controller import

app = Flask(__name__)

@app.route('/move/<path>') # /move/ui_calc 등등의 경로를 자동 세팅
def move(path):
    return render_template('{}.html'.format(path))

@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt', 'NONE') # request : html에서 받는 것 의미
    if stmt == 'NONE':
        print('넘어온 값이 없음')
    else:
        print('넘어온 식: {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자: {}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])

        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            result = n1 / n2

    return jsonify(result = result) # html의 result에 던져주겠다는 뜻

@app.route('/ai_calc', methods =['POST'])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']

    ctrl = CalculatorController(num1, num2, opcode)
    result = ctrl.calc()
    render_params = {}
    render_params['result'] = int(result)
    #print('app.py에 출력된 덧셈 결과: {}'.format(result))
    return render_template('ai_calc.html', **render_params) # ai_calc로 render_params를 던졌다고 보면 됨

@app.route('/cabbage')
def cabbage():
    # avg_temp min_temp     max_temp    rain_fall
    avg_temp = request.form['avg_temp']
    min_temp = request.form['min_temp']
    max_temp = request.form['max_temp']
    rain_fall = request.form['rain_fall']

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()