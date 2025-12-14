import numpy as np

# Step 1: Define character groups
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits    = list("0123456789")
symbols   = list("!@#$%&*")

# Step 2: Combine into one pool
all_chars = lowercase + uppercase + digits + symbols

# Step 3: Convert to NumPy array
pool = np.array(all_chars)


while True:
    n = int(input("ENTER THE LENGHT OF THE PASSWORD" ))
    if n > 8:
        while True:
            password = "".join(np.random.choice(pool, size = n))
            print(password)

            opinon = input("YOU WANT DIFFERENT PASSWORD (YES/NO): ").lower()
             

            if opinon == "yes":
                print("GENERATING NEW PASSWORD.... \n NEW PASSWORD : ")
                continue

            else:
                break

        break
    else:
        print("LENGTH OF THE PASSWORD SHOULD BE GREATER THAN 8")

print(f"THANK YOU.. \n YOUR FINAL PASSWORD IS {password}")
  