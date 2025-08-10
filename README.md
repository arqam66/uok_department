# University of Karachi – Department Portal

A modern, responsive web application for managing and displaying departmental information of the University of Karachi.  
Built with **Next.js**, **Tailwind CSS**, and **TypeScript** for the frontend, plus a **Python GUI tool** for editing data in CSV format.

---

## 📌 Features

- **Fully responsive UI** using Tailwind CSS & shadcn/ui components  
- **Next.js App Router** for modern routing and layouts  
- **TypeScript** for safe, scalable development  
- **Ready-to-use UI components** like accordions, tables, forms, and more  
- **Faculty & department listing** from `work.csv`  
- **Python GUI tool** (`karachi_university_departments_gui.py`) to edit CSV data  
- **Light/Dark theme toggle** support  

---

## 📂 Project Structure

uok_department/
├── app/ # Next.js App Router pages & layouts
│ ├── globals.css # Global styles
│ ├── layout.tsx # Root layout component
│ └── page.tsx # Home page
│
├── components/ # Reusable UI components
│ ├── ui/ # shadcn/ui components
│ │ ├── accordion.tsx
│ │ ├── alert-dialog.tsx
│ │ ├── alert.tsx
│ │ ├── aspect-ratio.tsx
│ │ ├── avatar.tsx
│ │ ├── badge.tsx
│ │ ├── breadcrumb.tsx
│ │ ├── button.tsx
│ │ ├── calendar.tsx
│ │ ├── card.tsx
│ │ ├── carousel.tsx
│ │ ├── chart.tsx
│ │ ├── checkbox.tsx
│ │ ├── collapsible.tsx
│ │ ├── command.tsx
│ │ ├── context-menu.tsx
│ │ ├── dialog.tsx
│ │ ├── drawer.tsx
│ │ ├── dropdown-menu.tsx
│ │ ├── form.tsx
│ │ ├── hover-card.tsx
│ │ ├── input-otp.tsx
│ │ ├── input.tsx
│ │ ├── label.tsx
│ │ ├── menubar.tsx
│ │ ├── navigation-menu.tsx
│ │ ├── pagination.tsx
│ │ ├── popover.tsx
│ │ ├── progress.tsx
│ │ ├── radio-group.tsx
│ │ ├── resizable.tsx
│ │ ├── scroll-area.tsx
│ │ ├── select.tsx
│ │ ├── separator.tsx
│ │ ├── sheet.tsx
│ │ ├── sidebar.tsx
│ │ ├── skeleton.tsx
│ │ ├── slider.tsx
│ │ ├── sonner.tsx
│ │ ├── switch.tsx
│ │ ├── table.tsx
│ │ ├── tabs.tsx
│ │ ├── textarea.tsx
│ │ ├── toast.tsx
│ │ ├── toaster.tsx
│ │ ├── toggle-group.tsx
│ │ ├── toggle.tsx
│ │ ├── tooltip.tsx
│ │ └── ...
│ ├── campus.tsx
│ ├── footer.tsx
│ ├── header.tsx
│ ├── theme-provider.tsx
│ └── theme-toggle.tsx
│
├── hooks/ # Custom React hooks
│ ├── use-mobile.tsx
│ └── use-toast.ts
│
├── lib/ # Utility functions
│ └── utils.ts
│
├── public/ # Static assets
│ ├── placeholder-logo.png
│ ├── placeholder-logo.svg
│ ├── placeholder-user.jpg
│ ├── placeholder.jpg
│ └── placeholder.svg
│
├── styles/ # Stylesheets
│ └── globals.css
│
├── .gitignore # Files ignored by Git
├── components.json # Component configuration
├── karachi_university_departments_gui.py # Python GUI for CSV data
├── next.config.mjs # Next.js configuration
├── package.json # Dependencies & scripts
├── pnpm-lock.yaml # pnpm lockfile
├── postcss.config.mjs # PostCSS configuration
├── tailwind.config.ts # Tailwind configuration
├── tsconfig.json # TypeScript configuration
├── work.csv # CSV data file
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
 API routes for live data fetching

 Department search & filter

 Dark mode refinements

 Authentication for faculty data editing

 Export data directly from GUI to backend

📜 License
This project is licensed under the MIT License.

Made with ❤️ by arqam66

pgsql
Copy
Edit
