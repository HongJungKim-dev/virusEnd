from operator import eq
from operator import eq, itemgetter
from ControlVirus import ControlVirus
import random

def shuffle(vaccine):
    for i in range(len(vaccine)):
        if len(vaccine[0]) == 2:
            print(f'백신 이름 :', vaccine[i][0])
            print(f'백신 치료율 :', str(vaccine[i][1]) + '%')
            print()
        elif len(vaccine[0]) == 3:
            print(f'감염 국가 :', vaccine[i][0])
            print(f'인구수 :', str(vaccine[i][1]) + '명')
            print(f'감염 인구수 :', str(vaccine[i][2]) + '명')
            print()


def printVaccine(self, i):
    vaccine = self.getVaccine()
    print(f'백신 이름 :', vaccine[i][0])
    print(f'백신 치료율 :', str(vaccine[i][1]) + '%')
    print()


def printResult(self, i):
    country = self.getCountry()
    curedNum = 0
    for i in range(len(country)):
        if country[i][2] > 0:
            print(f'감염 국가 :', country[i][0])
            print(f'인구수 :', str(country[i][1]) + '명')
            print(f'감염 인구수 :', str(int(country[i][2])) + '명')
            print()
        else:
            curedNum = curedNum + 1
    self.coured = curedNum


def printMenu():
    print(f'-' * 20)
    print(f'    코로나 종식 게임     ')
    print(f'-' * 20)
    print(f'1. 백신정보')
    print(f'2. 감염된 국가정보')
    print(f'3. 게임 시작')
    print(f'4. 게임종료')
    print(f'-' * 20)


def printScore(self, i):
    curedCountryStr = ''
    country = self.getCountry()
    cured = self.getCured()
    print(f'=' * 30)
    print('          최종 결과     ')
    print(f'=' * 30)
    print('라운드마다 추가로 감염된 감염자 수: ' + str(self.getIncreasingInfected()))
    print('백신으로 치료된 감염자 수: ' + str(cured))
    for i in range(self.getCompletelyCured()):
        curedCountryStr += ' '
        curedCountryStr += self.curedCountry[i]
    print('백신으로 완치된 국가:' + curedCountryStr
          + '(' + str(self.completelyCured) + '개)')
    country.sort(key=itemgetter(2), reverse=True)
    self.setCountry(country)
    printResult(cv, i)
    print('게임 종료!')


def infecteeIncrease(self, countryInput):
    country = self.getCountry()
    totalNewInfected = self.getIncreasingInfected()
    for i in range(len(country)):
        if not country[countryInput][2] == 0:
            currentNewInfected = int(country[i][2] * 0.15)
            country[countryInput][2] += currentNewInfected
            self.setCountry(country)
            totalNewInfected += currentNewInfected
            self.setIncreasingInfected(totalNewInfected)


def checkFinished(self, i):
    country = self.getCountry()
    if country[i][1] < country[i][2]:
        return True
    else:
        return False


def cure(self, loop, vaccine_in, country_in):
    curedCountry = self.getCuredCountry()
    cured = self.getCured()
    vaccine = self.getVaccine()
    country = self.getCountry()
    infected = country[country_in][2]
    completelyCured = self.getCompletelyCured()
    print(' ★ ' + str(loop + 1) + '번째 시도 ★\n')
    print('선택된 백신: ' + vaccine[vaccine_in][0] + ', 치료율: ' + str(vaccine[vaccine_in][1]) + '.0%')
    print('선택된 나라: ' + country[country_in][0] + ', 인구수: ' + str(country[country_in][1]) +
          ', 감염자수: ' + str(country[country_in][2]))
    if not eq(country[country_in][0], curedCountry[completelyCured - 1]):
        curCured = int(country[country_in][2] * (vaccine[vaccine_in][1] / 100))
        infected -= curCured
        cured += curCured
        self.cured = cured
        country[country_in][2] = infected
        self.country = country
    if country[country_in][2] == 0:
        if not eq(country[country_in][0], curedCountry[completelyCured - 1]):
            print('target')
            print(country[country_in][0])
            print('comp')
            print(curedCountry[completelyCured - 1])
            curedCountry[completelyCured] = country[country_in][0]
            self.setCompletelyCured(completelyCured + 1)
            print("=" * 30)
            print("완치 된 국가:" + curedCountry[completelyCured - 1] + '\n')
            print("=" * 30)
    curedNum = printResult(cv, country_in)
    if curedNum == len(country):
        return curedNum
    return checkFinished(cv, country_in)

if __name__ == '__main__':
    i=0
    a = 0
    loop = 5
    cv = ControlVirus()
    vaccine = cv.getVaccine()
    country = cv.getCountry()
    isTwice = False
    curedCountry = cv.getCuredCountry()
    for i in range(loop):
        if not a==3:
            printMenu()
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
                for indexNum in range(cv.getCompletelyCured()):
                    print('이미 완치된 국가===')
                    print(curedCountry[indexNum])
                    print('비교 국가===')
                    print(country[countryInput-1][0])                 
                    if eq(curedCountry[indexNum],country[countryInput-1][0]):

                        isTwice = True
                        break
                if isTwice == True:
                    print('이미 완치된 국가이므로 다시 선택합니다.')
                    continue

            outOfRange = cure(cv, i, vaccineInput-1, countryInput-1)
            if outOfRange:
                print('감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다 !!')
                printScore(i)
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
        if a==3:
            infecteeIncrease(cv, countryInput-1)
        # if not a==3:
        #     a = 0

    if i==loop-1:
        printScore(cv, i)