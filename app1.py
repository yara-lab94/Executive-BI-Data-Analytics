import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. إعداد الصفحة الأساسي والأنيق
st.set_page_config(
    page_title="Executive Data Analytics Platform", 
    page_icon="📊", 
    layout="wide"
)

# --- ذاكرة مؤقتة لحفظ الملف لمنع العودة للسكون عند تدوير اللغة ---
if "file_data_cache" not in st.session_state:
    st.session_state.file_data_cache = None

# 2. السايد بار - التحكم الفعلي في اللغات (عربي / إنجليزي)
st.sidebar.markdown("### 🌐 لغة الواجهة / Interface Language")
lang_option = st.sidebar.radio(
    "اختر لغة العرض المعتمدة للوحة التحكم:",
    ["العربية", "English"],
    index=0,
    label_visibility="collapsed"
)
is_arabic = (lang_option == "العربية")

# كشف المظهر الحالي (مضيء/مظلم) تلقائياً لتناسق ألوان الرسوم
is_dark_theme = st.get_option("theme.base") == "dark"

# تفعيل تبديل الاتجاه والمحاذاة ديناميكياً بناءً على اختيار زر اللغة
direction_css = "rtl" if is_arabic else "ltr"
text_align_css = "right" if is_arabic else "left"

# 3. تثبيت اللون الزهري الفخم والفاقع المعتمد بالكامل لحالتي السكون والبيانات
primary_color = "#E91E63"  
card_bg = "rgba(233, 30, 99, 0.03)"
border_color = "rgba(233, 30, 99, 0.15)"

# 4. حقن الـ CSS لتغيير اتجاه المنصة وهويتها البصرية حسب الحالة واللغة
st.markdown(f"""
    <style>
        .main .block-container {{
            direction: {direction_css} !important;
            text-align: {text_align_css} !important;
        }}
        .premium-hero-canvas {{
            background-color: {card_bg};
            border: 1px dashed {border_color};
            border-top: 4px solid {primary_color};
            padding: 50px;
            border-radius: 12px;
            text-align: center;
            margin-top: 25px;
        }}
        .premium-hero-icon {{
            font-size: 55px;
            color: {primary_color};
            margin-bottom: 15px;
        }}
        /* صناديق استخلاص دلالات الرسوم البيانية المتأثرة باللون الزهري المحاذية بدقة */
        .insight-executive-box {{
            background-color: {card_bg};
            border-right: {"4px solid " + primary_color if is_arabic else "none"} !important;
            border-left: {"4px solid " + primary_color if not is_arabic else "none"} !important;
            padding: 15px;
            border-radius: 6px;
            margin-top: 15px;
            font-size: 13.5px;
            line-height: 1.6;
            text-align: {text_align_css};
            min-height: 110px;
        }}
    </style>
""", unsafe_allow_html=True)

# حقل رفع الملف في السايد بار
st.sidebar.markdown("---")
sidebar_upload_title = "### 📂 تحميل البيانات" if is_arabic else "### 📂 Data Ingestion"
file_label = "رفع ملف (CSV):" if is_arabic else "Upload File (CSV):"
st.sidebar.markdown(sidebar_upload_title)
uploaded_file = st.sidebar.file_uploader(file_label, type=["csv"], label_visibility="collapsed")

if uploaded_file is not None:
    st.session_state.file_data_cache = uploaded_file

# 5. معالجة وتدفق البيانات وعرض اللوحة التنفيذية
if st.session_state.file_data_cache is not None:
    df = None
    for encoding in ['utf-8', 'latin1', 'cp1252']:
        try:
            st.session_state.file_data_cache.seek(0)
            df = pd.read_csv(st.session_state.file_data_cache, encoding=encoding, sep=None, engine='python', on_bad_lines='skip')
            break
        except Exception:
            continue
            
    if df is not None and not df.empty:
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category', 'string']).columns.tolist()

        # أبعاد التحكم بالمنصة المترجمة بالكامل
        st.sidebar.markdown("---")
        dimensions_title = "### ⚙️ أبعاد المنصة" if is_arabic else "### ⚙️ Dimensions"
        st.sidebar.markdown(dimensions_title)
        
        cat_label = "المتغير التصنيفي (الأساسي):" if is_arabic else "Categorical Variable:"
        num_label = "المتغير الرقمي المالي:" if is_arabic else "Numeric Variable:"
        
        main_category = st.sidebar.selectbox(cat_label, categorical_cols if categorical_cols else df.columns)
        main_numeric = st.sidebar.selectbox(num_label, numeric_cols) if numeric_cols else None

        # عنوان اللوحة القيادي المنفصل تماماً حسب اختيار زر اللغة
        if is_arabic:
            st.markdown(f"<h1 style='color:{primary_color}; font-size: 24px; margin-bottom:15px;'>📊 منصة ذكاء الأعمال والتحليلات التنفيذية</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='color:{primary_color}; font-size: 24px; margin-bottom:15px;'>📊 Executive BI & Data Analytics Platform</h1>", unsafe_allow_html=True)
        st.markdown("---")

        # التصفية السريعة
        st.sidebar.markdown("---")
        filter_label = "تصفية التقارير حسب الفئة:" if is_arabic else "Report Filter:"
        unique_vals = ["الكل"] + list(df[main_category].dropna().unique()) if is_arabic else ["All"] + list(df[main_category].dropna().unique())
        selected_filter = st.sidebar.selectbox(filter_label, unique_vals)
        
        filtered_df = df.copy()
        if selected_filter not in ["الكل", "All"]:
            filtered_df = df[df[main_category] == selected_filter]

        # 📈 عرض مؤشرات الأداء الرئيسية (KPIs) باللغة النشطة
        if main_numeric:
            kpi_header = "### 📈 مؤشرات الأداء الحالية" if is_arabic else "### 📈 Key Metric Indicators"
            st.markdown(kpi_header)
            
            lbl_vol = "إجمالي الكتلة المتراكمة" if is_arabic else "Total Volume"
            lbl_avg = "متوسط قيمة المعاملة" if is_arabic else "Average Value"
            lbl_rec = "إجمالي السجلات الموثقة" if is_arabic else "Total Records"
            
            kpi1, kpi2, kpi3 = st.columns(3)
            with kpi1:
                st.metric(label=lbl_vol, value=f"{filtered_df[main_numeric].sum():,.2f}")
            with kpi2:
                st.metric(label=lbl_avg, value=f"{filtered_df[main_numeric].mean():,.2f}")
            with kpi3:
                st.metric(label=lbl_rec, value=f"{filtered_df.shape[0]:,}")
            
            st.markdown("---")
            
            # 📊 قسم الرسوم البيانية المتناسقة بجانب بعضها
            layout_header = "### 📊 قطاعات التحليل البصري الهيكلي" if is_arabic else "### 📊 Visual Analytics Layout"
            st.markdown(layout_header)
            chart_col1, chart_col2 = st.columns(2)
            
            # تجهيز داتا الرسوم حركياً
            chart_data = filtered_df.groupby(main_category, as_index=False)[main_numeric].sum().sort_values(by=main_numeric, ascending=False)
            
            if not chart_data.empty:
                top_name = str(chart_data.iloc[0][main_category])
                top_val = chart_data.iloc[0][main_numeric]
                total_sum = chart_data[main_numeric].sum()
                percentage = (top_val / total_sum * 100) if total_sum > 0 else 0
            else:
                top_name = "N/A"
                top_val = 0
                percentage = 0

            def configure_safe_chart(fig, ax):
                fig.patch.set_facecolor('none')
                ax.set_facecolor('none')
                lbl_color = "#FFFFFF" if is_dark_theme else "#000000"
                ax.title.set_color(lbl_color)
                ax.xaxis.label.set_color(lbl_color)
                ax.yaxis.label.set_color(lbl_color)
                ax.tick_params(colors=lbl_color)
                ax.grid(True, color=lbl_color, linestyle='--', alpha=0.1)

            # تدرجات اللون الزهري الفخم لتوحيد هوية الرسوم البيانية تماماً مع المنصة
            pink_shades = ["#880E4F", "#C2185B", "#E91E63", "#F06292", "#F8BBD0"]

            # --- اللوحة الأولى (العمود الأول: Bar Chart) ---
            with chart_col1:
                if is_arabic:
                    st.markdown("#### 🔹 مخطط مقارنة الأداء المطلق والمساهمة", unsafe_allow_html=True)
                else:
                    st.markdown("#### 🔹 Performance Comparison (Bar Chart)", unsafe_allow_html=True)
                
                fig1, ax1 = plt.subplots(figsize=(6, 3.8))
                configure_safe_chart(fig1, ax1)
                
                # [تعديل تقني مصلح]: إضافة التعيين الصريح للـ hue و legend لإيقاف تحديثات التحذير مستقبلاً
                sns.barplot(
                    data=chart_data.head(5), 
                    x=main_numeric, 
                    y=main_category, 
                    ax=ax1, 
                    palette=pink_shades[:len(chart_data.head(5))],
                    hue=main_category,
                    legend=False
                )
                plt.tight_layout()
                st.pyplot(fig1)
                
                # صندوق الدلالة أحادي اللغة تماماً حسب اختيار الزر
                if is_arabic:
                    box_html = f"""
                        <div class="insight-executive-box">
                            💡 <b>دلالة التحليل المطلق:</b> يوضح الرسم أن الفئة <b>({top_name})</b> تمثل ركيزة المساهمة القصوى في لوحة التحكم حالياً بإجمالي كتلة تبلغ <b>{top_val:,.2f}</b>، مما يستوجب تركيز الخطط التشغيلية والموارد لدعم هذا القطاع القيادي.
                        </div>
                    """
                else:
                    box_html = f"""
                        <div class="insight-executive-box">
                            💡 <b>Absolute Insight:</b> The analysis highlights that <b>({top_name})</b> represents the ultimate driving factor with an aggregated volume of <b>{top_val:,.2f}</b>, requiring targeted resource allocation to support this leading segment.
                        </div>
                    """
                st.markdown(box_html, unsafe_allow_html=True)

            # --- اللوحة الثانية (العمود الثاني: Donut Chart) ---
            with chart_col2:
                if is_arabic:
                    st.markdown("#### 🔹 مخطط الوزن النسبي وتوزيع الحصص المئوية", unsafe_allow_html=True)
                else:
                    st.markdown("#### 🔹 Relative Share Distribution (Donut Chart)", unsafe_allow_html=True)
                
                fig2, ax2 = plt.subplots(figsize=(6, 3.8))
                configure_safe_chart(fig2, ax2)
                
                pie_data = filtered_df.groupby(main_category)[main_numeric].sum().head(5)
                
                wedges, texts, autotexts = ax2.pie(
                    pie_data, 
                    autopct='%1.1f%%', 
                    startangle=140, 
                    colors=pink_shades[:len(pie_data)],
                    pctdistance=0.72, 
                    wedgeprops=dict(width=0.42, edgecolor='white' if not is_dark_theme else '#1e1e1e')
                )
                
                # إجبار خطوط النسب لتكون بيضاء عريضة ومقروءة داخل اللون الزهري
                for autotext in autotexts: 
                    autotext.set_color('white')
                    autotext.set_fontsize(9.5)
                    autotext.set_weight('bold')
                    
                ax2.legend(wedges, pie_data.index, loc="center left", bbox_to_anchor=(0.95, 0.5))
                plt.tight_layout()
                st.pyplot(fig2)
                
                # صندوق الدلالة الثاني أحادي اللغة تماماً حسب اختيار الزر
                if is_arabic:
                    box_html2 = f"""
                        <div class="insight-executive-box">
                            💡 <b>دلالة التحليل النسبي:</b> يستحوذ العنصر المتصدر بمفرده على حصة نسبية تقدر بنحو <b>{percentage:.1f}%</b> من مجموع النطاق المستعرض، وهو مؤشر تركز قوي يتطلب مراقبة مستمرة لضمان توازن العمليات بين الأقسام.
                        </div>
                    """
                else:
                    box_html2 = f"""
                        <div class="insight-executive-box">
                            💡 <b>Relative Insight:</b> The top performing item commands a substantial <b>{percentage:.1f}%</b> of the displayed spectrum, signaling a significant concentration indicator that requires ongoing evaluation to maintain structural balance.
                        </div>
                    """
                st.markdown(box_html2, unsafe_allow_html=True)

        st.markdown("---")
        
        # 📂 تقرير البيانات النهائي البارز المترجم
        export_header = "### 📂 تقرير وتصدير ملف البيانات النهائي" if is_arabic else "### 📂 Export Data Insights Report"
        btn_label = "📥 تحميل تقرير البيانات الحالي (ملف CSV مصفى)" if is_arabic else "📥 Download Current Data Report (CSV)"
        preview_header = "#### 📋 مراجعة ومعاينة سجلات جدول السجلات بالكامل" if is_arabic else "#### 📋 Dataset Preview"
        
        st.markdown(export_header)
        csv_buffer = filtered_df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label=btn_label, 
            data=csv_buffer, 
            file_name=f"BI_Executive_Report.csv", 
            mime="text/csv"
        )
        
        st.markdown(" ")
        st.markdown(preview_header)
        
        # [تعديل تقني مصلح]: استبدال استخدام use_container_width بالخيار الجديد المطور والمستقر للمكتبة
        st.dataframe(filtered_df, width="stretch")

else:
    # 6. شاشة حالة السكون الترحيبية المستقلة تماماً باللون الزهري واللغة المنفصلة 100%
    if is_arabic:
        st.markdown("""
            <h1 style='text-align: center; color: #E91E63; font-size: 24px; margin-top: 15px;'>📊 منصة ذكاء الأعمال والتحليلات التنفيذية المتقدمة</h1>
            <hr>
            <div class="premium-hero-canvas">
                <div class="premium-hero-icon">📈</div>
                <h2 style="color: #E91E63; font-size: 18px; margin-bottom: 12px;">لوحة التحكم في حالة سكون مؤقت (بانتظار ملفاتك)</h2>
                <p style="font-size: 14px; color: #5f6368; max-width: 850px; margin: 0 auto; line-height: 1.8;">
                    مرحباً بك في واجهتك القيادية المخصصة. لتفعيل المؤشرات الإحصائية الذكية، وبناء التقارير التفاعلية للبيانات وعرض التحليلات المنطقية، يرجى التوجه إلى الشريط الجانبي وسحب ملف البيانات الخاص بك بصيغة (CSV) وإسقاطه في الحقل المخصص للرفع لبدء المعالجة الفورية.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <h1 style='text-align: center; color: #E91E63; font-size: 24px; margin-top: 15px;'>📊 Executive BI & Advanced Data Analytics Platform</h1>
            <hr>
            <div class="premium-hero-canvas">
                <div class="premium-hero-icon">📈</div>
                <h2 style="color: #E91E63; font-size: 18px; margin-bottom: 12px;">Dashboard is Currently in Idle Mode (Awaiting Files)</h2>
                <p style="font-size: 14px; color: #5f6368; max-width: 850px; margin: 0 auto; line-height: 1.8;">
                    Welcome to your strategic command interface. To initiate automated metrics, build semantic charts, and generate your custom data report, please use the sidebar panel to drag and drop your dataset file in (CSV) format to trigger full processing.
                </p>
            </div>
        """, unsafe_allow_html=True)