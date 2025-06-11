type Props = {
  data: {
    total_income: number;
    total_expenses: number;
    net_balance: number;
  };
};

export default function SummaryCards({ data }: Props) {
  return (
    <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
      <div style={{ background: "#d1e7dd", padding: "1rem", borderRadius: "10px" }}>
        <h3>Total Income</h3>
        <p>${data.total_income.toFixed(2)}</p>
      </div>
      <div style={{ background: "#f8d7da", padding: "1rem", borderRadius: "10px" }}>
        <h3>Total Expenses</h3>
        <p>${data.total_expenses.toFixed(2)}</p>
      </div>
      <div style={{ background: "#cff4fc", padding: "1rem", borderRadius: "10px" }}>
        <h3>Net Balance</h3>
        <p>${data.net_balance.toFixed(2)}</p>
      </div>
    </div>
  );
}
