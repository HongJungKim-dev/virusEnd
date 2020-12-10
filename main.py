# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import random
from operator import eq, itemgetter


def shuffle(name):
    for i in range(len(name)):
        if len(name[0]) == 2:
            print(f'백신 이름 :', name[i][0])
            print(f'백신 치료율 :', str(name[i][1]) + '%')
            print()
        elif len(name[0]) == 3:
            printResult(i, name)


# def shuffle(name, vaccine_in, country_in):
#     for i in range(len(name)):
#         name[country_in][2] *= (1 - (name[i][0] / 100))


def printVaccine(i, vaccine):
    print(f'백신 이름 :', vaccine[i][0])
    print(f'백신 치료율 :', str(vaccine[i][1]) + '%')
    print()


def printResult(i, conutry):
    print(f'감염 국가 :', conutry[i][0])
    print(f'인구수 :', str(conutry[i][1]) + '명')
    print(f'감염 인구수 :', str(conutry[i][2]) + '명')
    print()


def print_menu():
    print(f'-' * 20)
    print(f'    코로나 종식 게임     ')
    print(f'-' * 20)
    print(f'1. 백신정보')
    print(f'2. 감염된 국가정보')
    print(f'3. 게임 시작')
    print(f'4. 게임종료')
    print(f'-' * 20)


def printScore(i, name):
    print(f'-' * 30)
    print(str(i)+'차 백신 투여 후 감염된 나라에 대한 정보')
    print(f'-' * 30)
    name.sort(key=itemgetter(2), reverse=True)
    printResult(name)


def infecteeIncrease(name):
    for i in range(len(name)):
        name[i][2] *= 1.15


def checkFinished(name):
    #for i in range(len(name)):
        if name[i][1] < name[i][2]:
            return True
        else:
            return False


def cure(i,country, vaccine, vaccine_in, country_in):
    print(' ★ '+str(i+1)+'번째 시도 ★\n')
    print('선택된 백신: '+vaccine[vaccine_in][0]+', 치료율: '+str(vaccine[vaccine_in][1]))
    print('선택된 나라: '+country[country_in][0]+'인구수: '+str(country[country_in][1])+
          '감염자수: '+str(country[country_in][2]))
    country[country_in][2] *= (1 - (vaccine[vaccine_in][1] / 100))
    return checkFinished(country)



# def print_vaccine():


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    vaccine = [['백신1', 25], ['백신2', 50], ['백신3', 100]]
    country = [['한국', 1500, 300], ['중국', 3000, 800], ['일본', 2000, 500],
               ['미국', 2500, 750], ['독일', 2200, 1000]]

    for i in range(5):
        print_menu()
        if (i == 0):
            a = int(input())
        if a == 1:
            if(i==0):
                shuffle(vaccine)
        elif a == 2:
            if (i == 0):
                shuffle(country)
        elif a == 3:
            if i == 0:
                print('사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요')
                #vaccine_input, country_input = int(input('사용할 백신(1~3)과 백신을 적용할 국가(1~5)의 번호를 차례대로 입력하세요').split())
                b,c = input().split()
                vaccine_input = int(b)
                country_input = int(c)

                #contry_input = input()
            else:
                vaccine_input = random.randint(1, 3)
                contry_input = random.randint(1, 5)

            #
            #print(vaccine_input, country_input)
            outOfRange = cure(i, country, vaccine, vaccine_input-1, country_input-1)
            if outOfRange:
                break

            for j in range(len(country)):
                if not checkFinished(country):
                    print("="*50)
                    print(str(i+1)+'차 백신 투여 후 감염된 나라에 대한 정보')
                    print("=" * 50)
                    printResult(j, country)
        elif a == 4:
            break



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
