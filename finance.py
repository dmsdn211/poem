import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 시가총액 기준 상위 10개 글로벌 기업 (2025년 기준 가정, 필요시 업데이트)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta Platforms": "META",
    "Eli Lilly": "LLY",
    "TSMC": "TSM"
}

st.title("📈 글로벌 시가총액 Top 10 기업의 최근 1년 주가 추이")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 데이터 가져오기
@st.cache_data
def fetch_stock_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df["Adj Close"]

# 데이터프레임 생성
data = pd.DataFrame()
for name, symbol in top10_companies.items():
    try:
        series = fetch_stock_data(symbol)
        series.name = name
        data = pd.concat([data, series], axis=1)
    except Exception as e:
        st.warning(f"{name} ({symbol}) 데이터 로딩 실패: {e}")

# 선택 옵션
selected_companies = st.multiselect(
    "조회할 기업 선택:",
    options=list(top10_companies.keys()),
    default=list(top10_companies.keys())
)

# Plotly 시각화
if not selected_companies:
    st.info("표시할 기업을 하나 이상 선택하세요.")
else:
    fig = go.Figure()
    for company in selected_companies:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[company],
            mode='lines',
            name=company
        ))

    fig.update_layout(
        title="최근 1년간 주가 변화 (종가 기준)",
        xaxis_title="날짜",
        yaxis_title="주가 (USD 또는 현지 통화)",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
