import random 
dic = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣'}
while True : 
    roll = input("Roll the dice? (y/n): ").lower()
    if roll == 'y' :
        dic1 = random.randint(1, 6)
        dic2 = random.randint(1, 6)
        print(f'{dic[dic1]}, {dic[dic2]}')
        continue
    elif roll == 'n' :
        print("thanks for playing")
        break
    else :
        print("Invalid input. Please enter 'y' or 'n'.")
        continue

