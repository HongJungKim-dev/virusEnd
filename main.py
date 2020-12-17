from operator import eq

from ControlVirus import ControlVirus
import random
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
            cv.printMenu()
            a = int(input())
        if a == 1:
            if(i==0):
                cv.shuffle(vaccine)
        elif a == 2:
            if (i == 0):
                cv.shuffle(country)
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

            outOfRange = cv.cure(i, vaccineInput-1, countryInput-1)
            if outOfRange:
                print('감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다 !!')
                cv.printScore(i)
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
            cv.infecteeIncrease(countryInput-1)
        # if not a==3:
        #     a = 0

    if i==loop-1:
        cv.printScore(i)

