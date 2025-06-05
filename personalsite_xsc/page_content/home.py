import streamlit as st
from PIL import Image
import os

def home_page():
    st.title("许世晨")
    st.markdown("中共党员")
    
    # 左右分栏布局：左侧联系信息，右侧照片
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # 联系信息
        st.markdown(
            """
            <div class="contact-info">
                <strong>电话:</strong> 13668802266<br>
                <strong>邮箱:</strong> <a href="mailto:xushichen2024@163.com">xushichen2024@163.com</a><br>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # 个人简介
        st.markdown("### 个人简介")
        st.markdown("""
        香港中文大学市场营销硕士在读，中山大学本科。具备丰富的跨行业实习经验，涵盖品牌策划、国际交流、金融投行及市场研究领域。擅长数据分析、多模态内容创作及跨部门协作，拥有国家级/省级科研项目成果，英语专业八级（优秀）水平。
        """)
        
    with col2:
        # 显示个人照片
        try:
            # 确保照片文件路径正确（static/images/profile.jpg）
            photo_path = os.path.join("static", "images", "imagexu.jpg")
            image = Image.open(photo_path)
            st.image(image, caption="许世晨", width=200, use_column_width=True)
        except FileNotFoundError:
            st.warning("未找到个人照片，请将照片保存为 `static/images/profile.jpg`")
    
    
    # 简历下载按钮（需将PDF放入static/docs目录）
    st.markdown("### 📄 下载简历")
    try:
        with open("许世晨简历.pdf", "rb") as f:
            st.download_button(
                "下载PDF简历",
                f.read(),
                "许世晨简历.pdf",
                "application/pdf",
                key="resume_download"
            )
    except FileNotFoundError:
        st.warning("未找到简历PDF文件，请检查路径：static/docs/许世晨简历.pdf")