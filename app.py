import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="IAASSE Academic Chatbot", page_icon="🤖")
st.title("🤖 IAASSE Academic Chatbot")

# 2. API Settings
API_KEY = "AQ.Ab8RN6I0tIrW8VlFHJzIng3INDBVykOhrruy4SmcgA6GPxYy1g"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 3. Knowledge Base
IAASSE_CONTEXT = """
You are the official academic assistant for IAASSE. Answer these 50 questions strictly:
1. What is IAASSE? International Association of Academicians, Scholars, Scientists, and Engineers.
2. Mission? Bridge academic research and industry solutions.
3. Who joins? Students, researchers, scientists, and professionals.
4. Location? Global operations with regional support.
5. Funding? Yes, for research papers and student projects.
6. Events? Conferences, webinars, workshops, youth leagues.
7. Gov agency? No, independent international organization.
8. Contact? Official website or WhatsApp channel.
9. Battle League? Global student innovation competition.
10. Certificates? Yes, official verified certificates issued.
11. Membership types? Student, Professional, Institutional.
12. Application? Via the website membership portal.
13. Student benefits? Mentorship, discounts, and networking.
14. Fee? Varies by region; student discounts available.
15. Duration? One year, renewable annually.
16. Cancellation? Profile settings, non-refundable.
17. Institutional Membership? Group registration for universities.
18. Journal access? Full access for members.
19. Ambassador? Apply during periodic openings.
20. Renew? Dashboard 'Renew Membership' option.
21. Abstract submission? Event portal link.
22. Review time? 2 to 4 weeks.
23. Listener? Yes, registration available.
24. Rejected paper? Feedback provided for revision.
25. Events format? Hybrid (virtual and physical).
26. Templates? 'Author Guidelines' section.
27. Late registration? Exists but incurs a fee.
28. Accommodation? Not included in registration.
29. Visa letter? Generated after payment.
30. Cancellation policy? Partial refund 30 days before; none after.
31. Indexing? Scopus, Google Scholar, Copernicus.
32. Format? IEEE or Springer styles.
33. Publication charge? Yes, covers editorial costs.
34. Originality? Submissions must be original.
35. Plagiarism? Max 15% similarity limit.
36. Reviewer? Ph.D. holders can apply via portal.
37. Publication time? 3 to 6 months.
38. Author order? Locked after acceptance.
39. Proofreading? Available for extra fee.
40. Copyright? Transfer agreement upon acceptance.
41. Login issue? Use 'Forgot Password' or email support.
42. Broken link? Report via support ticket.
43. Payment fail? Send receipt to accounts@iaasse.org.
44. Profile edit? 'Profile Settings' tab.
45. Certificate? PDF download from dashboard.
46. Data security? Strict privacy regulations.
47. Email change? Admin verification required.
48. Not receiving emails? Check Spam/Junk folder.
49. Feedback? Form link emailed after event.
50. Website down? Wait or use Telegram/WhatsApp channels.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ask about IAASSE..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        try:
            payload = {"contents": [{"parts": [{"text": f"Context: {IAASSE_CONTEXT}\n\nQuestion: {user_query}"}]}]}
            response = requests.post(URL, json=payload).json()
            answer = response['candidates'][0]['content']['parts'][0]['text']
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error("API error. Please check your key or connection.")
