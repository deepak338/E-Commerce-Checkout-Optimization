# E-Commerce Checkout Optimization: A/B Testing & Segment Analysis


## 📌 Project Overview (STAR Method)

### **Situation**
An e-commerce company aimed to reduce cart abandonment by redesigning its checkout page. The Product team launched an A/B test for 14 days with a 50/50 traffic split to evaluate whether the new design (Variant B) could drive a significant increase in conversion rates compared to the current page (Variant A).

### **Task**
As the Data Analyst, my task was to:
1. Validate the statistical significance of the test results using a **Two-Proportion Z-Test**.
2. Analyze conversion rates across different segments (Device Type) to ensure the new design performed consistently.
3. Provide a data-driven recommendation for the full rollout strategy.

### **Action**
* **Data Cleaning & EDA:** Processed 100,000 unique user sessions using Python (`pandas`), handling duplicates and verifying the 50/50 traffic split.
* **Statistical Validation:** Performed a Z-Test with a 95% confidence interval ($\alpha = 0.05$).
* **Segmented Analysis:** Deep-dived into the data using SQL and Python to compare performance across Desktop and Mobile users.
* **Visualization:** Created comparative charts using `Seaborn` and `Matplotlib` to highlight discrepancies between aggregate and segmented data.

### **Result**
* **The "Data Trap":** At the aggregate level, Variant B showed a **statistically significant lift** (11.5% vs. 10.2%, $p=0.003$).
* **Simpson’s Paradox Identified:** Granular analysis revealed that while Desktop saw a 15% lift, **Mobile conversion crashed by 60%**. The high volume of Desktop traffic had mathematically masked the Mobile failure.
* **Strategic Recommendation:** Recommended a **Desktop-only rollout** while halting the Mobile deployment.
* **Business Impact:** Prevented a projected **$320,000 annual revenue loss** by identifying the Mobile UI bug before full deployment.

---

## 📊 Key Visualizations

### 1. The Paradox: Aggregate Success vs. Segment Failure
This chart illustrates how the overall positive trend in Variant B was misleading due to the severe drop in Mobile performance.

![Conversion Rate by Device](![alt text](image.png))  

### 2. Conversion Lift Analysis
| Segment | Variant A (Control) | Variant B (Treatment) | Relative Lift |
| :--- | :--- | :--- | :--- |
| **Overall** | 10.2% | 11.5% | +12.7% |
| **Desktop** | 12.0% | 13.8% | +15.0% |
| **Mobile** | 5.0% | 2.0% | **-60.0%** |

---

## 🛠️ Tech Stack & Tools
* **Data Manipulation:** Python (`pandas`, `numpy`)
* **Statistical Testing:** `scipy.stats`, `statsmodels`
* **Visualization:** `matplotlib`, `seaborn`, Tableau
* **Querying:** SQL (CTEs, Window Functions)

---

## 📁 Repository Structure
* `checkout_ab_test_data.csv`: Raw session data (100k rows).
* `eda_and_testing.ipynb`: Python notebook with EDA, Z-Tests, and Visuals.
* `analysis_queries.sql`: SQL scripts for segmentation and extraction.
* `README.md`: Project summary in STAR format.

---

## 🚀 How to Run the Analysis
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install pandas numpy matplotlib seaborn statsmodels`
3. Run the Jupyter Notebook: `jupyter notebook eda_and_testing.ipynb`
4. Execute `analysis_queries.sql` in your preferred SQL environment.
