import { BookOpen, Users, Lightbulb, Trophy, Clock, Star } from 'lucide-react'

export default function WelcomeSection() {
  return (
    <section className="bg-purple-700 text-white">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20 border-t border-purple-600">

          {/* Section header */}
          <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Welcome to UniNotes: Your Path to Academic Success</h2>
            <p className="text-xl text-purple-200">Unlock your full potential with our comprehensive study resources and collaborative learning platform.</p>
          </div>

          {/* Features grid */}
          <div className="max-w-sm mx-auto grid gap-8 md:grid-cols-2 lg:grid-cols-3 lg:gap-16 items-start md:max-w-2xl lg:max-w-none">

            {/* 1st feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <BookOpen className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Extensive Resources</h4>
              <p className="text-center text-purple-200">Access a vast library of study materials, lecture notes, and practice exams to enhance your learning experience.</p>
            </div>

            {/* 2nd feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <Users className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Collaborative Learning</h4>
              <p className="text-center text-purple-200">Connect with fellow students, share insights, and participate in group study sessions to boost your understanding.</p>
            </div>

            {/* 3rd feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <Lightbulb className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Expert Guidance</h4>
              <p className="text-center text-purple-200">Benefit from insights and tips provided by top-performing students and experienced educators in your field.</p>
            </div>

            {/* 4th feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <Trophy className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Track Progress</h4>
              <p className="text-center text-purple-200">Monitor your academic growth with our advanced analytics and performance tracking tools.</p>
            </div>

            {/* 5th feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <Clock className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Time Management</h4>
              <p className="text-center text-purple-200">Optimize your study schedule with our built-in planner and reminder system to stay on top of your coursework.</p>
            </div>

            {/* 6th feature */}
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 mb-4 rounded-full bg-purple-600 flex items-center justify-center">
                <Star className="w-8 h-8 text-purple-100" />
              </div>
              <h4 className="text-xl font-semibold mb-2">Personalized Learning</h4>
              <p className="text-center text-purple-200">Enjoy a tailored learning experience with content recommendations based on your study habits and goals.</p>
            </div>

          </div>

        </div>
      </div>
    </section>
  )
}