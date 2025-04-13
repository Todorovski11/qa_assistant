import { useState } from 'react';

function App() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setAnswer('Loading...');

    const res = await fetch('http://127.0.0.1:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });

    const data = await res.json();
    setAnswer(data.answer || data.result || 'No answer received.');
  };

  return (
    <div style={{
      padding: '2rem',
      maxWidth: '800px',
      margin: '0 auto',
      fontFamily: 'Segoe UI, sans-serif',
      backgroundColor: '#1e1e1e',
      color: '#fff',
      minHeight: '100vh'
    }}>
      <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>🧠 QA Assistant</h1>
      <form onSubmit={handleSubmit} style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
        <input
          style={{
            flex: 1,
            padding: '0.75rem',
            borderRadius: '8px',
            border: '1px solid #555',
            backgroundColor: '#2b2b2b',
            color: '#fff',
            fontSize: '1rem'
          }}
          type="text"
          placeholder="Ask your question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          style={{
            padding: '0.75rem 1.25rem',
            backgroundColor: '#4caf50',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '1rem'
          }}
          type="submit"
        >
          Ask
        </button>
      </form>

      {answer && (
        <div style={{ marginTop: '2rem' }}>
          <h2 style={{ marginBottom: '0.5rem' }}>📘 Answer:</h2>
          <div style={{
            backgroundColor: '#2a2a2a',
            padding: '1rem',
            borderRadius: '10px',
            whiteSpace: 'pre-wrap',
            lineHeight: '1.5',
            fontSize: '1rem'
          }}>
            {answer}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
