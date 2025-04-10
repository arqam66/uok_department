import Link from "next/link"
import { Github } from "lucide-react"

export function Footer() {
  return (
    <footer className="border-t py-6 bg-white dark:bg-gray-950">
      <div className="container flex flex-col items-center justify-center gap-4 px-4 md:flex-row md:justify-between">
        <p className="text-sm text-muted-foreground">All rights reserved to Arqam Hussain</p>
        <Link
          href="https://github.com/arqam66"
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-2 text-sm text-muted-foreground hover:text-emerald-600 transition-colors"
        >
          <Github className="h-4 w-4" />
          <span>github.com/arqam66</span>
        </Link>
      </div>
    </footer>
  )
}
