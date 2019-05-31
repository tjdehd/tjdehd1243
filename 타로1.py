import random
from bs4 import BeautifulSoup
import urllib.request
#------------메이저아르카나---------------------------------
major=["FOOL","MAGICIAN","HIGH-PRIESTESS", "EMPRESS", "EMPEROR",
              "POPE","LOVERS","CHARIOT","STRENGTH","HERMIT","WHEEL-OF-FORTUNE",
              "JUSTICE","HANGED MAN","DEATH","TEMPERANCE","DEVIL","TOWER","STAR",
              "MOON","SUN","JUDGEMENT","WORLD"]
htmlmajor=["fool","magician","papess","empress","emperor","pope","lovers","chariot","strength","hermit","wheel_of_fortune",
           "justice","hanged_man","death","temperance","devil","tower","star","moon","sun","judgement","world"]
#-------------앞면 또는 뒷면--------------------------------
updign=["Upright(앞면)","Dignified or Reversed(뒷면)"]
#------------마이너아르카나---------------------------------
miner=["WANDS", "PENTACLES", "SWORDS", "CUPS"]
htmlminer=["wands","pentacles","swords","cups"]
minum=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight" "Queen", "King"]
htmminum=["ace","two","three","four","five","six","seven","eight","nine","ten","page","knight","queen","king"]
#----------------------실행창----------------------------
print("이 프로그램은 타로로 점을 봅니다. 메이저 아르카나와 마이너 아르카나, 그리고 섞은 경우가 포함되어있습니다.")
print(" 첫번째와 두번째는 오늘의 운세이며, 3번째의 경우에는 과거 현재 미래를 알려줍니다. 번외로 4는 메이저ㅡ마이너를 모두 섞은 후 향후 7일간의 점을 봐 줍니다.")
select_card=int(input("1 또는 2,3 을 쳐주세요. 1은 메이저 아르카나, 2은 마이너 아르카나이며 3은 메이저ㅡ마이너를 모두 합친 덱 입니다."))
while True:
    if select_card == 1: #메이저 아르카나일 때    
        a=random.randint(1,len(major))
        b=major[a-1]
        c=random.randint(1,len(updign))
        d=updign[c-1]
        e="http://www.paranormality.com/tarot_"+htmlmajor[a-1]+".shtml"
        print("뽑은 카드는",b,"이며,",d,"입니다. 자세한 정보는",e,"에 있습니다.")
        major_q=str(input("홈페이지로 연결해드릴까요?(Y/N):"))
        if major_q=='Y' or major_q=='y' :
            print("주소연결방법을 찾자.")
        elif major_q=='N' or major_q=='n':
            print("주소연결방법을 찾자.")
    
    
    elif select_card == 2: #마이너 아르카나일 때
        aa=random.randint(1,len(miner))
        aaa=miner[aa-1]
        bb=random.randint(1,len(minum))
        bbb=minum[bb-1]
        cc=random.randint(1,len(updign))
        dd=updign[cc-1]
        deck=[]
        deck.append(bbb+"_of_"+aaa)
        ee="http://www.paranormality.com/tarot_"+htmminum[bb-1]+"_of_"+htmlminer[aa-1]+".shtml"
        print("뽑은 카드는",deck,"이며",dd,"입니다. 자세한 정보는",ee,"에 있습니다.")
        minor_q=str(input("홈페이지로 연결해드릴까요?(Y/N):"))
        if minor_q=='Y' or minor_q=='y' :
            print("주소연결방법을 찾자.")
        elif minor_q=='N' or minor_q=='n':
            print("주소연결방법을 찾자.")
    elif select_card ==3 or select_card ==4 : #두개 다 섞여있을 때
        newarcana=[]
        a_a=random.randint(1,len(miner))
        aa_a=miner[a_a-1]
        b_b=random.randint(1,len(minum))
        bb_b=minum[b_b-1]
        newarcana.append(aa_a)
        newarcana.append(bb_b)
        nm=random.randint(1,len(newarcana))        
        nn=random.randint(1,len(updign))
        print("아직은 아님")    
    newquestion=str(input(" 다른 질문이 있습니까?(Y/N): "))
#-------------------------------다시 질문할 수 있게 하기 -----------
    if(newquestion =='Y' or newquestion =='y'):
        select_card=int(input("1 또는 2,3 을 쳐주세요. 1은 메이저 아르카나, 2은 마이너 아르카나이며 3은 메이저ㅡ마이너를 모두 합친 덱 입니다."))
    elif (newquestion =='N' or newquestion =='n'):
        print(" 타로는 재미를 위해 하는 것 입니다. 좋지 않은 카드가 나왔다고 실망하지 않으셨으면 좋겠습니다.")
        print(" 좋은 하루 되세요.")
        break
