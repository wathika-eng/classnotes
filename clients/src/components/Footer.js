import React from 'react';
import { Link } from 'react-router-dom';
import { Twitter, Github, Facebook, Instagram, Linkedin } from 'lucide-react';

export default function Footer() {
	return (
		<footer className='bg-gray-900 text-gray-300 py-12'>
			<div className='container mx-auto px-4'>
				<div className='grid grid-cols-1 md:grid-cols-4 gap-8'>
					<div>
						<div className='flex items-center space-x-2 mb-4'>
							<div className='w-8 h-8 bg-indigo-600 rounded-full'></div>
							<span className='text-xl font-bold text-white'>UniNotes</span>
						</div>
						<p className='text-sm'>
							Lorem ipsum is placeholder text commonly used in the graphic,
							print, and publishing industries for previewing layouts and visual
							mockups.
						</p>
					</div>
					<div>
						<h3 className='text-lg font-semibold mb-4 text-white'>Products</h3>
						<ul className='space-y-2'>
							<li>
								<Link to='#' className='hover:text-white'>
									Web Studio
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									DynamicBox Flex
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Programming Forms
								</Link>
							</li>
						</ul>
					</div>
					<div>
						<h3 className='text-lg font-semibold mb-4 text-white'>Resources</h3>
						<ul className='space-y-2'>
							<li>
								<Link to='#' className='hover:text-white'>
									Nostrud exercitation
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Visual mockups
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Nostrud exercitation
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Visual mockups
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Nostrud exercitation
								</Link>
							</li>
						</ul>
					</div>
					<div>
						<h3 className='text-lg font-semibold mb-4 text-white'>Company</h3>
						<ul className='space-y-2'>
							<li>
								<Link to='#' className='hover:text-white'>
									Consectetur adipiscing
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Labore et dolore
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Consectetur adipiscing
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Labore et dolore
								</Link>
							</li>
							<li>
								<Link to='#' className='hover:text-white'>
									Consectetur adipiscing
								</Link>
							</li>
						</ul>
					</div>
				</div>
				<div className='mt-8 pt-8 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center'>
					<p className='text-sm'>&copy; Cruip.com. All rights reserved.</p>
					<div className='flex space-x-4 mt-4 md:mt-0'>
						<Link to='#' className='text-gray-400 hover:text-white'>
							<Twitter className='w-5 h-5' />
						</Link>
						<Link to='#' className='text-gray-400 hover:text-white'>
							<Github className='w-5 h-5' />
						</Link>
						<Link to='#' className='text-gray-400 hover:text-white'>
							<Facebook className='w-5 h-5' />
						</Link>
						<Link to='#' className='text-gray-400 hover:text-white'>
							<Instagram className='w-5 h-5' />
						</Link>
						<Link to='#' className='text-gray-400 hover:text-white'>
							<Linkedin className='w-5 h-5' />
						</Link>
					</div>
				</div>
			</div>
		</footer>
	);
}
