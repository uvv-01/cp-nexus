import Sidebar from "../components/sidebar";
import Navbar from "../components/navbar";

export default function Problems() {
  return (
    <div className="bg-slate-900 min-h-screen flex">
      <Sidebar />

      <div className="flex-1">
        <Navbar />

        <div className="p-8">

          <div className="flex justify-between items-center mb-8">
            <h1 className="text-3xl font-bold">
              Problems
            </h1>

            <button className="bg-blue-600 px-5 py-3 rounded-xl">
              + Add Problem
            </button>
          </div>

          <div className="space-y-4">

            <div className="bg-slate-800 p-5 rounded-2xl flex justify-between">
              <div>
                <h2 className="font-semibold">
                  Two Sum
                </h2>

                <p className="text-gray-400">
                  LeetCode • Easy • Array
                </p>
              </div>

              <span className="text-green-500 text-xl">
                ✓
              </span>
            </div>

            <div className="bg-slate-800 p-5 rounded-2xl flex justify-between">
              <div>
                <h2 className="font-semibold">
                  House Robber
                </h2>

                <p className="text-gray-400">
                  LeetCode • Medium • DP
                </p>
              </div>

              <span className="text-yellow-500 text-xl">
                ○
              </span>
            </div>

          </div>

        </div>
      </div>
    </div>
  );
}