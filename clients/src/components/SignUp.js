import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function SignUp() {
	const [formData, setFormData] = useState({
		username: '',
		email: '',
		password: '',
		password2: '',
		first_name: '',
		last_name: '',
	});
	const [error, setError] = useState('');
	const navigate = useNavigate();

	const handleChange = (e) => {
		setFormData({ ...formData, [e.target.name]: e.target.value });
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		setError('');
		try {
			const response = await axios.post(
				'http://localhost:8000/api/auth/signup/',
				formData
			);

			localStorage.setItem('accessToken', response.data.access);
			localStorage.setItem('refreshToken', response.data.refresh);

			navigate('/profile');
		} catch (err) {
			setError(
				err.response?.data?.message || 'An error occurred during sign up.'
			);
			console.error('Sign up error', err.response?.data || err.message);
		}
	};

	return (
		<div className='min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8'>
			<div className='sm:mx-auto sm:w-full sm:max-w-md'>
				<h2 className='mt-6 text-center text-3xl font-extrabold text-gray-900'>
					Create your account
				</h2>
			</div>

			<div className='mt-8 sm:mx-auto sm:w-full sm:max-w-md'>
				<div className='bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10'>
					<form className='space-y-6' onSubmit={handleSubmit}>
						{error && (
							<div
								className='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative'
								role='alert'>
								<span className='block sm:inline'>{error}</span>
							</div>
						)}
						<div>
							<label
								htmlFor='username'
								className='block text-sm font-medium text-gray-700'>
								Username
							</label>
							<div className='mt-1'>
								<input
									id='username'
									name='username'
									type='text'
									required
									value={formData.username}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<label
								htmlFor='email'
								className='block text-sm font-medium text-gray-700'>
								Email address
							</label>
							<div className='mt-1'>
								<input
									id='email'
									name='email'
									type='email'
									autoComplete='email'
									required
									value={formData.email}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<label
								htmlFor='password'
								className='block text-sm font-medium text-gray-700'>
								Password
							</label>
							<div className='mt-1'>
								<input
									id='password'
									name='password'
									type='password'
									autoComplete='new-password'
									required
									value={formData.password}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<label
								htmlFor='password2'
								className='block text-sm font-medium text-gray-700'>
								Confirm Password
							</label>
							<div className='mt-1'>
								<input
									id='password2'
									name='password2'
									type='password'
									autoComplete='new-password'
									required
									value={formData.password2}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<label
								htmlFor='first_name'
								className='block text-sm font-medium text-gray-700'>
								First Name
							</label>
							<div className='mt-1'>
								<input
									id='first_name'
									name='first_name'
									type='text'
									required
									value={formData.first_name}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<label
								htmlFor='last_name'
								className='block text-sm font-medium text-gray-700'>
								Last Name
							</label>
							<div className='mt-1'>
								<input
									id='last_name'
									name='last_name'
									type='text'
									required
									value={formData.last_name}
									onChange={handleChange}
									className='appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
								/>
							</div>
						</div>

						<div>
							<button
								type='submit'
								className='w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'>
								Sign up
							</button>
						</div>
					</form>

					<div className='mt-6'>
						<div className='relative'>
							<div className='absolute inset-0 flex items-center'>
								<div className='w-full border-t border-gray-300' />
							</div>
							<div className='relative flex justify-center text-sm'>
								<span className='px-2 bg-white text-gray-500'>
									Already have an account?
								</span>
							</div>
						</div>
						<div className='mt-6 text-center'>
							<Link
								to='/signin'
								className='font-medium text-indigo-600 hover:text-indigo-500'>
								Sign in
							</Link>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}
