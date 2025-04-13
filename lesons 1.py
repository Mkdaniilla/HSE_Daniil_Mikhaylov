a = 1
b = 5.5
print(a)
a = 'привет'
a = 1 # int целые числа
print(id(a))
a = 1 + 2
print(id(a))

b = 5.5 # float числа с плавающей точкой
c = True # bool it 1 правда ложь
d = False # bool it 0
print(a+b+c+d)
name = 'Daniil'
surname = 'Mikhailov'
company = ' ООО "Рога и Капыта" '
print(name + ' ' + surname)
print(company)



company_list=['ООО "Рога и Капыта"',
              'ООО "Креведка"',
              'ООО "Медвед"' ]
company_tuple= ('ООО "Рога и Капыта"',
              'ООО "Креведка"',
              'ООО "Медвед"' )
print('before change', company_list)
company_list[0] = 'ЗАО "Рога и Капыта"'
print('after change', company_list )

print(company_list)
print(company_list[-3])
print(name[0])
company_dict = {'name': 'ООО "Рога и Капыта"',
                'adress': 'Volgograd, arbat,1',
                'inn' : '225456454564',
                'employers' : 20,
                'active' : True}

if company_dict['active']:
    print('Company is active')
else:
    print('company is not active')

#
#company_dict ['name'] = 'ЗАО "Рога и Капыта"'
#print(company_dict)
#company_dict['employers'] -= 5
#company_dict['employers'] += 3
#print(company_dict)

#company_list=[company_dict,
             # company_dict,
              #company_dict]
#print(company_list)
#company_list[0] ['name'] ='ПАО "Рога и Капыта"'
#print(company_list)
#company_set = {'ООО "Рога и Капыта"', 'ООО "Креведка"', 'ООО "Медвед"'}
#company = None

#company_list=['ООО "Рога и Капыта"',
              #'ООО "Креведка"',
              #'ООО "Медвед"' ]
#company_tuple= ('ООО "Рога и Капыта"',
              #'ООО "Креведка"',
              #'ООО "Медвед"' )
statement_1 = True
statement_2 = False
print(statement_1 and statement_2)
print(statement_1 or statement_2)
print(not statement_1)
print( not statement_2)

