import Form from "@/components/Form";
import Image from "next/image";

export default function Home() {
  return (
    <div className="flex items-center justify-center w-full h-full bg-black">
      <div className="flex flex-col items-start gap-10">
        <h1 className="text-4xl font-semibold text-white font-montserrat">
          Music Recommendation System
        </h1>

        <Form />
      </div>
    </div>
  );
}
