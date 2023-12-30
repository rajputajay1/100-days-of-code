print('Welcome to tip Calculator ')
bill =float(input('What was the tatal bill : $'))
tip =int(input('How much tip like 10 ,12 ,& 15 ?'))
people =int(input('How many people to split the bill ?'))
tip_persent =tip/100
total_tip =bill*tip_persent
total_bil =total_tip+bill
bil_per_person =total_bil/people
final_amount =round(bil_per_person,2)
print(f"Each person pay : ${final_amount}")