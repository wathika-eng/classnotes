import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { User, Pencil, X, Check, LogOut } from 'lucide-react';

export default function UserProfile() {
	const [userInfo, setUserInfo] = useState(null);
	const [error, setError] = useState('');
	const [isEditing, setIsEditing] = useState(false);
	const [editedInfo, setEditedInfo] = useState(null);
	const navigate = useNavigate();

	useEffect(() => {
		fetchUserInfo();
	}, []);

	const fetchUserInfo = async () => {
		try {
			const response = await axios.get(
				'http://localhost:8000/api/auth/profile/',
				{
					headers: {
						Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
					},
				}
			);
			setUserInfo(response.data);
			setEditedInfo(response.data);
		} catch (err) {
			setError('Failed to fetch user information');
			console.error('Error fetching user info:', err);
		}
	};

	const handleLogout = () => {
		localStorage.removeItem('accessToken');
		localStorage.removeItem('refreshToken');
		navigate('/signin');
	};

	const handleEdit = () => {
		setIsEditing(true);
	};

	const handleCancel = () => {
		setIsEditing(false);
		setEditedInfo(userInfo);
	};

	const handleSave = async () => {
		try {
			const response = await axios.put(
				'http://localhost:8000/api/auth/profile/',
				editedInfo,
				{
					headers: {
						Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
					},
				}
			);
			setUserInfo(response.data);
			setIsEditing(false);
		} catch (err) {
			setError('Failed to update user information');
			console.error('Error updating user info:', err);
		}
	};

	const handleChange = (e) => {
		setEditedInfo({ ...editedInfo, [e.target.name]: e.target.value });
	};

	const handleImageUpload = async (e) => {
		const file = e.target.files?.[0];
		if (file) {
			const formData = new FormData();
			formData.append('profile_image', file);
			try {
				const response = await axios.post(
					'http://localhost:8000/api/auth/upload-profile-image/',
					formData,
					{
						headers: {
							Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
							'Content-Type': 'multipart/form-data',
						},
					}
				);
				setUserInfo({
					...userInfo,
					profile_image: response.data.profile_image,
				});
				setEditedInfo({
					...editedInfo,
					profile_image: response.data.profile_image,
				});
			} catch (err) {
				setError('Failed to upload profile image');
				console.error('Error uploading profile image:', err);
			}
		}
	};

	if (error) {
		return <div className='text-red-500 text-center'>{error}</div>;
	}

	if (!userInfo) {
		return <div className='text-center'>Loading...</div>;
	}

	return (
		<div className='min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8'>
			<div className='max-w-3xl mx-auto bg-white shadow-lg rounded-lg overflow-hidden'>
				<div className='bg-indigo-600 px-4 py-5 sm:px-6'>
					<h3 className='text-lg leading-6 font-medium text-white'>
						User Profile
					</h3>
				</div>
				<div className='px-4 py-5 sm:p-6'>
					<div className='flex items-center space-x-6 mb-6'>
						<div className='relative'>
							{userInfo.profile_image ? (
								<img
									className='h-24 w-24 rounded-full object-cover'
									src={userInfo.profile_image}
									alt='Profile'
								/>
							) : (
								<div className='h-24 w-24 rounded-full bg-indigo-100 flex items-center justify-center'>
									<User className='h-12 w-12 text-indigo-600' />
								</div>
							)}
							<label
								htmlFor='profile-image-upload'
								className='absolute bottom-0 right-0 bg-white rounded-full p-1 cursor-pointer'>
								<Pencil className='h-4 w-4 text-indigo-600' />
								<input
									id='profile-image-upload'
									type='file'
									className='hidden'
									accept='image/*'
									onChange={handleImageUpload}
								/>
							</label>
						</div>
						<div>
							<h2 className='text-2xl font-bold text-gray-900'>
								{userInfo.first_name} {userInfo.last_name}
							</h2>
							<p className='text-sm text-gray-500'>{userInfo.email}</p>
						</div>
					</div>
					<div className='space-y-4'>
						{isEditing ? (
							<>
								<div>
									<label
										htmlFor='username'
										className='block text-sm font-medium text-gray-700'>
										Username
									</label>
									<input
										type='text'
										name='username'
										id='username'
										value={editedInfo?.username}
										onChange={handleChange}
										className='mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
									/>
								</div>
								<div>
									<label
										htmlFor='email'
										className='block text-sm font-medium text-gray-700'>
										Email
									</label>
									<input
										type='email'
										name='email'
										id='email'
										value={editedInfo?.email}
										onChange={handleChange}
										className='mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
									/>
								</div>
								<div>
									<label
										htmlFor='first_name'
										className='block text-sm font-medium text-gray-700'>
										First Name
									</label>
									<input
										type='text'
										name='first_name'
										id='first_name'
										value={editedInfo?.first_name}
										onChange={handleChange}
										className='mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
									/>
								</div>
								<div>
									<label
										htmlFor='last_name'
										className='block text-sm font-medium text-gray-700'>
										Last Name
									</label>
									<input
										type='text'
										name='last_name'
										id='last_name'
										value={editedInfo?.last_name}
										onChange={handleChange}
										className='mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
									/>
								</div>
							</>
						) : (
							<>
								<div>
									<span className='text-sm font-medium text-gray-500'>
										Username:
									</span>
									<span className='ml-2 text-sm text-gray-900'>
										{userInfo.username}
									</span>
								</div>
								<div>
									<span className='text-sm font-medium text-gray-500'>
										Email:
									</span>
									<span className='ml-2 text-sm text-gray-900'>
										{userInfo.email}
									</span>
								</div>
								<div>
									<span className='text-sm font-medium text-gray-500'>
										First Name:
									</span>
									<span className='ml-2 text-sm text-gray-900'>
										{userInfo.first_name}
									</span>
								</div>
								<div>
									<span className='text-sm font-medium text-gray-500'>
										Last Name:
									</span>
									<span className='ml-2 text-sm text-gray-900'>
										{userInfo.last_name}
									</span>
								</div>
							</>
						)}
					</div>
				</div>
				<div className='px-4 py-4 sm:px-6 bg-gray-50 flex justify-between items-center'>
					{isEditing ? (
						<>
							<button
								onClick={handleSave}
								className='inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'>
								<Check className='h-4 w-4 mr-2' />
								Save Changes
							</button>
							<button
								onClick={handleCancel}
								className='inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'>
								<X className='h-4 w-4 mr-2' />
								Cancel
							</button>
						</>
					) : (
						<>
							<button
								onClick={handleEdit}
								className='inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'>
								<Pencil className='h-4 w-4 mr-2' />
								Edit Profile
							</button>
							<button
								onClick={handleLogout}
								className='inline-flex items-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500'>
								<LogOut className='h-4 w-4 mr-2' />
								Logout
							</button>
						</>
					)}
				</div>
			</div>
		</div>
	);
}
