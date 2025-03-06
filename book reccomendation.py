import tkinter as tk
from tkinter import ttk

class BookRecommendationChatbot:
    def __init__(self):
        # Predefined book recommendations categorized by genre
        self.books = {
            "Fiction": [
                "To Kill a Mockingbird by Harper Lee",
                "1984 by George Orwell",
                "The Great Gatsby by F. Scott Fitzgerald",
            ],
            "Non-Fiction": [
                "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
                "Educated by Tara Westover",
                "The Immortal Life of Henrietta Lacks by Rebecca Skloot",
            ],
            "Fantasy": [
                "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                "The Hobbit by J.R.R. Tolkien",
                "Mistborn by Brandon Sanderson",
            ],
            "Mystery": [
                "Gone Girl by Gillian Flynn",
                "The Girl with the Dragon Tattoo by Stieg Larsson",
                "Big Little Lies by Liane Moriarty",
            ],
            "Science Fiction": [
                "Dune by Frank Herbert",
                "Ender's Game by Orson Scott Card",
                "The Martian by Andy Weir",
            ],
        }

    def get_recommendations(self, genre):
        return self.books.get(genre, ["No recommendations available for this genre."])


def run_tkinter_ui():
    chatbot = BookRecommendationChatbot()

    def show_recommendations():
        genre = genre_combobox.get()
        recommendations = chatbot.get_recommendations(genre)
        recommendations_text.set("\n".join(recommendations))

    def on_enter(e):
        e.widget['background'] = '#d4f1f4'

    def on_leave(e):
        e.widget['background'] = '#75c9c8'

    # Create the main window
    root = tk.Tk()
    root.title("Book Recommendation Chatbot")
    root.geometry("500x400")
    root.configure(bg="#fef9ef")

    # Create a custom style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox", fieldbackground="#f4d35e", background="#f4d35e")

    # Title label
    tk.Label(root, text="Book Recommendation Chatbot", font=("Helvetica", 18, "bold"), bg="#fef9ef", fg="#457b9d").pack(pady=10)

    # Genre selection
    tk.Label(root, text="Select a Genre:", font=("Helvetica", 12), bg="#fef9ef", fg="#1d3557").pack(pady=5)
    genre_combobox = ttk.Combobox(root, values=list(chatbot.books.keys()), state="readonly")
    genre_combobox.pack(pady=5)
    genre_combobox.set("Select a genre")

    # Button to get recommendations
    get_recommendations_button = tk.Button(root, text="Get Recommendations", command=show_recommendations,
                                           font=("Helvetica", 12), bg="#75c9c8", fg="#ffffff", relief="raised", bd=3)
    get_recommendations_button.pack(pady=10)
    get_recommendations_button.bind("<Enter>", on_enter)
    get_recommendations_button.bind("<Leave>", on_leave)

    # Display recommendations
    recommendations_text = tk.StringVar()
    tk.Label(root, textvariable=recommendations_text, wraplength=400, justify="left", font=("Helvetica", 10),
             bg="#fef9ef", fg="#1d3557").pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    run_tkinter_ui()
