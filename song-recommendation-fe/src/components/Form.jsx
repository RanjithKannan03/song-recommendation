'use client';

import React, { useState } from "react";
import Loading from "./Loading";
import song from "@/actions/song";
import SubmitButton from "./SubmitButton";


const Form = () => {
    const [isLoading, setIsLoading] = useState(false);
    return (
        <form className='flex flex-col w-full gap-4' action={song}>

            <div className="relative items-center w-full px-2 py-1 text-white border border-gray-200 rounded-md font-montserrat 0 focus-within:ring-1 focus-within:ring-black">
                <input
                    type="text"
                    id="floating_outlined_email"
                    name="song"
                    className="peer w-full appearance-none bg-transparent px-2.5 pb-2.5 pt-4 text-sm focus:outline-0 "
                    placeholder=" "
                />
                <label
                    htmlFor="floating_outlined_email"
                    className="absolute start-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 transform bg-black px-2 text-sm text-gray-500 duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 rtl:peer-focus:left-auto rtl:peer-focus:translate-x-1/4  dark:text-gray-400 peer-focus:text-white peer-focus:bg-black"
                >
                    Song Name
                </label>
            </div>



            <SubmitButton text='Submit' />


        </form>
    )
}

export default Form