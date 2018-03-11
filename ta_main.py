import ta_authorize
import ta_actions

#print('Введите емейл:')
#email = input()
#print('Введите пароль:')
#password = input()

email = 'test.box706@mail.ru'
password = '003Solver'

ta_authorize.authorize(email, password)
ta_actions.actions(email,password)
ta_actions.check_box(state)

