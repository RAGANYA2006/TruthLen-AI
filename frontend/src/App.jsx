import { useState } from "react";
import {
  ShieldCheck,
  ArrowRight,
  Sparkles,
  Zap,
  Lock,
  Activity,
  ScanSearch,
} from "lucide-react";
import "./App.css";

function App() {
  const [newsText, setNewsText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeNews = async () => {
    if (!newsText.trim()) {
      alert("Please enter some news content.");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: newsText,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Analysis failed");
      }

      setResult(data);
    } catch (error) {
      console.error("Backend Error:", error);
      alert("Cannot connect to the backend. Make sure Flask is running.");
    } finally {
      setLoading(false);
    }
  };

  const trySample = () => {
    setNewsText(
      "The government announced a new technology initiative to improve digital services across the country."
    );
    setResult(null);
  };

  return (
    <div className="app">
      {/* NAVBAR */}
      <nav className="navbar">
        <div className="logo">
          <div className="logo-icon">
            <ShieldCheck size={22} />
          </div>

          <span>
            TruthLens<span className="logo-ai"> AI</span>
          </span>
        </div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#analyzer">Analyzer</a>
          <a href="#how-it-works">How It Works</a>
          <a href="#about">About</a>
        </div>

        <button
          className="nav-button"
          onClick={() =>
            document
              .getElementById("analyzer")
              ?.scrollIntoView({ behavior: "smooth" })
          }
        >
          Try Analyzer <ArrowRight size={16} />
        </button>
      </nav>

      {/* HERO */}
      <main id="home">
        <section className="hero">
          <div className="hero-glow glow-one"></div>
          <div className="hero-glow glow-two"></div>

          <div className="hero-content">
            <div className="badge">
              <span className="pulse-dot"></span>
              AI-POWERED NEWS VERIFICATION
            </div>

            <h1>
              Verify Before
              <br />
              <span>You Share.</span>
            </h1>

            <p>
              TruthLens AI analyzes news content using machine learning
              to help identify potentially misleading information.
            </p>

            <div className="hero-buttons">
              <button
                className="primary-button"
                onClick={() =>
                  document
                    .getElementById("analyzer")
                    ?.scrollIntoView({ behavior: "smooth" })
                }
              >
                Analyze News
                <ArrowRight size={18} />
              </button>

              <button
                className="secondary-button"
                onClick={trySample}
              >
                <Sparkles size={17} />
                Try Sample
              </button>
            </div>

            <div className="trust-row">
              <div>
                <Zap size={16} />
                Fast Analysis
              </div>

              <div>
                <Lock size={16} />
                Private
              </div>

              <div>
                <Activity size={16} />
                ML Powered
              </div>
            </div>
          </div>

          {/* AI VISUAL */}
          <div className="ai-visual">
            <div className="orbit orbit-one"></div>
            <div className="orbit orbit-two"></div>

            <div className="ai-core">
              <div className="core-ring">
                <ScanSearch size={54} />
              </div>

              <span>TRUTH</span>
              <strong>LENS</strong>

              <small>AI CORE</small>
            </div>

            <div className="floating-card card-one">
              <ShieldCheck size={18} />

              <div>
                <span>Credibility</span>
                <strong>94.7%</strong>
              </div>
            </div>

            <div className="floating-card card-two">
              <Activity size={18} />

              <div>
                <span>AI Status</span>
                <strong>{loading ? "Analyzing" : "Ready"}</strong>
              </div>
            </div>
          </div>
        </section>

        {/* STATS */}
        <section className="stats">
          <div>
            <strong>1,248+</strong>
            <span>Articles Analyzed</span>
          </div>

          <div>
            <strong>91.4%</strong>
            <span>Average Confidence</span>
          </div>

          <div>
            <strong>24/7</strong>
            <span>AI Availability</span>
          </div>

          <div>
            <strong>ML</strong>
            <span>Powered Analysis</span>
          </div>
        </section>

        {/* ANALYZER */}
        <section className="analyzer-preview" id="analyzer">
          <div className="section-heading">
            <span>01 — ANALYZE</span>

            <h2>
              Put the news
              <br />
              <span>under the lens.</span>
            </h2>

            <p>
              Paste a headline or article and let our machine learning
              model evaluate its credibility.
            </p>
          </div>

          <div className="analyzer-card">
            <div className="card-top">
              <span>NEWS CONTENT</span>

              <span>{newsText.length} / 5000</span>
            </div>

            <textarea
              placeholder="Paste your news article or headline here..."
              value={newsText}
              onChange={(e) => setNewsText(e.target.value)}
              maxLength={5000}
            />

            <div className="card-bottom">
              <span>
                {loading ? "AI is analyzing..." : "AI analysis ready"}
              </span>

              <button
                onClick={analyzeNews}
                disabled={loading}
              >
                {loading ? "Analyzing..." : "Analyze with AI"}

                <ArrowRight size={17} />
              </button>
            </div>
          </div>

          {/* RESULT */}
          {result && (
            <div className="result-card">
              <div className="result-header">
                <ShieldCheck size={24} />

                <h3>Analysis Result</h3>
              </div>

              <p>
                Prediction:{" "}
                <strong>{result.prediction}</strong>
              </p>

              <p>
                Confidence:{" "}
                <strong>{result.confidence}%</strong>
              </p>

              {result.message && (
                <p>{result.message}</p>
              )}
            </div>
          )}
        </section>

        {/* HOW IT WORKS */}
        <section className="how-section" id="how-it-works">
          <div className="section-heading center">
            <span>02 — HOW IT WORKS</span>

            <h2>
              From headline
              <br />
              <span>to insight.</span>
            </h2>
          </div>

          <div className="steps">
            <div className="step">
              <div className="step-number">01</div>

              <h3>Paste</h3>

              <p>
                Enter the news article or headline you want to verify.
              </p>
            </div>

            <div className="step">
              <div className="step-number">02</div>

              <h3>Analyze</h3>

              <p>
                Our machine learning model processes the content.
              </p>
            </div>

            <div className="step">
              <div className="step-number">03</div>

              <h3>Discover</h3>

              <p>
                Receive a credibility prediction and confidence score.
              </p>
            </div>
          </div>
        </section>
      </main>

      {/* FOOTER */}
      <footer id="about">
        <div className="logo">
          <div className="logo-icon">
            <ShieldCheck size={20} />
          </div>

          TruthLens AI
        </div>

        <span>
          Built with Machine Learning & React
        </span>
      </footer>
    </div>
  );
}

export default App;