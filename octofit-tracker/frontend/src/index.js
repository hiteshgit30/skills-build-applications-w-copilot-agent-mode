import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import App from './App';

// Log the codespace backend API base for debugging
console.log('Backend API base:', `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/`);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
