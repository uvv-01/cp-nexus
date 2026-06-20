import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../services/auth";

export default function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleLogin() {
    try {
      const data = await loginUser(
        email,
        password
      );

      localStorage.setItem(
        "token",
        data.access_token
      );

      alert("Login successful!");

      navigate("/");
    }

    catch (error) {
      alert("Invalid credentials");
    }
  }

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center">
      <div className="w-[400px] bg-slate-800 p-8 rounded-2xl shadow-xl">

        <h1 className="text-3xl font-bold text-center mb-8">
          CP Nexus
        </h1>

        <div className="mb-5">
          <label>Email</label>

          <input
            type="email"
            className="w-full p-3 rounded-lg bg-slate-700 mt-2"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
          />
        </div>

        <div className="mb-7">
          <label>Password</label>

          <input
            type="password"
            className="w-full p-3 rounded-lg bg-slate-700 mt-2"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
          />
        </div>

        <button
          onClick={handleLogin}
          className="w-full bg-blue-600 p-3 rounded-lg"
        >
          Sign In
        </button>

      </div>
    </div>
  );
}