
choce1 =input('where do you want to go : ').lower()
if choce1=='left':
  choce2=  input(" you come to a lake this is island type do you wait a bote or swime to across :  ").lower()
  if choce2=='wait':
      choce3=input('this is house where 3 doors 1st is red 2nd is blue 3rd is yellow chose is 1  : ').lower()
      if choce3=='red' :
        print('house full of fire game over.')
      elif choce3=='blue':
        print('house full of fire game over.')
      elif choce3=='yellow':
        print('You win')
  else:
      print('Game over')
else:
    print('you fell in the hole Gane over :')