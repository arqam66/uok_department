import { MapPin } from "lucide-react"
import Link from "next/link"
import { ThemeToggle } from "./theme-toggle"

export function Header() {
  return (
    <header className="sticky top-0 z-10 bg-white border-b shadow-sm dark:bg-gray-950 dark:border-gray-800">
      <div className="container flex items-center justify-between h-16 px-4 mx-auto">
        <Link href="/" className="flex items-center space-x-2">
          <MapPin className="w-6 h-6 text-emerald-600" />
          <span className="text-xl font-bold">UoK Map</span>
        </Link>
        <ThemeToggle />
      </div>
    </header>
  )
}
