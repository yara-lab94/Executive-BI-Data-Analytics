# 📊 Executive BI & Data Analytics Platform
### منصة ذكاء الأعمال والتحليلات التنفيذية المتقدمة

A dynamic, production-ready Business Intelligence (BI) and Data Analytics dashboard built with **Python**, **Streamlit**, **Seaborn**, and **Matplotlib**. This platform features automated dynamic schema handling, allowing users to upload any transactional or operational CSV dataset and instantly extract strategic insights.

منصة ديناميكية متكاملة لذكاء الأعمال وتحليل البيانات، تم تطويرها باستخدام لغة **Python** ومكتبات **Streamlit** و**Seaborn** و**Matplotlib**. تتميز المنصة بقدرتها على التعامل الحركي التام مع مختلف هياكل البيانات (CSV)، مما يتيح استخراج المؤشرات الاستراتيجية فوراً بمجرد رفع الملف.

---

## 🌐 Links & Live Demo / الروابط والتشغيل الحي
* **Live Demo:** [Click here to explore the live dashboard](https://executive-bi-data-analytics-nsz4u9sz24rve9rb3mh9wi.streamlit.app/)
* **Dual-Language Support:** Features a seamless language toggle in the sidebar, instantly adapting the entire system architecture, text alignment (RTL/LTR), and layout configuration.
* **دعم لغوي مزدوج:** تتميز اللوحة بدعم كامل ومزدوج لتبديل لغة الواجهة ديناميكياً من الشريط الجانبي، حيث تتغير محاذاة الهيكل البصري واتجاه النصوص بالكامل (من اليمين لليسار للعربية ومن اليسار لليمين للإنجليزية).

---

## 🚀 How to Test the Live Demo / كيف تجرّب المنصة حية

To experience the dynamic capabilities of this schema-agnostic platform, follow these simple steps:
لتجربة القدرات الديناميكية للمنصة، اتبع الخطوات البسيطة التالية:

1. **Download a Sample Dataset:** Click on any of the sample `.csv` files provided in this repository above (e.g., `perfect_sales_data.csv`, `retail_sales.csv`, or `supermarket_sales.csv`) and download it to your computer.
   (**تحميل ملف تجريبي:** اضغط على أي من ملفات البيانات التجريبية بصيغة `.csv` المرفوعة في هذا المستودع في الأعلى وحملها على جهازك).
2. **Open the Live App:** Open the **[Live Demo](https://executive-bi-data-analytics-nsz4u9sz24rve9rb3mh9wi.streamlit.app/)** link.
   (**افتح المنصة حية:** اضغط على رابط الـ Live Demo المتاح في الأعلى).
3. **Upload & Explore:** Upload the downloaded CSV file into the dashboard, and watch the system automatically identify metrics, build visualizations, and generate Pareto-based automated insights!
   (**ارفع واكتشف:** ارفع ملف الـ CSV الذي قمت بتحميله، وشاهد كيف يتعرف النظام تلقائياً على المقاييس، ويبني الرسوم البيانية، ويولد التحليلات الذكية فوراً!).

---

## ⚙️ Core Architecture & Logical Reasoning / البنية والمنطق التحليلي
The background logic is strictly **Schema-Agnostic** (Data Type Driven), operating on the following core principles:
يعتمد المنطق البرمجي خلف الكواليس على **علم أنماط البيانات الحركية الحرة**، ويفكر بناءً على المبادئ التالية:

1. **Dimensional Drilling (أبعاد المنصة):**
   * It scans the uploaded file to isolate **Categorical Dimensions** (text, strings) representing *Who, Where, or When* (e.g., Products, Branches, Regions).
   * It extracts **Numeric Metrics** representing *How Much* (e.g., Revenue, Profit, Units, Wattage) to prevent any mathematical discrepancy.
2. **Real-time Data Filtering (تصفية التقارير):** Applies rapid boolean masking to isolate data subsets on the fly without affecting the global integrity of the file.
3. **Automated Insights (صناديق الدلالة الحركية):** Uses the Pareto Principle (80/20) to extract the top-performing categories and programmatically draft executive textual descriptions in real-time, functioning as an automated data analyst.

---

## 📊 Visual Analytics Spectrum / قطاعات التحليل البصري الهيكلي
* **Absolute Performance (Bar Chart):** Focuses on absolute volume comparison and ranking of top 5 impact drivers using a customized luxury pink-shade palette.
* **Relative Share (Donut Chart):** Illustrates the market share or relative distribution of specific sub-categories.
* **Key Performance Indicators (KPIs):** Instant display of Cumulative Volume, Average Transaction Value, and Total Logged Records.

---

## 📂 Suitable Datasets / نوعية البيانات المتوافقة
This dashboard is highly versatile and optimally tracks **Transactional & Operational Data**:
هذه اللوحة مرنة للغاية وتناسب بشكل مثالي **بيانات المعاملات الإدارية والمالية المستمرة**:
* **Sales & Retail:** Products, regions, and sales representatives vs. revenue, profits, and quantities.
* **Project Management & Telecom Operations:** Stations, solar cell installations, regions, and engineers vs. power output (Watt), maintenance costs, and operation hours.
* **HR Analytics & Payroll:** Departments, job titles, and branches vs. salaries, incentives, and performance ratings.

---

## 🛠️ Installation & Local Deployment / التشغيل المحلي

1. **Clone the repository / استنساخ المستودع:**
```bash
git clone [https://github.com/yara-lab94/Executive-BI-Data-Analytics.git](https://github.com/yara-lab94/Executive-BI-Data-Analytics.git)
cd Executive-BI-Data-Analytics

 ```
Install requirements / تثبيت المكتبات:
```bash
pip install streamlit pandas matplotlib seaborn

 ```
 Run the application / تشغيل المنصة:
```bash
streamlit run app1.py
 
 ```
**🤝 Contribution & License / المساهمة والترخيص
Feel free to fork this repository, report issues, or submit pull requests to enhance the BI analytics engine.


يرحب المشروع بمساهمات المطورين وتطوير محرك التحليلات. الخصائص خاضعة لرخصة MIT المفتوحة.
