import { Campus } from "@/components/campus"
import { Footer } from "@/components/footer"
import { Header } from "@/components/header"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-1">
        <Campus />
      </main>
      <Footer />
    </div>
  )
}
