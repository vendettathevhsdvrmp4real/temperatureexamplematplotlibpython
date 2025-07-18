import matplotlib.pyplot as plt
import random

def generated_tmp(days, temp_day, temp_night, file_name='temp.png'):

        plt.figure(figsize=(8, 6))

        plt.plot(days, temp_day, marker='o', color='r', linestyle='--', label='Температура в днём')
        plt.plot(days, temp_night, marker='o', color='b', linestyle='--', label='Температура в ночью')

        plt.title('График температура через matplotlib ')

        plt.xlabel('Дни неделя')

        plt.ylabel('Значение темп')

        plt.savefig('test.png')
        plt.close()

daytime = [random.randint(20, 30) for b in range(7)]
night = [random.randint(15, 20) for r in daytime]

weeks = ['ПН','ВТ',"СР",'ЧТ','ПТ','СБ','ВС']

generated_tmp(weeks, daytime, night)
