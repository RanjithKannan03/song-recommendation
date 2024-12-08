import React from 'react';
import Loading from './Loading';
import { useFormStatus } from 'react-dom';

const SubmitButton = ({ text }) => {
    const status = useFormStatus();
    return (
        <div className='w-full p-3 text-white text-xl font-light transition-all bg-gradient-to-r from-[#AA15A2] to-[#800CB1] rounded-lg hover:font-normal'>
            {
                status.pending ?
                    <div className='relative w-full'>
                        <span className='opacity-0'>{text}</span>
                        <Loading />
                    </div>
                    :
                    <button id='login-bth' className='w-full'>
                        {text}
                    </button>
            }
        </div>
    )
}

export default SubmitButton