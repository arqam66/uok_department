
```markdown
# UOK Departments

A modern, responsive web application to display and manage information about Karachi University departments.  
Built with **Next.js**, **TypeScript**, **Tailwind CSS**, and **ShadCN UI components**.

---

## 📌 Features

- **Next.js 13+ App Router** for fast and scalable routing.
- **Tailwind CSS** for responsive and customizable styling.
- **ShadCN UI** components for consistent UI/UX.
- **Reusable components** such as accordions, modals, tables, charts, and more.
- **Light/Dark Theme Toggle** using context providers.
- **Fully responsive design** for mobile, tablet, and desktop.
- **CSV integration** for department data (`work.csv`).
- **TypeScript** for type safety and better developer experience.

---

## 📂 Project Structure

```

```
uok_department/
├── app/                # Next.js App Router pages & layouts
│   ├── globals.css     # Global styles
│   ├── layout.tsx      # Root layout component
│   └── page.tsx        # Home page
│
├── components/         # Reusable UI components
│   ├── ui/             # shadcn/ui components (40+ components)
│   ├── campus.tsx      # Campus component
│   ├── footer.tsx      # Footer component
│   ├── header.tsx      # Header component
│   ├── theme-provider.tsx # Theme management
│   └── theme-toggle.tsx   # Theme switcher
│
├── hooks/              # Custom React hooks
│   ├── use-mobile.tsx  # Mobile detection hook
│   └── use-toast.ts    # Toast notification hook
│
├── lib/                # Utility functions
│   └── utils.ts        # Shared utilities
│
├── public/             # Static assets
│   ├── placeholder-logo.png
│   ├── placeholder-logo.svg
│   ├── placeholder-user.jpg
│   ├── placeholder.jpg
│   └── placeholder.svg
│
├── styles/             # Stylesheets
│   └── globals.css     # Global CSS
│
├── .gitignore          # Git ignore rules
├── components.json     # shadcn/ui configuration
├── karachi_university_departments_gui.py # Python CSV GUI
├── next.config.mjs     # Next.js config
├── package.json        # Project dependencies
├── postcss.config.mjs  # PostCSS config
├── tailwind.config.ts  # Tailwind config
├── tsconfig.json       # TypeScript config
├── work.csv            # Department data
└── README.md           # Project documentation
```
````

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/arqam66/uok_department.git
cd uok_department
````

### 2️⃣ Install dependencies

Using **pnpm**:

```bash
pnpm install
```

Or using **npm**:

```bash
npm install
```

Or using **yarn**:

```bash
yarn install
```

### 3️⃣ Run the development server

```bash
pnpm dev
# or
npm run dev
# or
yarn dev
```

Your app will be running at: **[http://localhost:3000](http://localhost:3000)**

---

## 🛠️ Built With

* [Next.js](https://nextjs.org/)
* [React](https://react.dev/)
* [Tailwind CSS](https://tailwindcss.com/)
* [ShadCN UI](https://ui.shadcn.com/)
* [TypeScript](https://www.typescriptlang.org/)

---

## 📊 Data Source

The department details are stored in `work.csv` and can be easily updated.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Arqam Tahir**
📧 Contact: *\[Your Email Here]*
🔗 GitHub: [@arqam66](https://github.com/arqam66)


