from matplotlib import pyplot as plt

formula = input("x로 이루어진 함수식을 입력하세요. (예시:3*x**3+2*x)")


x_values = range(-100, 101)
y_values = []

for x in x_values:
    try:
        y_values.append(eval(formula))
    except:
        print("잘못 임력하셨습니다. 올바른 함수식을 입력하세요.")
        break


if len(y_values) == len(x_values):
    plt.plot(x_values, y_values)
    plt.grid()
    plt.savefig('2차함수.png')
    plt.show()
