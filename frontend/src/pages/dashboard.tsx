import Sidebar from "../components/sidebar";
import Navbar from "../components/navbar";

export default function Dashboard() {
  return (
    <div className="bg-slate-900 min-h-screen flex">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8">
          <h1 className="text-3xl font-bold mb-8">
            Welcome to CP Nexus
          </h1>

          <div className="grid grid-cols-2 gap-6">

            <div className="bg-slate-800 p-6 rounded-2xl">
              <h2 className="text-xl font-semibold">
                Total Problems
              </h2>

              <p className="text-4xl mt-4 text-blue-500">
                0
              </p>
            </div>

            <div className="bg-slate-800 p-6 rounded-2xl">
              <h2 className="text-xl font-semibold">
                Tasks
              </h2>

              <p className="text-4xl mt-4 text-green-500">
                0
              </p>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
}