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
            print(f'감염 국가 :', name[i][0])
            print(f'인구수 :', str(name[i][1]) + '명')
            print(f'감염 인구수 :', str(name[i][2]) + '명')
            print()


# def shuffle(name, vaccine_in, country_in):
#     for i in range(len(name)):
#         name[country_in][2] *= (1 - (name[i][0] / 100))


def printVaccine(i, vaccine):
    print(f'백신 이름 :', vaccine[i][0])
    print(f'백신 치료율 :', str(vaccine[i][1]) + '%')
    print()


def printResult(i, country):
    curedNum=0
    for i in range(len(country)):
        if country[i][2]>0:
            print(f'감염 국가 :', country[i][0])
            print(f'인구수 :', str(country[i][1]) + '명')
            print(f'감염 인구수 :', str(int(country[i][2])) + '명')
            print()
        else:
            curedNum=curedNum+1
    return curedNum
    #return isAllCured(country, curedNum)

def isAllCured(country, curedNum):
    if curedNum==len(country):
        return True
    else:
        return False


def printMenu():
    print(f'-' * 20)
    print(f'    코로나 종식 게임     ')
    print(f'-' * 20)
    print(f'1. 백신정보')
    print(f'2. 감염된 국가정보')
    print(f'3. 게임 시작')
    print(f'4. 게임종료')
    print(f'-' * 20)


def printScore(i, country, newInfected, cured, curedCountry):
    curedCountryNum = 0
    print(f'=' * 30)
    print('          최종 결과     ')
    #print(str(i)+'차 백신 투여 후 감염된 나라에 대한 정보')
    print(f'=' * 30)
    print('라운드마다 추가로 감염된 감염자 수: '+str(newInfected))
    print('백신으로 치료된 감염자 수: '+str(cured))
    for i in range(len(country)):
        if country[i][2]==0:
           curedCountryNum=curedCountryNum+1
            # curedCountry+=' '
            # curedCountry+=country[i][0]

    print('백신으로 완치된 국가:'+curedCountry+'('+str(curedCountryNum)+'개)')
    country.sort(key=itemgetter(2), reverse=True)
    printResult(i, country)
    print('게임 종료!')


def infecteeIncrease(country, totalNewInfected, countryInput):
    print("증가\n")
    for i in range(len(country)):
        currentNewInfected = int(country[i][2]*0.15)
        country[countryInput][2] += currentNewInfected
        totalNewInfected += currentNewInfected
        print(str(totalNewInfected)+'\n')


def checkFinished(name):
    #for i in range(len(name)):
        if name[i][1] < name[i][2]:
            return True
        else:
            return False


def cure(loop,country, vaccine, vaccine_in, country_in, infected, cured, curedCountry):
    print(' ★ '+str(loop+1)+'번째 시도 ★\n')
    print('선택된 백신: '+vaccine[vaccine_in][0]+', 치료율: '+str(vaccine[vaccine_in][1])+'.0%')
    print('선택된 나라: '+country[country_in][0]+', 인구수: '+str(country[country_in][1])+
          ', 감염자수: '+str(country[country_in][2]))
    curCured = int(country[country_in][2]*(vaccine[vaccine_in][1] / 100))
    infected -= curCured
    cured += curCured
    country[country_in][2] -= curCured

    for i in range(len(country)):
        if country[i][2] == 0:
            curedCountry += ' '
            curedCountry += country[i][0]
    print("=" * 30)
    if not curedCountry=="":
        print("완치 된 국가:" + curedCountry + '\n')
    print(str(loop + 1) + '차 백신 투여 후 감염된 나라에 대한 정보')
    print("=" * 30)
    curedNum = printResult(i, country)
    if curedNum == len(country):
        return curedNum
    #country[country_in][2] *= (1 - (vaccine[vaccine_in][1] / 100))
    return checkFinished(country)



# def print_vaccine():


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    vaccine = [['백신1', 25], ['백신2', 50], ['백신3', 100]]
    country = [['한국', 1500, 300], ['중국', 3000, 800], ['일본', 2000, 500],
               ['미국', 2500, 750], ['독일', 2200, 1000]]
    newInfected = 0
    cured = 0
    curedCountry = ""
    i=0
    loop = 5
    a = 0
    for i in range(loop):
        if not a==3:
            printMenu()
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
                b,c = input().split()
                vaccineInput = int(b)
                countryInput = int(c)
            else:
                vaccineInput = random.randint(1, 3)
                countryInput = random.randint(1, 5)

            outOfRange = cure(i, country, vaccine, vaccineInput-1, countryInput-1, country[countryInput-1][2], cured,curedCountry)
            if outOfRange:
                print('감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다 !!')
                printScore(i, country, newInfected, cured, curedCountry)
                print('^' * 30 + '\n')
                print(outOfRange)
                break
            if outOfRange==len(country):
                print('^'*30+'\n')
                print(outOfRange)
                break
        elif a == 4:
            print('게임을 종료합니다')
            break
        infecteeIncrease(country, newInfected ,countryInput-1)
        if not a==3:
            a = 0

    if i==loop-1:
        printScore(i, country, newInfected, cured, curedCountry)

