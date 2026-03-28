import React, { useState } from "react";
import axios from "axios";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid
} from "recharts";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "https://financial-health-analysis.onrender.com/analyze",
      formData
    );

    setResult(response.data);
  };

  const downloadReport = async () => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    "https://financial-health-analysis.onrender.com/generate-report",
    formData,
    { responseType: "blob" }
  );

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", "financial_report.pdf");
  document.body.appendChild(link);
  link.click();
};


  const chartData = result
    ? Object.keys(result.summary).map((key) => ({
        name: key,
        value: result.summary[key],
      }))
    : [];

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>SME Financial Health Analyzer</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Analyze</button>

      <button onClick={downloadReport} style={{ marginLeft: "10px" }}>
  Download Report
</button>

      {result && (
        <>
          <h2>Financial Metrics Dashboard</h2>
          <BarChart width={800} height={400} data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" />
          </BarChart>

          <h2>Financial Health Insights</h2>

<div style={{
  display: "flex",
  gap: "30px",
  marginTop: "20px",
  flexWrap: "wrap"
}}>

  <div style={{
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "20px",
    width: "300px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  }}>
    <h3>Credit Score</h3>
    <h1 style={{ color: "#2e7d32" }}>
      {result.risk_analysis.credit_score}
    </h1>
    <p>{result.risk_analysis.credit_status}</p>
  </div>

  <div style={{
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "20px",
    width: "300px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  }}>
    <h3 style={{ color: "red" }}>Risks</h3>
    <ul>
      {result.risk_analysis.risks.map((risk, index) => (
        <li key={index}>{risk}</li>
      ))}
    </ul>
  </div>

  <div style={{
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "20px",
    width: "300px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  }}>
    <h3 style={{ color: "green" }}>Recommendations</h3>
    <ul>
      {result.risk_analysis.recommendations.map((rec, index) => (
        <li key={index}>{rec}</li>
      ))}
    </ul>
  </div>

</div>


        </>
      )}
    </div>
  );
}

export default App;
