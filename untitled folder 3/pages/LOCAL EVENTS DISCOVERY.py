import streamlit as st
import datetime
import calendar
import pandas as pd


events = []


st.title("Local Events Calendar")


def create_monthly_table(year, month):
    cal = calendar.monthcalendar(year, month)
    data = []
    headers = [calendar.day_name[d] for d in range(7)]

    for week in cal:
        data.append([str(day) if day != 0 else "" for day in week])

    df = pd.DataFrame(data, columns=headers)
    return df


today = datetime.date.today()


year = today.year
month = today.month


st.write(f"### {calendar.month_name[month]} {year}")


table = create_monthly_table(year, month)


st.write(f'<style>.dataframe .col1 {{ width: 700px; }}</style>', unsafe_allow_html=True)
st.dataframe(table)


st.sidebar.header("Add Event")
event_date = st.sidebar.date_input("Select Date")
event_description = st.sidebar.text_input("Event Description")

if st.sidebar.button("Add Event"):
    events.append((event_date, event_description))
    st.success(f"Event added on {event_date}: {event_description}")


st.header("Events for the Current Month")

for event in events:
    event_date, event_description = event
    if event_date.year == year and event_date.month == month:
        st.write(f"- {event_date.day}: {event_description}")