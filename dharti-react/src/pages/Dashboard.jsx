import { FaLeaf, FaCloudSun, FaChartLine, FaRobot } from "react-icons/fa";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <div className="max-w-7xl mx-auto p-10">

        <h1 className="text-5xl font-bold">

          🌱 DHARTI AI

        </h1>

        <p className="text-gray-400 mt-3 text-xl">

          AI Powered Climate Smart Agriculture Platform

        </p>

        <div className="grid grid-cols-4 gap-6 mt-12">

          <div className="bg-slate-800 rounded-2xl p-8">

            <FaLeaf size={35} />

            <h2 className="mt-4 text-3xl font-bold">

              22

            </h2>

            <p>Total Crops</p>

          </div>

          <div className="bg-slate-800 rounded-2xl p-8">

            <FaCloudSun size={35} />

            <h2 className="mt-4 text-3xl font-bold">

              31°C

            </h2>

            <p>Weather</p>

          </div>

          <div className="bg-slate-800 rounded-2xl p-8">

            <FaChartLine size={35} />

            <h2 className="mt-4 text-3xl font-bold">

              ₹1.8L

            </h2>

            <p>Expected Profit</p>

          </div>

          <div className="bg-slate-800 rounded-2xl p-8">

            <FaRobot size={35} />

            <h2 className="mt-4 text-3xl font-bold">

              AI

            </h2>

            <p>Assistant</p>

          </div>

        </div>

      </div>

    </div>
  );
}