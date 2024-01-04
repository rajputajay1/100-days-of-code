
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction =input("Type 'encode' to encrypt , type 'decode to decrypt : ")
# text =input("Type your message : ").lower()
# shift =int(input("Type the shift number : "))



def caesar(start_text,shift_amount,cipher_direction):
     end_text =""
     if cipher_direction == "decode":
          shift_amount = shift_amount * -1
     for letter in start_text:
          if letter in alphabet:
               position =alphabet.index(letter)
               new_postion =position+shift_amount
               end_text +=alphabet[new_postion]
          else:
               end_text+=letter
     print(f"the {cipher_direction}d text is {end_text}")

should_continous =True
while should_continous:
     direction =input("Type 'encode' to encrypt , type 'decode to decrypt : ")
     text =input("Type your message : ").lower()
     shift =int(input("Type the shift number : "))
     shift =shift%25
     caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
     result =  input("type yes do you want again , otherwise no : ")
     if result =="no":
          should_continous =False
          print("Goodbye")



