export default function Register() {
  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center">
      <div className="w-[400px] bg-slate-800 p-8 rounded-2xl shadow-xl">
        <h1 className="text-3xl font-bold text-center text-white mb-8">
          Create Account
        </h1>

        <div className="mb-5">
          <label className="block text-gray-300 mb-2">
            Username
          </label>

          <input
            type="text"
            placeholder="Enter username"
            className="w-full p-3 rounded-lg bg-slate-700 text-white outline-none"
          />
        </div>

        <div className="mb-5">
          <label className="block text-gray-300 mb-2">
            Email
          </label>

          <input
            type="email"
            placeholder="Enter email"
            className="w-full p-3 rounded-lg bg-slate-700 text-white outline-none"
          />
        </div>

        <div className="mb-7">
          <label className="block text-gray-300 mb-2">
            Password
          </label>

          <input
            type="password"
            placeholder="Enter password"
            className="w-full p-3 rounded-lg bg-slate-700 text-white outline-none"
          />
        </div>

        <button className="w-full bg-green-600 hover:bg-green-700 p-3 rounded-lg font-semibold">
          Register
        </button>
      </div>
    </div>
  );
}