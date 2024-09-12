import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Logout from './Logout';
const UserProfile = () => {
	const [userInfo, setUserInfo] = useState(null);
	const [error, setError] = useState('');

	useEffect(() => {
		const fetchUserInfo = async () => {
			try {
				const response = await axios.get('http://localhost:8000/api/me', {
					headers: {
						Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
					},
				});
				setUserInfo(response.data);
			} catch (err) {
				setError('Failed to fetch user information');
				console.error('Error fetching user info:', err);
			}
		};

		fetchUserInfo();
	}, []);

	if (error) {
		return <div className='text-red-500'>{error}</div>;
	}

	if (!userInfo) {
		return <div>Loading...</div>;
	}

	return (
		<div className='max-w-md mx-auto mt-10 bg-white shadow-lg rounded-lg overflow-hidden'>
			<div className='text-2xl font-bold text-gray-800 px-6 py-4 bg-gray-100'>
				User Profile
			</div>
			<div className='px-6 py-4'>
				<div className='mb-2'>
					<span className='font-bold'>Username:</span> {userInfo.username}
				</div>
				<div className='mb-2'>
					<span className='font-bold'>Email:</span> {userInfo.email}
				</div>
				<div className='mb-2'>
					<span className='font-bold'>First Name:</span> {userInfo.first_name}
				</div>
				<div className='mb-2'>
					<span className='font-bold'>Last Name:</span> {userInfo.last_name}
				</div>
			</div>
			<div className='px-6 py-4'>
				<Logout />
			</div>
		</div>
	);
};

export default UserProfile;
