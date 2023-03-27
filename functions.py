#problem 1 
price=float(input("Price: "))
a=input("Are you prime member? " )
def cdp(price, a):
    if (a=="yes" or a=="Yes" or a=="YES"):
        discount_1 = 0.15*price
        p_a_d1= price-discount_1
        discount_2= 0.08*p_a_d1
        price_after_discount_2=p_a_d1-discount_2
        return price_after_discount_2
    else:
        black_friday_discount=0.08*price
        friday_price= price-black_friday_discount
        return friday_price
print("Your final price after calculating all discount is",cdp(price,a))


# problem 2.1
def length(message):
    words = message.split()
    if len(words) <= 200:
        return message
    else:
        return ' '.join(words[:200])

message = input("Enter the message:\n")
message_length = length(message)
print(message_length) 

# problem 2.2
def check_word(message):
    words =  len(message.split())
    if words > 30:
        return False
    else:
        return True

message = input("Enter the message:\n")

if check_word(message):
    print("message meets words limit.\n")
else:
    print("message exceed word limit.\n")