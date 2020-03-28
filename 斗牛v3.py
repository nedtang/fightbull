import random

#用我玩的玩法来写，没有大小鬼，有jqk当10，黑桃最大，方片最小。先不加入五小牛和五花牛，葫芦等玩法。
#要计算价值用复杂一点的计数法例如黑桃K为134，方片A为011
#先用random.sample来发牌1-5张为庄家不差开，下一步再模拟现实发牌，再模拟现实洗牌
#庄家和边家全程比大小没有打平，没有无10以上牌边家直接输
#牛七 八两倍，牛九3倍，炸弹4倍
#一副牌只玩一局
class bullfighting():

    def __init__(self):

        poker={}
            
        for i in range(1,53):
            #52张牌，前面是数字后面是花色0为方片，3为黑桃好比大小 直接将花色和数值结合方便牛一样大的时候比大小
            poker[i]=[((i-1)%13)+1,int((i-1)/13)+(((i-1)%13)+1)*10]

            if poker[i][0]>=10:

                poker[i][0]=10

                poker[i].append(((i-1)%13)+1)

            else:

                poker[i].append(((i-1)%13)+1)

            if poker[i][1]%10==0:

                if ((i-1)%13)+1==1:

                    poker[i].append("♦A")

                elif ((i-1)%13)+1==11:

                    poker[i].append("♦J")

                elif ((i-1)%13)+1==12:

                    poker[i].append("♦Q")

                elif ((i-1)%13)+1==13:

                    poker[i].append("♦K")

                else:

                    poker[i].append("♦"+str(((i-1)%13)+1))

            elif poker[i][1]%10==1:

                if ((i-1)%13)+1==1:

                    poker[i].append("♣A")

                elif ((i-1)%13)+1==11:

                    poker[i].append("♣J")

                elif ((i-1)%13)+1==12:

                    poker[i].append("♣Q")

                elif ((i-1)%13)+1==13:

                    poker[i].append("♣K")

                else:
                
                    poker[i].append("♣"+str(((i-1)%13)+1))

            elif poker[i][1]%10==2:

                if ((i-1)%13)+1==1:

                    poker[i].append("♥A")

                elif ((i-1)%13)+1==11:

                    poker[i].append("♥J")

                elif ((i-1)%13)+1==12:

                    poker[i].append("♥Q")

                elif ((i-1)%13)+1==13:

                    poker[i].append("♥K")

                else:

                    poker[i].append("♥"+str(((i-1)%13)+1))

            elif poker[i][1]%10==3:

                if ((i-1)%13)+1==1:

                    poker[i].append("♠A")

                elif ((i-1)%13)+1==11:

                    poker[i].append("♠J")

                elif ((i-1)%13)+1==12:

                    poker[i].append("♠Q")

                elif ((i-1)%13)+1==13:

                    poker[i].append("♠K")

                else:
                
                    poker[i].append("♠"+str(((i-1)%13)+1))

            self.poker=poker

    def one_poker(self,n):

        player_cards=[]

        player_card=random.sample(range(1,53),5*n)

        for i in range(n):

            exec("play"+str(i)+"="+"player_card[5*i:5*(i+1)]")

            player_cards.append(eval("play"+str(i)))
            
        return player_cards

    def the_bull(self,num):

        max_card=[]
        
        List_card=[]
        
        for i in num:

            max_card.append(self.poker[i][1])
            
            List_card.append(self.poker[i][2])
            
        the_max=max(max_card)
        
#没有办法使用组合来验证，等学习完算法来实现，现在先用祖传代码
#先检验是否是炸弹

        boom=list(set(List_card))

        for n in boom:

            if List_card.count(n)>3:

                player_bull=11

                break
                    
        else:
        
            if (self.poker[num[0]][0]+self.poker[num[1]][0]+self.poker[num[2]][0])%10==0:#012

                player_bull=(self.poker[num[3]][0]+self.poker[num[4]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[0]][0]+self.poker[num[1]][0]+self.poker[num[3]][0])%10==0:#013

                player_bull=(self.poker[num[2]][0]+self.poker[num[4]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[0]][0]+self.poker[num[1]][0]+self.poker[num[4]][0])%10==0:#014

                player_bull=(self.poker[num[2]][0]+self.poker[num[3]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10
      
            elif (self.poker[num[0]][0]+self.poker[num[2]][0]+self.poker[num[3]][0])%10==0:#023

                player_bull=(self.poker[num[1]][0]+self.poker[num[4]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[0]][0]+self.poker[num[2]][0]+self.poker[num[4]][0])%10==0:#024

                player_bull=(self.poker[num[1]][0]+self.poker[num[3]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10
     
            elif (self.poker[num[2]][0]+self.poker[num[1]][0]+self.poker[num[3]][0])%10==0:#123

                player_bull=(self.poker[num[0]][0]+self.poker[num[4]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[2]][0]+self.poker[num[1]][0]+self.poker[num[4]][0])%10==0:#124

                player_bull=(self.poker[num[0]][0]+self.poker[num[3]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[2]][0]+self.poker[num[4]][0]+self.poker[num[3]][0])%10==0:#234

                player_bull=(self.poker[num[0]][0]+self.poker[num[1]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10
                    
            elif (self.poker[num[1]][0]+self.poker[num[4]][0]+self.poker[num[3]][0])%10==0:#134

                player_bull=(self.poker[num[2]][0]+self.poker[num[0]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            elif (self.poker[num[4]][0]+self.poker[num[0]][0]+self.poker[num[3]][0])%10==0:#034

                player_bull=(self.poker[num[2]][0]+self.poker[num[1]][0]-1)%10+1

                if player_bull==0:

                    player_bull=10

            else:

                player_bull=0

        result=[]

        result.append(player_bull)

        result.append(the_max)
        
        return result
#a是玩家1 b是玩家2 c是下注
    def contest(self,a,b,c):

        if a[0]>b[0]:

            if a[0]==7 or a[0]==8:

                return 2*c
            
            elif a[0]==9:

                return 3*c

            elif a[0]==10:

                return 4*c

            elif a[0]==11:

                return 5*c
            
            else:

                return c

        elif a[0]<b[0]:

            if b[0]==7 or b[0]==8:

                return -2*c

            elif b[0]==9:

                return -3*c

            elif b[0]==10:

                return -4*c

            elif b[0]==11:

                return -5*c
            
            else:

                return -c
            
        elif a[0]==b[0]:

            if a[1]>b[1]:
                
                if a[0]==7 or a[0]==8:

                    return 2*c
                
                elif a[0]==9:

                    return 3*c

                elif a[0]==10:

                    return 4*c

                elif a[0]==11:

                    return 5*c
                
                else:

                    return c
                
            elif a[1]<b[1]:

                if b[0]==7 or b[0]==8:

                    return -2*c

                elif b[0]==9:

                    return -3*c

                elif b[0]==10:

                    return -4*c

                elif b[0]==11:

                    return -5*c
                
                else:

                    return -c
                    
if __name__=="__main__":

    b=bullfighting()
    
    end={"play0":0,"play1":0,"play2":0}
##    
    for i in range(1000000):

    
#单局内
        play_card=b.one_poker(3)

        for i in range(len(play_card)):

            exec("play"+str(i)+"=b.the_bull(play_card[i])")

            flower=[]

##            print(eval("play"+str(i)))
            
        end["play0"]+=b.contest(play0,play1,5)

        end["play1"]-=b.contest(play0,play1,5)

        end["play0"]+=b.contest(play0,play2,5)

        end["play2"]-=b.contest(play0,play2,5)

    print(end)
