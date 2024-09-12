import React from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
	const navigate = useNavigate();

	const handleLogout = () => {
		localStorage.removeItem('accessToken');
		localStorage.removeItem('refreshToken');
		navigate('/signin');
	};

	return (
		<button
			onClick={handleLogout}
			className='bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded'>
			Logout
		</button>
	);
};

export default Logout;
