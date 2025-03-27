"use client";

import React from "react";
import { SetStateAction, useState } from "react";

export default function Home() {
  const [profile, setProfile] = useState<string>("");
  const [roast, setRoast] = useState<string>("Fetching roast");

  const handleTextInput = (e: {
    target: { value: SetStateAction<string> };
  }) => {
    setProfile(e.target.value);
    // console.log(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!profile) return;

    try {
      console.log("Fetching roast");
      const response = await fetch(`http://127.0.0.1:5000/roast/${profile}`);

      if (response.ok) {
        const data = await response.text();
        console.log("the data is", data);

        setRoast(data);
      }
    } catch (error) {
      console.log("Error fetching roast on the frontend", error);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center p-6 bg-blue-600 text-white">
      <div className="text-3xl mb-3">MyAnimeList.net (MAL) Profile Roaster</div>
      <form onSubmit={handleSubmit}>
        <label className="pr-3">Roast MAL Profile!</label>
        <input
          name="input-profile"
          id="input-profile"
          value={profile}
          type="text"
          className="bg-white text-black px-3 py-2 rounded mr-3"
          alt="input-profile"
          onChange={(e) => handleTextInput(e)}
        ></input>
        <button
          type="submit"
          className="bg-white text-black px-3 py-2 rounded cursor-pointer"
        >
          Submit
        </button>
      </form>
      <div className="text-xl mt-3">{roast}</div>
    </div>
  );
}
