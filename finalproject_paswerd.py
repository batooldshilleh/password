import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num =['0','1','2','3','4','5','6','7','8','9']
sympol =['!','#','$','%','&','(',')','*','+']
print("welcome to the pypassword generator^_^")
nr_letter= int(input("how many letter would you like in your password ?? \n"))
nr_num=int(input("how many namber would you like in your password ?? \n"))
nr_sym=int(input("how many sympol would you like in your password ?? \n"))
#ezey way
#password=" "
#for n in range(1,nr_letter+1):
    #radomle=random.choice(letter)
    #password+=radomle
#for m in range(1,nr_num+1):
 #   radomnu=random.choice(num)
  #  password+=radomnu
#for o in range(1,nr_sym+1):
 #   radomsy=random.choice(sympol)
  #  password+=radomsy
#print(password)
#hard way 
password_list=[]
for n in range(1,nr_letter+1):
    radomle=random.choice(letter)
    password_list+=radomle
for m in range(1,nr_num+1):
     radomnu=random.choice(num)
     password_list+=radomnu
for o in range(1,nr_sym+1):
    radomsy=random.choice(sympol)
    password_list+=radomsy
random.shuffle(password_list)
pas=" "
for q in password_list:
    pas+=q
print(f" you'r password is {pas}")

