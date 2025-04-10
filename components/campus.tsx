"use client"

import { useEffect, useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { MapPin, Search } from "lucide-react"
import { Button } from "@/components/ui/button"

interface Department {
  Department: string
  "Google Maps Link": string
}

export function Campus() {
  const [departments, setDepartments] = useState<Department[]>([])
  const [searchQuery, setSearchQuery] = useState("")
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(
          "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/work-TSqCAceoaWJIguoeT0oLx0ziMYIkpO.csv",
        )
        const text = await response.text()

        // Parse CSV
        const rows = text.split("\n")
        const headers = rows[0].split(",")

        const parsedData = rows
          .slice(1)
          .filter((row) => row.trim() !== "") // Skip empty rows
          .map((row) => {
            // Handle CSV parsing more carefully
            const values = row.split(",")
            const entry: Record<string, string> = {}

            // For Google Maps Link, we need to handle it specially since it might contain commas
            if (values.length >= 2) {
              entry["Department"] = values[0].trim()
              // Join the rest as the Google Maps Link (in case it contains commas)
              entry["Google Maps Link"] = values.slice(1).join(",").trim()

              // Clean up the URL if it has quotes
              if (entry["Google Maps Link"].startsWith('"') && entry["Google Maps Link"].endsWith('"')) {
                entry["Google Maps Link"] = entry["Google Maps Link"].slice(1, -1)
              }
            }

            return entry as Department
          })
          .filter((dep) => dep.Department && dep["Google Maps Link"])

        setDepartments(parsedData)
      } catch (error) {
        console.error("Error fetching data:", error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  const filteredDepartments = departments.filter((dep) =>
    dep.Department.toLowerCase().includes(searchQuery.toLowerCase()),
  )

  const openInGoogleMaps = (url: string) => {
    // Ensure the URL is properly formatted
    let cleanUrl = url

    // Remove any quotes that might be in the URL
    cleanUrl = cleanUrl.replace(/["']/g, "")

    // If it's not a valid URL, try to fix it
    if (!cleanUrl.startsWith("http")) {
      cleanUrl = `https://${cleanUrl}`
    }

    try {
      // Use this approach to ensure the URL opens correctly
      const newWindow = window.open()
      if (newWindow) {
        newWindow.location.href = cleanUrl
      } else {
        // Fallback if popup is blocked
        window.location.href = cleanUrl
      }
    } catch (error) {
      console.error("Error opening URL:", error)
      // Fallback method
      window.open(cleanUrl, "_blank", "noopener,noreferrer")
    }
  }

  return (
    <div className="container px-4 py-8 mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-center mb-2">University of Karachi Campus Map</h1>
        <p className="text-center text-muted-foreground max-w-2xl mx-auto">
          Find your way around the University of Karachi campus. Click on any department to get directions via Google
          Maps.
        </p>
      </div>

      <div className="relative mb-8">
        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground h-4 w-4" />
        <Input
          placeholder="Search for a department..."
          className="pl-10"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>

      <div id="departments" className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading ? (
          <p className="col-span-full text-center py-8">Loading departments...</p>
        ) : filteredDepartments.length > 0 ? (
          filteredDepartments.map((dep, index) => (
            <Card key={index} className="overflow-hidden hover:shadow-md transition-shadow">
              <CardHeader className="pb-2">
                <CardTitle className="text-lg">{dep.Department}</CardTitle>
                <CardDescription>University of Karachi</CardDescription>
              </CardHeader>
              <CardContent>
                <Button
                  variant="outline"
                  className="w-full flex items-center gap-2"
                  onClick={() => openInGoogleMaps(dep["Google Maps Link"])}
                >
                  <MapPin className="h-4 w-4" />
                  <span>Open in Google Maps</span>
                </Button>
              </CardContent>
            </Card>
          ))
        ) : (
          <p className="col-span-full text-center py-8">No departments found matching your search.</p>
        )}
      </div>
    </div>
  )
}
