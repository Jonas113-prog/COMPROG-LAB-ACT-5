def classify_age(age):
    if age < 0:
        print("Invalid age! Age cannot be negative.")
    if age <= 13:
        print("You are a Child.")
    if age <= 18:
        print("You are a Teen.")    
    if age <= 60:
        print("You are an Adult.")
    else:
        print("You are a Senior.")
        
classify_age(12)
classify_age(17)
classify_age(59)
classify_age(70)