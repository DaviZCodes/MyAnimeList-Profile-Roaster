"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [roast, setRoast] = useState<string>("Fetching roast");

  useEffect(() => {
    const fetchRoast = async () => {
      try {
        console.log("Fetching roast");
        const response = await fetch("http://127.0.0.1:5000/roast");

        if (response.ok) {
          const data = await response.text();

          setRoast(data);
        }
      } catch (error) {
        console.log("Error fetching roast on the frontend", error);
      }
    };

    fetchRoast();
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center p-6 bg-blue-600 text-white">
      <div className="text-3xl mb-3">MyAnimeList.net (MAL) Profile Roaster</div>
      <div className="text-xl">{roast}</div>
    </div>
  );
}
