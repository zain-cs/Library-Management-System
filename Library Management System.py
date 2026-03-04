import re

valid_availability = ['Available', 'Not Available']

def is_valid_book_title(title):
    return bool(title.strip() and re.match(r'^[A-Za-z\s-]+$', title))

def is_valid_book_author(author):
    return bool(author.strip() and re.match(r'^[A-Za-z\s-]+$', author))

def is_valid_author_id(author_id):
    return bool(author_id.strip() and author_id.isdigit()) 

def is_valid_book_availability(status):
    return bool(status.strip() and status in valid_availability)

def is_valid_book_id(book_id):
    return bool(book_id.strip() and book_id.isdigit())

def is_book_id_unique(book_id):
    try:
        with open('library.txt', "r") as file:
            for line in file:
                fields = line.strip().split(", ")
                if len(fields) >= 5 and fields[4] == book_id:
                    return False
        return True
    except FileNotFoundError:
        return True

def add_book():
    title = input("Enter book title (letters, spaces and hyphens only): ")
    if not is_valid_book_title(title):
        print("Invalid title. Error: (Use letters, spaces and hyphens only)")
        return
    
    author = input("Enter Author name (letters, spaces or hyphens only): ")
    if not is_valid_book_author(author):
        print("Invalid name of book Author. Error: (Use letters, spaces or hyphens only)")
        return
    
    author_id = input("Enter Author ID (numeric only): ")
    if not is_valid_author_id(author_id):
        print("Invalid ID. Error: ID should be numeric only")
        return
    
    availability = input(f"Enter availability of book ({', '.join(valid_availability)}): ")  
    if not is_valid_book_availability(availability):
        print("Invalid availability. Please choose from: " + ', '.join(valid_availability))
        return
    
    book_id = input("Enter Book ID (numeric only): ")
    if not is_valid_book_id(book_id):
        print("Invalid Book ID. Error: ID should be numeric only")
        return
    
    if not is_book_id_unique(book_id):
        print("Error: Book ID already exists. Please use a unique ID")
        return
    
    with open('library.txt', "a") as file:
        file.write(f"{title}, {author}, {author_id}, {availability}, {book_id}\n")
        print("Book record added successfully!")

def view_book():
    try:
        with open('library.txt', "r") as file:
            lines = file.readlines()
            if not lines or all(not line.strip() for line in lines):
                print("No records found. Please add some books first")
                return
            
            print("\n" + "="*100)
            print(f"{'Title':<30} {'Author':<25} {'Author ID':<12} {'Availability':<15} {'Book ID':<10}")
            print("="*100)
            
            for line in lines:
                if not line.strip():
                    continue
                try:
                    parts = line.strip().split(", ")
                    if len(parts) != 5:
                        print(f"Skipping invalid line: {line.strip()} (Expected 5 values, got {len(parts)})")
                        continue
                    title, author, author_id, availability, book_id = parts
                    print(f"{title:<30} {author:<25} {author_id:<12} {availability:<15} {book_id:<10}")
                except ValueError as e:
                    print(f"Error processing line: {line.strip()} - {e}")
            print("="*100)
    except FileNotFoundError:
        print("No records found. Please add some books first")

def update_book():
    target_book_id = input("Enter Book ID to update: ")
    updated = False
    
    try:
        with open('library.txt', "r") as file:
            lines = file.readlines()
        
        new_lines = []
        for line in lines:
            parts = line.strip().split(", ")
            if len(parts) != 5:
                new_lines.append(line)
                continue
            
            title, author, author_id, availability, book_id = parts
            
            if book_id == target_book_id:
                print("Book found! Please enter updated details:")
                
                new_title = input("Enter updated title of book: ")
                if not is_valid_book_title(new_title):
                    print("Invalid title. Update cancelled.")
                    return
                
                new_author = input("Enter updated author of book: ")
                if not is_valid_book_author(new_author):
                    print("Invalid author name. Update cancelled.")
                    return
                
                new_author_id = input("Enter updated Author ID: ")
                if not is_valid_author_id(new_author_id):
                    print("Invalid Author ID. Update cancelled.")
                    return
                
                new_availability = input(f"Enter updated availability ({', '.join(valid_availability)}): ")
                if not is_valid_book_availability(new_availability):
                    print("Invalid availability. Update cancelled.")
                    return
                
                new_line = f"{new_title}, {new_author}, {new_author_id}, {new_availability}, {book_id}\n"
                new_lines.append(new_line)
                updated = True
            else:
                new_lines.append(line)
        
        with open('library.txt', "w") as file:
            file.writelines(new_lines)
        
        if updated:
            print("Book record updated successfully!")
        else:
            print("Book ID not found")
    except FileNotFoundError:
        print("No records found")

def delete_book():
    target_book_id = input("Enter Book ID to delete: ")
    found = False
    
    try:
        with open('library.txt', "r") as file:
            lines = file.readlines()
        
        new_lines = []
        for line in lines:
            parts = line.strip().split(", ")
            if len(parts) == 5 and parts[4] == target_book_id:
                found = True
                # Don't append this line (delete it)
            else:
                new_lines.append(line)
        
        if found:
            with open('library.txt', "w") as file:
                file.writelines(new_lines)
            print("Book record deleted successfully!")
        else:
            print("No book found with this ID")
    except FileNotFoundError:
        print("No records found. Please add some books first")

def main():
    while True:
        print("\n" + "="*40)
        print("    Library Management System")
        print("="*40)
        print("1. Add Book")
        print("2. View Book Records")
        print("3. Update Book Record")
        print("4. Delete Book Record")
        print("5. Exit Program")
        print("="*40)
        
        try:
            ch = int(input("Enter choice (1-5): "))
            
            if ch == 1:
                add_book()
            elif ch == 2:
                view_book()
            elif ch == 3:
                update_book()
            elif ch == 4:
                delete_book()
            elif ch == 5:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main()