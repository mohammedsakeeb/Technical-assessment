def find_start_index(food, people):
    n = len(food)
    
    for start_index in range(n):
        food_available = 0
        success = True
        
        for i in range(n):
            food_available += food[(start_index + i) % n] - people[(start_index + i) % n]
            
            if food_available < 0:
                success = False
                break
        
        if success:
            return start_index
    
    return -1


food = list(map(int, input("Enter the list of food parcels: ").split()))
people = list(map(int, input("Enter the list of people: ").split()))

result = find_start_index(food, people)

if result != -1:
    print(result)
else:
    print(-1)
