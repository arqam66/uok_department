# University of Karachi – Department Portal

A modern web application for managing and displaying departmental information of the University of Karachi.  
Built with **Next.js**, **Tailwind CSS**, and **TypeScript** for the frontend, with a **Python-based GUI tool** for editing department data stored in CSV.

---

## 📌 Features

- **Responsive UI** powered by Tailwind CSS  
- **Next.js App Router** for fast and efficient navigation  
- **Type-safe development** with TypeScript  
- **Faculty & department listings** with data from `work.csv`  
- **Python GUI tool** to manage CSV data without manual editing  
- **Clean, accessible design** for desktop and mobile

---

## 📂 Project Structure

uok_department/
├── app/ # Next.js App Router pages & layouts
├── components/ # Reusable UI components
├── hooks/ # Custom React hooks
├── lib/ # Utility functions & helpers
├── public/ # Static assets (images, icons)
├── styles/ # Global and Tailwind styles
├── .gitignore # Files ignored by Git
├── components.json # Component configuration
├── karachi_university_departments_gui.py # Python GUI for managing department data
├── next.config.mjs # Next.js configuration
├── package.json # Project metadata & dependencies
├── pnpm-lock.yaml # Lockfile for pnpm package manager
├── postcss.config.mjs # PostCSS configuration for Tailwind
├── tailwind.config.ts # Tailwind CSS configuration
├── tsconfig.json # TypeScript configuration
├── work.csv # CSV data file for faculty/departments
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/arqam66/uok_department.git
cd uok_department
2️⃣ Install Dependencies
Using pnpm (recommended):

bash
Copy
Edit
pnpm install
Or with npm:

bash
Copy
Edit
npm install
3️⃣ Run the Development Server
bash
Copy
Edit
pnpm dev
Then open:
👉 http://localhost:3000 in your browser.

🖥 Running the Python GUI Tool
The Python GUI lets you manage work.csv easily.

Ensure Python 3.x is installed.

Install required libraries (if any).

Run:

bash
Copy
Edit
python karachi_university_departments_gui.py
📋 Scripts
Command	Description
pnpm dev	Start development server
pnpm build	Build for production
pnpm start	Start production server
pnpm lint	Run ESLint to check code style

📌 Roadmap
 Add API routes for live data fetching

 Implement search & filter for departments

 Dark mode support

 Authentication for faculty data editing

 Export data directly from GUI to backend

📜 License
This project is licensed under the MIT License.

Made with ❤️ by arqam66

yaml
Copy
Edit

---

If you want, I can also **add a “📸 Screenshots” section** showing the UI from your `public/` folder so it looks visually appealing on GitHub.  
That would make it stand out a lot more.  

Do you want me to add that section next?
