export default function Sidebar() {
  return (
    <div className="w-64 bg-slate-800 h-screen p-6">
      <h1 className="text-2xl font-bold text-blue-500 mb-10">
        CP Nexus
      </h1>

      <ul className="space-y-5 text-gray-300">
        <li className="hover:text-white cursor-pointer">
          Dashboard
        </li>

        <li className="hover:text-white cursor-pointer">
          Tasks
        </li>

        <li className="hover:text-white cursor-pointer">
          Problems
        </li>

        <li className="hover:text-white cursor-pointer">
          Stats
        </li>

        <li className="hover:text-white cursor-pointer">
          Profile
        </li>
      </ul>
    </div>
  );
}