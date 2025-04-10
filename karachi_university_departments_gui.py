import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import urllib.parse
import csv
from tkinter import filedialog

def generate_google_maps_link(destination):
    base_url = "https://www.google.com/maps/dir/?api=1&origin=University+of+Karachi,+KU+Circular+Rd,+Karachi,+Pakistan&destination="
    query = urllib.parse.quote(destination)
    return base_url + query

def get_karachi_university_departments_locations():
    ku_departments = {
        # Faculty of Arts & Social Sciences
        "Arabic": "Department of Arabic, University of Karachi, Karachi, Pakistan",
        "Bengali": "Department of Bengali, University of Karachi, Karachi, Pakistan",
        "Criminology": "Department of Criminology, University of Karachi, Karachi, Pakistan",
        "Economics": "Department of Economics, University of Karachi, Karachi, Pakistan",
        "English": "Department of English, University of Karachi, Karachi, Pakistan",
        "General History": "Department of General History, University of Karachi, Karachi, Pakistan",
        "International Relations": "Department of International Relations, University of Karachi, Karachi, Pakistan",
        "Islamic History": "Department of Islamic History, University of Karachi, Karachi, Pakistan",
        "Library & Information Science": "Department of Library & Information Science, University of Karachi, Karachi, Pakistan",
        "Mass Communication": "Department of Mass Communication, University of Karachi, Karachi, Pakistan",
        "Persian": "Department of Persian, University of Karachi, Karachi, Pakistan",
        "Philosophy": "Department of Philosophy, University of Karachi, Karachi, Pakistan",
        "Political Science": "Department of Political Science, University of Karachi, Karachi, Pakistan",
        "Psychology": "Department of Psychology, University of Karachi, Karachi, Pakistan",
        "Sindhi": "Department of Sindhi, University of Karachi, Karachi, Pakistan",
        "Sociology": "Department of Sociology, University of Karachi, Karachi, Pakistan",
        "Social Work": "Department of Social Work, University of Karachi, Karachi, Pakistan",
        "Urdu": "Department of Urdu, University of Karachi, Karachi, Pakistan",
        "Visual Studies": "Department of Visual Studies, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Education
        "Education": "Department of Education, University of Karachi, Karachi, Pakistan",
        "Special Education": "Department of Special Education, University of Karachi, Karachi, Pakistan",
        "Teacher Education": "Department of Teacher Education, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Engineering
        "Chemical Engineering": "Department of Chemical Engineering, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Islamic Studies
        "Islamic Learning": "Department of Islamic Learning, University of Karachi, Karachi, Pakistan",
        "Quran Wa Sunnah": "Department of Quran Wa Sunnah, University of Karachi, Karachi, Pakistan",
        "Usul-ud-Din": "Department of Usul-ud-Din, University of Karachi, Karachi, Pakistan",
        "Sirah Chair": "Department of Sirah Chair, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Law
        "School of Law": "School of Law, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Management & Administrative Sciences
        "Karachi University Business School": "Karachi University Business School, University of Karachi, Karachi, Pakistan",
        "Commerce": "Department of Commerce, University of Karachi, Karachi, Pakistan",
        "Public Administration": "Department of Public Administration, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Medicine
        "Affiliated Medical and Dental Colleges": "Karachi Medical & Dental College, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Pharmacy
        "Pharmaceutical Chemistry": "Department of Pharmaceutical Chemistry, University of Karachi, Karachi, Pakistan",
        "Pharmaceutics": "Department of Pharmaceutics, University of Karachi, Karachi, Pakistan",
        "Pharmacognosy": "Department of Pharmacognosy, University of Karachi, Karachi, Pakistan",
        "Pharmacology": "Department of Pharmacology, University of Karachi, Karachi, Pakistan",
        
        # Faculty of Science
        "Agriculture & Agribusiness Management": "Department of Agriculture & Agribusiness Management, University of Karachi, Karachi, Pakistan",
        "Applied Chemistry & Chemical Technology": "Department of Applied Chemistry & Chemical Technology, University of Karachi, Karachi, Pakistan",
        "Applied Physics": "Department of Applied Physics, University of Karachi, Karachi, Pakistan",
        "Biochemistry": "Department of Biochemistry, University of Karachi, Karachi, Pakistan",
        "Biotechnology": "Department of Biotechnology, University of Karachi, Karachi, Pakistan",
        "Botany": "Department of Botany, University of Karachi, Karachi, Pakistan",
        "Chemistry": "Department of Chemistry, University of Karachi, Karachi, Pakistan",
        "Computer Science (UBIT)": "Department of Computer Science (UBIT), University of Karachi, Karachi, Pakistan",
        "Food Science & Technology": "Department of Food Science & Technology, University of Karachi, Karachi, Pakistan",
        "Genetics": "Department of Genetics, University of Karachi, Karachi, Pakistan",
        "Geology": "Department of Geology, University of Karachi, Karachi, Pakistan",
        "Geography": "Department of Geography, University of Karachi, Karachi, Pakistan",
        "Health & Physical Education": "Department of Health & Physical Education, University of Karachi, Karachi, Pakistan",
        "Mathematical Sciences": "Department of Mathematical Sciences, University of Karachi, Karachi, Pakistan",
        "Microbiology": "Department of Microbiology, University of Karachi, Karachi, Pakistan",
        "Petroleum Technology": "Department of Petroleum Technology, University of Karachi, Karachi, Pakistan",
        "Physics": "Department of Physics, University of Karachi, Karachi, Pakistan",
        "Physiology": "Department of Physiology, University of Karachi, Karachi, Pakistan",
        "Statistics": "Department of Statistics, University of Karachi, Karachi, Pakistan",
        "Zoology": "Department of Zoology, University of Karachi, Karachi, Pakistan",
        
        # Additional Locations
        "Library": "Central Library, University of Karachi, Karachi, Pakistan",
        "Administration Block": "Administration Block, University of Karachi, Karachi, Pakistan",
        "Medical Center": "Medical Center, University of Karachi, Karachi, Pakistan"
    }
    
    departments_with_links = {}
    for department, destination in ku_departments.items():
        google_maps_link = generate_google_maps_link(destination)
        departments_with_links[department] = google_maps_link
    
    return departments_with_links

def open_link(url):
    webbrowser.open(url, new=2)

def copy_to_clipboard(tree):
    try:
        selected_item = tree.selection()[0]
        text = '\n'.join(tree.item(selected_item, 'values'))
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")
    except IndexError:
        messagebox.showwarning("Copy Error", "No item selected to copy.")

def export_to_csv(tree):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Department", "Google Maps Link"])
            for item in tree.get_children():
                writer.writerow(tree.item(item, 'values'))
        messagebox.showinfo("Exported", f"Data exported to {file_path}")

def create_gui():
    departments_with_links = get_karachi_university_departments_locations()

    global root
    root = tk.Tk()
    root.title("Karachi University Departments")
    
    tree = ttk.Treeview(root, columns=("Department", "Google Maps Link"), show='headings')
    tree.heading("Department", text="Department")
    tree.heading("Google Maps Link", text="Google Maps Link")
    
    for department, maps_link in departments_with_links.items():
        tree.insert("", "end", values=(department, maps_link))
    
    tree.pack(expand=True, fill='both')

    def on_double_click(event):
        item = tree.selection()[0]
        maps_link = tree.item(item, "values")[1]
        open_link(maps_link)

    tree.bind("<Double-1>", on_double_click)
    
    # Menu Bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # Edit Menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Copy", command=lambda: copy_to_clipboard(tree))
    
    # File Menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Export to CSV", command=lambda: export_to_csv(tree))
    
    # Export Button
    export_button = ttk.Button(root, text="Export to CSV", command=lambda: export_to_csv(tree))
    export_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()