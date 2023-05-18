import tkinter as tk
from tkinter import messagebox, ttk

class Library:
    """Represents a library."""

    def __init__(self):
        """Initialize the Library with a collection of books."""
        self.books = {
            "Introduction to AI": {"quantity": 5, "available": 5},
            "Python Programming": {"quantity": 3, "available": 3},
            "Data Science Handbook": {"quantity": 4, "available": 4}
        }

    def checkout(self, book_name):
        """Checkout a book from the library."""
        if self.books.get(book_name) and self.books[book_name]["available"] > 0:
            self.books[book_name]["available"] -= 1
            return f"You have successfully checked out {book_name}"
        else:
            return f"Sorry, {book_name} is not available right now."

    def return_book(self, book_name):
        """Return a book to the library."""
        if self.books.get(book_name) is not None and self.books[book_name]["available"] < self.books[book_name]["quantity"]:
            self.books[book_name]["available"] += 1
            return f"You have successfully returned {book_name}"
        else:
            return f"We don't recognize that book or it is already fully available."

    def add_book(self, book_name, quantity=1):
        """Add a book to the library."""
        if self.books.get(book_name) is not None:
            self.books[book_name]["quantity"] += quantity
            self.books[book_name]["available"] += quantity
        else:
            self.books[book_name] = {"quantity": quantity, "available": quantity}
        return f"{quantity} {book_name} has been added to the library."

    def remove_book(self, book_name):
        """Remove a book from the library."""
        if self.books.get(book_name) is not None:
            quantity = self.books[book_name]["quantity"]
            del self.books[book_name]
            return f"{quantity} {book_name} has been removed from the library."
        else:
            return f"We don't recognize that book."

    def display_books(self):
        """Display the books in the library."""
        return '\n'.join([f"{book}: Quantity: {info['quantity']}, Available: {info['available']}" for book, info in self.books.items()])

class LibraryGUI:
    """Represents the graphical user interface for the library."""

    def __init__(self, library):
        """Initialize the LibraryGUI."""
        self.library = library
        self.window = tk.Tk()
        self.window.title("University Library")

        self.frame = ttk.Frame(self.window, padding=20)
        self.frame.pack()

        self.book_actions_frame = ttk.LabelFrame(self.frame, text="Book Actions")
        self.book_actions_frame.pack(padx=10, pady=10)

        self.checkout_entry = ttk.Combobox(self.book_actions_frame, values=list(library.books.keys()))
        self.checkout_entry.pack(pady=5)
        self.checkout_button = ttk.Button(self.book_actions_frame, text="Checkout Book", command=self.checkout_book)
        self.checkout_button.pack(pady=5)

        self.return_entry = ttk.Combobox(self.book_actions_frame, values=list(library.books.keys()))
        self.return_entry.pack(pady=5)
        self.return_button = ttk.Button(self.book_actions_frame, text="Return Book", command=self.return_book)
        self.return_button.pack(pady=5)

        self.add_entry = ttk.Entry(self.book_actions_frame)
        self.add_entry = ttk.Entry(self.book_actions_frame)
        self.add_entry.pack(pady=5)
        self.add_button = ttk.Button(self.book_actions_frame, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_entry = ttk.Combobox(self.book_actions_frame, values=list(library.books.keys()))
        self.remove_entry.pack(pady=5)
        self.remove_button = ttk.Button(self.book_actions_frame, text="Remove Book", command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.display_button = ttk.Button(self.frame, text="Display Books", command=self.display_books)
        self.display_button.pack(pady=5)

    def display_books(self):
        """Display a messagebox with the information of books in the library."""
        book_info = self.library.display_books()
        messagebox.showinfo("Books in Library", book_info)

    def checkout_book(self):
        """Perform the checkout process for a selected book."""
        book_name = self.checkout_entry.get()
        if book_name:
            result = self.library.checkout(book_name)
            messagebox.showinfo("Checkout Book", result)
            self.update_comboboxes()

    def return_book(self):
        """Perform the return process for a selected book."""
        book_name = self.return_entry.get()
        if book_name:
            result = self.library.return_book(book_name)
            messagebox.showinfo("Return Book", result)
            self.update_comboboxes()

    def add_book(self):
        """Add a book to the library."""
        book_name = self.add_entry.get()
        if book_name:
            quantity = 1  # Default quantity is 1
            result = self.library.add_book(book_name, quantity)
            messagebox.showinfo("Add Book", result)
            self.update_comboboxes()

    def remove_book(self):
        """Remove a book from the library."""
        book_name = self.remove_entry.get()
        if book_name:
            result = self.library.remove_book(book_name)
            messagebox.showinfo("Remove Book", result)
            self.update_comboboxes()

    def update_comboboxes(self):
        """Update the values of the comboboxes with the current list of books."""
        book_list = list(self.library.books.keys())
        self.checkout_entry['values'] = book_list
        self.return_entry['values'] = book_list
        self.remove_entry['values'] = book_list

    def run(self):
        """Run the GUI application."""
        self.window.mainloop()

def main():
    """Entry point for the application."""
    library = Library()
    gui = LibraryGUI(library)
    gui.run()

if __name__ == "__main__":
    main()
