import { useEffect, useState } from "react";
import { getAccountSummary, getMonthlySummary, getCategorySummary } from "../api/finance";
import SummaryCards from "../components/SummaryCards";
import ChartByMonth from "../components/ChartByMonth";
import ChartByCategory from "../components/ChartByCategory";

export default function Dashboard() {
  const accountId = 1; // or let the user pick

  const [summary, setSummary] = useState(null);
  const [monthly, setMonthly] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    getAccountSummary(accountId).then(res => setSummary(res.data));
    getMonthlySummary(accountId).then(res => setMonthly(res.data.monthly));
    getCategorySummary(accountId).then(res => setCategories(res.data.categories));
  }, []);

  return (
    <div>
      {summary && <SummaryCards data={summary} />}
      <ChartByMonth data={monthly} />
      <ChartByCategory data={categories} />
    </div>
  );
}
