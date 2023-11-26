import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="mb-32 grid text-center lg:mb-0 lg:grid-cols-4 lg:text-left">
        <a
          className="text-xl font-mono my-4 cursor-pointer"
          href="https://github.com/kashifulhaque/gpt4-vision-api"
          target="_blank"
          rel="noopener noreferrer"
        >
          <h1 className="text-2xl font-serif underline text-blue-400">
            Docs
          </h1>
        </a>
      </div>
    </main>
  );
}
