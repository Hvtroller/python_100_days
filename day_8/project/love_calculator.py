def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    name = name1 + name2
    for letter in name:
        if letter.lower() in "true":
            true_count += 1
    
    for letter in name:
        if letter.lower() in "love":
            love_count += 1
            
    print(f"{true_count}{love_count}")

calculate_love_score("John Doe", "Jane Doe")
calculate_love_score("John Doe", "Jane Smith")
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Angela Yu", "Jack Bauer")