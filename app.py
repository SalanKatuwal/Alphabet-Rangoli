def Rangoli(size,chars):
    for i in range(size):
        if i==0:
            print((2*size-2*1)*"-"+ chars[size-1] + (2*size-2*1)*"-")
        else:
            print((2*size-2*(i+1))*"-"+ "-".join(chars[(size-1):(size-(i+1)):-1]) +"-"+chars[size-(i+1)]+"-" + "-".join(chars[(size-i):(size)]) + (2*size-2*(i+1))*"-")
    for i in range(size-2,-1,-1):
        if i==0:
            print((2*size-2*1)*"-"+ chars[size-1] + (2*size-2*1)*"-")
        else:
            print((2*size-2*(i+1))*"-"+ "-".join(chars[(size-1):(size-(i+1)):-1]) +"-"+chars[size-(i+1)]+"-" + "-".join(chars[(size-i):(size)]) + (2*size-2*(i+1))*"-")

chars_lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chars_upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
try:
    size=int(input("Enter the size of Rangoli you want: (Note: Values must be between 1 and 26)\n"))
    if size < 1 or size > 26:
        raise ValueError("Please enter the value between 1 and 26")
    
    user_choice=input("Do you want Rangoli in upper case or lower case? (Enter L or U below): \n").strip().lower()
    if user_choice not in ['u','l']:
        raise ValueError("Invalid choice! Enter 'U' for uppercase or 'L' for lowercase.")
    if user_choice == "l":
        Rangoli(size,chars_lower)
    else:
        Rangoli(size,chars_upper)
except ValueError as e:
    print(f"Error {e}")