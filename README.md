# 📚 Library Management System

A simple yet powerful command-line library management system built with Python. This application allows users to efficiently manage book records with full CRUD (Create, Read, Update, Delete) functionality.

## ✨ Features

- **Add Books**: Add new book records with comprehensive validation
- **View Records**: Display all books in a well-formatted table
- **Update Books**: Modify existing book information
- **Delete Books**: Remove books from the system
- **Input Validation**: Robust validation for all user inputs
- **Unique Book IDs**: Automatic checking to prevent duplicate book IDs
- **Persistent Storage**: All data stored in a text file for persistence

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zain-cs/Library-Management-System.git
cd Library-Management-System
```

2. Run the program:
```bash
python library_management.py
```

## 📖 Usage

When you run the program, you'll see a menu with the following options:

```
========================================
    Library Management System
========================================
1. Add Book
2. View Book Records
3. Update Book Record
4. Delete Book Record
5. Exit Program
========================================
```

### Adding a Book

Choose option 1 and provide the following information:
- **Book Title**: Letters, spaces, and hyphens only
- **Author Name**: Letters, spaces, and hyphens only
- **Author ID**: Numeric only
- **Availability**: "Available" or "Not Available"
- **Book ID**: Unique numeric identifier

### Viewing Books

Choose option 2 to display all book records in a formatted table showing:
- Title
- Author
- Author ID
- Availability Status
- Book ID

### Updating a Book

Choose option 3, enter the Book ID, and provide updated information. All fields will be validated before saving.

### Deleting a Book

Choose option 4 and enter the Book ID of the book you want to remove from the system.

## 🔧 Input Validation

The system includes comprehensive validation:

- ✅ Book titles and author names: Only letters, spaces, and hyphens
- ✅ Author ID and Book ID: Numeric values only
- ✅ Availability status: Must be "Available" or "Not Available"
- ✅ Unique Book IDs: System prevents duplicate Book IDs
- ✅ Menu input: Validates numeric choices between 1-5

## 📁 Data Storage

All book records are stored in `library.txt` in the following format:
```
Title, Author, Author ID, Availability, Book ID
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Libraries Used**: 
  - `re` (Regular expressions for input validation)
- **File Handling**: Text file-based storage system
- **Architecture**: Modular function-based design

## 🎯 Code Structure

```
library_management.py
├── is_valid_book_title()      # Validates book titles
├── is_valid_book_author()     # Validates author names
├── is_valid_author_id()       # Validates author IDs
├── is_valid_book_availability() # Validates availability status
├── is_valid_book_id()         # Validates book IDs
├── is_book_id_unique()        # Checks for duplicate IDs
├── add_book()                 # Adds new book records
├── view_book()                # Displays all books
├── update_book()              # Updates existing records
├── delete_book()              # Deletes book records
└── main()                     # Main program loop
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add search functionality
- [ ] Implement book borrowing/return system
- [ ] Add due date tracking
- [ ] Export data to CSV/Excel
- [ ] Add GUI interface
- [ ] Implement database storage (SQLite)
- [ ] Add user authentication
- [ ] Generate reports and statistics

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Zain**
- GitHub: [@zain-cs](https://github.com/zain-cs)

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by the need for simple library management solutions

---

⭐ If you find this project useful, please consider giving it a star!
