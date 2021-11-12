import random
import string

def password_generator(l):

    generated_password_list = []
    char_list_lc = string.ascii_lowercase
    char_list_uc = string.ascii_uppercase
    char_special = ["!","@","#","$","%","^","&","*"]
    
    x = [] 

    while len(generated_password_list) < l:
        rx = random.randint(0,3)
        if rx in x and len(x) < 4:
            continue
        x.append(rx)
        if rx == 0:
            generated_password_list.append(random.choice(char_special))
        elif rx == 1:
            generated_password_list.append(random.randint(0,9))
        elif rx == 2:
            generated_password_list.append(random.choice(char_list_uc))
        elif rx == 3:
            generated_password_list.append(random.choice(char_list_lc))
    
    generated_password = "".join(map(str,generated_password_list))
    return generated_password

