import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import UserProfile from './components/UserProfile';
import ProtectedRoute from './components/ProtectedRoute';
import Footer from './components/Footer';

function App() {
	return (
		<Router>
			<div className='flex flex-col min-h-screen'>
				<Routes>
					<Route path='/' element={<LandingPage />} />
					<Route path='/signin' element={<SignIn />} />
					<Route path='/signup' element={<SignUp />} />
					<Route element={<ProtectedRoute />}>
						<Route path='/profile' element={<UserProfile />} />
					</Route>
				</Routes>
				<Footer />
			</div>
		</Router>
	);
}

export default App;
