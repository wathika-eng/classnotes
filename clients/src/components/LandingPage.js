import React from 'react';
import { Link } from 'react-router-dom';
import { Book, Users, Lightbulb, Trophy, Clock, Star } from 'lucide-react';

function FeatureCard({ icon: Icon, title, description }) {
	return (
		<div className='bg-indigo-700 p-6 rounded-lg'>
			<div className='flex justify-center mb-4'>
				<Icon className='w-12 h-12' />
			</div>
			<h3 className='text-xl font-semibold mb-2'>{title}</h3>
			<p className='text-indigo-200'>{description}</p>
		</div>
	);
}

export default function LandingPage() {
	return (
		<div className='min-h-screen bg-indigo-600 text-white'>
			<header className='container mx-auto px-4 py-6 flex justify-between items-center'>
				<div className='flex items-center space-x-2'>
					<div className='w-8 h-8 bg-white rounded-full'></div>
					<span className='text-2xl font-bold'>UniNotes</span>
				</div>
				<nav>
					<Link to='/signin' className='mr-4 hover:underline'>
						Sign in
					</Link>
					<Link
						to='/signup'
						className='bg-white text-indigo-600 px-4 py-2 rounded-md hover:bg-opacity-90'>
						Sign up
					</Link>
				</nav>
			</header>

			<main className='container mx-auto px-4 py-16 text-center'>
				<h1 className='text-5xl font-bold mb-6'>
					Welcome to UniNotes: Your Path to Academic Success
				</h1>
				<p className='text-xl mb-12 max-w-2xl mx-auto'>
					Unlock your full potential with our comprehensive study resources and
					collaborative learning platform.
				</p>

				<div className='grid grid-cols-1 md:grid-cols-3 gap-8 mb-16'>
					<FeatureCard
						icon={Book}
						title='Extensive Resources'
						description='Access a vast library of study materials, lecture notes, and practice exams to enhance your learning experience.'
					/>
					<FeatureCard
						icon={Users}
						title='Collaborative Learning'
						description='Connect with fellow students, share insights, and participate in group study sessions to boost your understanding.'
					/>
					<FeatureCard
						icon={Lightbulb}
						title='Expert Guidance'
						description='Benefit from insights and tips provided by top-performing students and experienced educators in your field.'
					/>
					<FeatureCard
						icon={Trophy}
						title='Track Progress'
						description='Monitor your academic growth with our advanced analytics and performance tracking tools.'
					/>
					<FeatureCard
						icon={Clock}
						title='Time Management'
						description='Optimize your study schedule with our built-in planner and reminder system to stay on top of your coursework.'
					/>
					<FeatureCard
						icon={Star}
						title='Personalized Learning'
						description='Enjoy a tailored learning experience with content recommendations based on your study habits and goals.'
					/>
				</div>
			</main>
		</div>
	);
}
