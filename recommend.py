import streamlit as st
import pandas as pd
from num2words import num2words
import base64
import requests

def app():

    st.header('Đề xuất')

    df = pd.read_excel('combined_data.xlsx')

    col1 = st.sidebar
    def sidebar_bg(img_url):
        side_bg_ext = 'jpg'  # Assuming the image format is PNG (can be adjusted if needed)

        # Retrieve image data from URL
        response = st.cache_resource(requests.get)(img_url, stream=True)
        img_data = response.content

        # Encode image data as base64
        encoded_data = base64.b64encode(img_data).decode()

        # Apply background image style to sidebar
        st.markdown(
            f"""
            <style>
            [data-testid="stSidebar"] > div:first-child {{
                background: url(data:image/{side_bg_ext};base64,{encoded_data});
                background-size: cover;  /* Adjust background sizing as needed */
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Example usage with a valid image URL
    # img_url = "https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTEwL3Jhd3BpeGVsb2ZmaWNlM19taW5pbWFsX2ZsYXRfdmVjdG9yX2Flc3RoZXRpY19pbGx1c3RyYXRpb25fb2ZfYV9hYWMyODk1Ny02ODI3LTQ3OGUtOTQ2Ni0wNWI0MzVhYjk2MmQtYi5qcGc.jpg"  # Replace with your desired image URL
    img_url = "https://4kwallpapers.com/images/wallpapers/porsche-918-spyder-1290x2796-13004.jpg"  # Replace with your desired image URL
    sidebar_bg(img_url)


    col2, col3, col4 = st.columns((1, 1, 1))  # Chia layout thành 3 cột

    with col1:
        # Widget để chọn Tình Trạng xe
        selected_state = col1.multiselect("Chọn Tình trạng xe:", options=df['Tình trạng'].unique())
        if selected_state:
                filtered_brands = df.loc[(df['Tình trạng'].isin(selected_state)), 'Hãng xe'].unique()
        else:
            filtered_brands = df['Hãng xe'].unique()
            
        selected_brands = st.multiselect("Chọn Hãng xe:", filtered_brands)
        # Lọc Dòng xe dựa trên Hãng xe đã chọn
        filtered_vehicles = df.loc[df['Hãng xe'].isin(selected_brands), 'Dòng xe'].unique()
        # Widget để chọn Dòng xe
        selected_vehicles = st.multiselect("Chọn Dòng xe:", filtered_vehicles)
        
        if selected_brands:
            if selected_vehicles:
                # Lọc Kiểu dáng dựa trên Dòng xe đã chọn
                filtered_styles = df.loc[(df['Dòng xe'].isin(selected_vehicles)), 'Kiểu dáng'].unique()
            else:
                # Lọc Kiểu dáng dựa trên Hãng xe đã chọn
                filtered_styles = df.loc[(df['Hãng xe'].isin(selected_brands)), 'Kiểu dáng'].unique()
        else:
            filtered_styles = df['Kiểu dáng'].unique()
        # Widget để chọn Kiểu dáng
        selected_styles = st.multiselect("Chọn Kiểu dáng:", filtered_styles)
        # Widget để chọn Năm sx
        if selected_state == 'Xe Cũ' or selected_state == 'Xe cũ':
            if selected_brands:
                if selected_vehicles:
                # Lọc Kiểu dáng dựa trên Dòng xe đã chọn
                    filtered_year = df.loc[(df['Dòng xe'].isin(selected_vehicles)), 'Năm SX'].unique()
                else:
                    # Lọc Kiểu dáng dựa trên Hãng xe đã chọn
                    filtered_year = df.loc[(df['Hãng xe'].isin(selected_brands)), 'Năm SX'].unique()
        else:
            filtered_year = df['Năm SX'].unique()
        selected_year = st.multiselect("Chọn Năm sản xuất:", filtered_year)
        
        # Widget để chọn Nhiên liệu 
        if selected_brands:
            if selected_vehicles:
            # Lọc Kiểu dáng dựa trên Dòng xe đã chọn
                filtered_fuel = df.loc[(df['Dòng xe'].isin(selected_vehicles)), 'Nhiên liệu'].unique()
            else:
                # Lọc Kiểu dáng dựa trên Hãng xe đã chọn
                filtered_fuel = df.loc[(df['Hãng xe'].isin(selected_brands)), 'Nhiên liệu'].unique()
        else:
            filtered_fuel = df['Nhiên liệu'].unique()
        selected_segment = st.multiselect("Chọn Nhiên liệu:", filtered_fuel)
        
        # Widget để chọn Hộp số 
        if selected_brands:
            if selected_vehicles:
            # Lọc Kiểu dáng dựa trên Dòng xe đã chọn
                filtered_hopso = df.loc[(df['Dòng xe'].isin(selected_vehicles)), 'Hộp số'].unique()
            else:
                # Lọc Kiểu dáng dựa trên Hãng xe đã chọn
                filtered_hopso = df.loc[(df['Hãng xe'].isin(selected_brands)), 'Hộp số'].unique()
        else:
            filtered_hopso = df['Hộp số'].unique()
        selected_hopso = st.multiselect("Chọn Hộp số:", filtered_hopso)
        
        # Widget để chọn Số chỗ ngồi
        if selected_brands:
            if selected_vehicles:
            # Lọc Kiểu dáng dựa trên Dòng xe đã chọn
                filtered_seat = df.loc[(df['Dòng xe'].isin(selected_vehicles)), 'Số chỗ ngồi'].unique()
            else:
                # Lọc Kiểu dáng dựa trên Hãng xe đã chọn
                filtered_seat = df.loc[(df['Hãng xe'].isin(selected_brands)), 'Số chỗ ngồi'].unique()
        else:
            filtered_seat = df['Số chỗ ngồi'].unique()
        selected_seat = st.multiselect("Chọn Số chỗ ngồi:", filtered_seat)
    # Nút lọc
    filter_button = col1.button("Search 🔍")
    
    with col2, col3, col4:
        # Nếu nút lọc được nhấn
        if filter_button:
            if selected_brands or selected_vehicles or selected_styles or selected_state or selected_segment or selected_hopso or selected_seat or selected_year: #or (selected_km_min and selected_km_max):
                # Khởi tạo điều kiện lọc
                mask = pd.Series([True] * len(df))
                
                # Lọc DataFrame dựa trên các lựa chọn
                if selected_state:
                    mask &= df['Tình trạng'].isin(selected_state)
                if selected_brands:
                    mask &= df['Hãng xe'].isin(selected_brands)
                if selected_vehicles:
                    mask &= df['Dòng xe'].isin(selected_vehicles)
                if selected_styles:
                    mask &= df['Kiểu dáng'].isin(selected_styles)
                if selected_segment:
                    mask &= df['Nhiên liệu'].isin(selected_segment)
                if selected_hopso:
                    mask &= df['Hộp số'].isin(selected_hopso)
                if selected_seat:
                    mask &= df['Số chỗ ngồi'].isin(selected_seat)
                if selected_year:
                    mask &= df['Năm SX'].isin(selected_year)
                    
                # if selected_km_min and selected_km_max:
                #     mask = (df['Km đã đi'] >= selected_km_min) & (df['Km đã đi'] <= selected_km_max)

                filtered_df = df[mask]
                
                # Reset index
                filtered_df = filtered_df.reset_index(drop=True)
                
                if filtered_df.shape[0] == 0:
                    st.error("***No result is found***\n\n Please select 🔻 / re-enter 💬    🧐")
                else: 
                    # Hiển thị số lượng features
                    st.write("Number of cars found: ", filtered_df.shape[0])

                    # Hiển thị hình ảnh, tên xe và đơn giá
                    count = 0
                    cols = [col2, col3, col4]
                    for index, row in filtered_df.iterrows():
                        count = count + 1
                        col_index = (count - 1) % 3
                        col = cols[col_index]
                        col.image(row['Image_URL'], caption=row['Tên Xe'])
                        col.subheader("Chi tiết xe:")
                        col.text("- Hộp số: " + str(row['Hộp số']))
                        col.text("- Nhiên liệu: " + str(row['Nhiên liệu']))
                        col.text("- Tình trạng: " + str(row['Tình trạng']))
                        if row['Tình trạng'] == 'Xe Mới' or row['Tình trạng'] == 'Xe mới':
                            col.text("- Số chỗ ngồi: " + str(row['Số chỗ ngồi']) + ' chỗ')
                        else: 
                            col.text("- Km đã đi: " + str(row['Km đã đi']) + ' KM')
                        col.text('')  # Thêm một dòng trống để tạo khoảng cách                        
                        # Chia thành 2 cột
                        with col:
                            # Button with bold text using markdown syntax
                            button_content = f"**Select**"

                            # Button styling using inline CSS
                            button_style = """
                            <style>
                                .buy-button {
                                background-color: #CBEAF5;
                                color: white;
                                padding: 5px 10px;
                                border: none;
                                border-radius: 10px;
                                float: right;
                                cursor: pointer;
                                text-decoration: none;
                                font-weight: normal !important;
                                }
                            </style>
                            """
                            # Combine button content, link, and style
                            content = f"""{button_style}
                            <a class="buy-button" href="{row['Link xe']}" target="_blank">{button_content}</a>
                            """
                            # Display content with unsafe_allow_html for button styling
                            st.markdown(content, unsafe_allow_html=True)
                            
                        col.text("-" * 10)
            else:
                st.error("***No result is found***\n\n Please select 🔻 / re-enter 💬    🧐")


