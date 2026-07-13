import streamlit as st

st.set_page_config(page_title="IAASSE Academic Chatbot", page_icon="🤖")
st.title("🤖 IAASSE Academic Chatbot")

# قاعدة البيانات المدمجة (تحتوي على جميع الأسئلة والأجوبة)
knowledge_base = {
    "what is iaasse": "IAASSE is the International Association of Academicians, Scholars, Scientists, and Engineers, focusing on promoting global research and academic collaboration.",
    "mission": "The mission of IAASSE is to bridge the gap between academic research and practical industry solutions globally.",
    "who can join": "Students, researchers, scientists, professors, and industry professionals can join IAASSE.",
    "location": "IAASSE operates globally with regional chapters and online support networks.",
    "funding": "Yes, IAASSE provides funding for selected outstanding research papers and innovative student projects.",
    "events": "IAASSE organizes international conferences, webinars, workshops, and youth league competitions.",
    "government": "No, IAASSE is an independent international academic organization, not a government agency.",
    "contact": "You can contact IAASSE through the official website support channels or the dedicated WhatsApp channel.",
    "battle league": "The IAASSE Battle League is a global competitive platform for students to tackle real-world innovation challenges.",
    "certificates": "Yes, official verified certificates are issued upon completing event requirements.",
    "membership types": "There are three types: Student Membership, Professional Membership, and Institutional Membership.",
    "how to apply": "You can apply through the membership portal on the IAASSE official website.",
    "student benefits": "Student members get access to mentorship, discounted conference fees, and networking with global scientists.",
    "membership fee": "Yes, fees vary by membership type and region, but student discounts are available.",
    "duration": "Standard memberships are valid for one year and can be renewed annually.",
    "cancel membership": "Yes, you can cancel anytime through your profile settings, though fees are non-refundable.",
    "institutional membership": "This program allows universities to register their faculty and students at group rates.",
    "journal access": "Yes, members enjoy full access to selected IAASSE indexed journals.",
    "ambassador": "Yes, applications open periodically for active students to represent IAASSE.",
    "renew membership": "Log into your dashboard and click on the 'Renew Membership' option.",
    "abstract": "Use the conference submission portal link provided on the specific event page.",
    "review process": "The peer-review process usually takes between 2 to 4 weeks depending on the conference volume.",
    "listener": "Yes, registration options are available for both authors and listeners.",
    "rejected paper": "You will receive feedback and can revise it for future cycles or alternative journals.",
    "virtual or in-person": "Most events offer a hybrid model, including both virtual online presentations and physical venues.",
    "templates": "You can download the conference presentation template directly from the 'Author Guidelines' section on the event page.",
    "late registration": "Late registration options exist but may incur an additional late fee.",
    "accommodation": "No, attendees must arrange their own accommodation unless specified otherwise.",
    "invitation letter": "An official invitation letter is generated automatically after successful registration and payment.",
    "cancellation policy": "Cancellations made 30 days before the event get a partial refund; after that, no refunds.",
    "indexing": "Selected papers are indexed in major global databases like Scopus, Google Scholar, and Copernicus.",
    "formatting": "Journals follow standard IEEE or Springer formats, detailed in the templates section.",
    "publication charge": "Yes, article processing charges (APC) apply to open-access journals to cover editorial costs.",
    "previously published": "No, all submissions must be original, unpublished work.",
    "plagiarism": "The maximum acceptable similarity index is 15%, excluding references.",
    "reviewer": "Ph.D. holders and established researchers can apply via the 'Join Reviewer Board' portal.",
    "publication time": "It typically ranges from 3 to 6 months from submission to final publication.",
    "author order": "No, the author list and order are locked once the paper is accepted.",
    "editing services": "Yes, professional academic proofreading can be requested for an extra fee.",
    "copyright": "Authors sign a copyright transfer agreement upon acceptance, allowing IAASSE to publish the work.",
    "login issue": "Reset your password using the 'Forgot Password' link or email tech support.",
    "broken link": "Report it directly via the support ticket system or the WhatsApp support channel.",
    "payment failed": "Send your transaction receipt to accounts@iaasse.org for manual verification.",
    "profile details": "Log into your account dashboard and edit details under the 'Profile Settings' tab.",
    "certificate location": "It will be downloadable in PDF format directly from your event dashboard.",
    "data security": "Yes, we follow strict data protection regulations to ensure user privacy.",
    "change email": "Yes, but it requires verification by contacting the administration helpdesk.",
    "not receiving emails": "Check your Spam/Junk folder, or make sure to whitelist info@iaasse.org.",
    "feedback": "A feedback form link is emailed to all participants right after the event closes.",
    "website down": "Please wait a few minutes or use our alternative Telegram/WhatsApp channels for urgent announcements."
}

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ask about IAASSE..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    query_lower = user_query.lower()
    found = False
    
    for key, value in knowledge_base.items():
        if key in query_lower:
            st.chat_message("assistant").markdown(value)
            st.session_state.messages.append({"role": "assistant", "content": value})
            found = True
            break
            
    if not found:
        default_resp = "I can only assist you with IAASSE academic and technical questions. Please rephrase your question."
        st.chat_message("assistant").markdown(default_resp)
        st.session_state.messages.append({"role": "assistant", "content": default_resp})
