/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{js,jsx,ts,tsx}'],
	theme: {
		extend: {
			colors: {
				primary: {
					DEFAULT: '#4F46E5',
					foreground: '#FFFFFF',
				},
			},
		},
	},
	plugins: [],
};
