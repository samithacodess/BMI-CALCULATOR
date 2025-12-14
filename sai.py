import csv
import tkinter as tk
from tkinter import messagebox

# ------------------ LOAD CSV ------------------
foodlisted = []
foodlist = []

with open('foodp.csv', 'r') as file:
    lines = file.readlines()
    for line in lines:
        fields = line.strip().split(',')
        foodlisted.append(fields)

        food = {
            'products': fields[0],
            'kcal': fields[1],
            'protein': fields[2],
            'fats': fields[3]
        }
        foodlist.append(food)


# ------------------ GLOBAL TOTALS ------------------
kcal = []
protein = []
fats = []


# ------------------ SEARCH FUNCTION ------------------
def search_food():
    term = entry_search.get().lower()
    listbox_search.delete(0, tk.END)

    for food in foodlist:
        if term in food['products'].lower():
            listbox_search.insert(tk.END, food['products'])

    if listbox_search.size() == 0:
        listbox_search.insert(tk.END, "No match found")


# ------------------ ADD INGREDIENT FUNCTION ------------------
def add_ingredient():
    a = entry_ingredient.get().lower()
    grams = entry_grams.get()

    if a == "" or grams == "":
        messagebox.showwarning("Missing Data", "Enter ingredient and grams.")
        return

    try:
        grams = float(grams)
    except:
        messagebox.showerror("Invalid Input", "Grams must be a number")
        return

    found = False

    # your exact logic: loop through foodlisted (1 to 466)
    for i in range(1, len(foodlisted)):
        if foodlisted[i][0].lower() == a:
            found = True

            kc = (float(foodlisted[i][1]) / 100) * grams
            pr = (float(foodlisted[i][2]) / 100) * grams
            ft = (float(foodlisted[i][3]) / 100) * grams

            kcal.append(kc)
            protein.append(pr)
            fats.append(ft)

            listbox_added.insert(
                tk.END,
                f"{a} ({grams}g) → {kc:.2f} kcal, {pr:.2f}g protein, {ft:.2f}g fats"
            )

    if not found:
        messagebox.showerror("Not Found", "Food item not in database")

    update_totals()
    entry_ingredient.delete(0, tk.END)
    entry_grams.delete(0, tk.END)


# ------------------ UPDATE TOTAL LABELS ------------------
def update_totals():
    label_kcal.config(text=f"Total Calories: {sum(kcal):.2f}")
    label_protein.config(text=f"Total Protein: {sum(protein):.2f} g")
    label_fats.config(text=f"Total Fats: {sum(fats):.2f} g")


# ------------------ GUI SETUP ------------------
root = tk.Tk()
root.title("Calorie Counter")
root.geometry("600x600")
root.config(bg="white")

title = tk.Label(root, text="Calorie Counter", font=("Arial", 22, "bold"), bg="white")
title.pack(pady=10)


# SEARCH FRAME
frame_search = tk.Frame(root, bg="white")
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search:", bg="white").grid(row=0, column=0)
entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=1, padx=5)
tk.Button(frame_search, text="Search", command=search_food).grid(row=0, column=2)

listbox_search = tk.Listbox(root, width=50, height=5)
listbox_search.pack()


# INGREDIENT FRAME
frame_add = tk.Frame(root, bg="white")
frame_add.pack(pady=10)

tk.Label(frame_add, text="Ingredient:", bg="white").grid(row=0, column=0)
entry_ingredient = tk.Entry(frame_add, width=25)
entry_ingredient.grid(row=0, column=1)

tk.Label(frame_add, text="Grams:", bg="white").grid(row=1, column=0)
entry_grams = tk.Entry(frame_add, width=25)
entry_grams.grid(row=1, column=1)

tk.Button(root, text="Add Ingredient", command=add_ingredient).pack(pady=10)


# ADDED ITEMS LISTBOX
listbox_added = tk.Listbox(root, width=60, height=10)
listbox_added.pack(pady=10)


# TOTALS
label_kcal = tk.Label(root, text="Total Calories: 0", font=("Arial", 12), bg="white")
label_kcal.pack()

label_protein = tk.Label(root, text="Total Protein: 0 g", font=("Arial", 12), bg="white")
label_protein.pack()

label_fats = tk.Label(root, text="Total Fats: 0 g", font=("Arial", 12), bg="white")
label_fats.pack()


root.mainloop()
