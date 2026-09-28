def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combined.count(letter)

    print(f"{true_count}{love_count}")


calculate_love_score
your_name = input("Enter you name! ")
your_love_name = input("Enter you lover name! ")
calculate_love_score(your_name, your_love_name)