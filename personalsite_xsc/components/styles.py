import streamlit as st

def load_css():
    """直接嵌入 CSS 样式，避免文件依赖"""
    st.markdown(
        """
        <style>
        /* 全局样式 */
        body {
            font-family: 'Segoe UI', sans-serif;
            line-height: 1.6;
        }
        .st-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        h1, h2, h3 {
            color: #2C3E50;
            margin-bottom: 1rem;
        }
        .section {
            background: white;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .contact-info {
            margin: 1.5rem 0;
        }
        .experience-item {
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #e0e0e0;
        }
        .skill-list {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        .skill-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 4px;
        }
        /* 响应式布局 */
        @media (max-width: 768px) {
            .skill-list { grid-template-columns: 1fr; }
            .st-sidebar { width: 100% !important; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )