import { FaLeaf } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="bg-green-700 p-5 flex justify-between items-center">
      <h1 className="text-2xl font-bold text-white flex items-center gap-2">
        <FaLeaf />
        DHARTI AI
      </h1>

      <div className="flex gap-8 text-white">
        <a href="#">Home</a>
        <a href="#">Crop</a>
        <a href="#">Weather</a>
        <a href="#">Market</a>
      </div>
    </nav>
  );
}