import streamlit as st

class ATM:
    def __init__(self, balance=5000, pin=1234):
        self.balance = balance
        self.pin = pin
        self.is_authenticated = False
        self.attempts = 3
    
    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.is_authenticated = True
            return True
        else:
            self.attempts -= 1
            if self.attempts == 0:
                return "Card blocked."
            return f"Invalid PIN. {self.attempts} attempts remaining."
    
    def check_balance(self):
        if not self.is_authenticated:
            return "Please authenticate first."
        return f"Current balance: Rs.{self.balance}"

    def deposit(self, amount):
        if not self.is_authenticated:
            return "Please authenticate first."
        self.balance += amount
        return f"Deposited Rs.{amount}. New balance: Rs.{self.balance}"

    def withdraw(self, amount):
        if not self.is_authenticated:
            return "Please authenticate first."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrawn Rs.{amount}. New balance: Rs.{self.balance}"

# Initialize session state
if 'atm' not in st.session_state:
    st.session_state.atm = ATM()
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'message' not in st.session_state:
    st.session_state.message = ""

# App title
st.title("ATM Simulator")

# Authentication section
if not st.session_state.authenticated:
    st.subheader("Please authenticate")
    pin_input = st.number_input("Enter your PIN:", min_value=1000, max_value=9999, step=1)
    
    if st.button("Submit PIN"):
        result = st.session_state.atm.authenticate(pin_input)
        if result is True:
            st.session_state.authenticated = True
            st.session_state.message = "Authentication successful!"
            st.experimental_rerun()
        else:
            st.session_state.message = result
    
    if st.session_state.message:
        st.warning(st.session_state.message)

# ATM operations section
else:
    st.success("You are authenticated!")
    
    # Create tabs for different operations
    tab1, tab2, tab3 = st.tabs(["Check Balance", "Deposit", "Withdraw"])
    
    with tab1:
        if st.button("Check Balance", key="check"):
            st.session_state.message = st.session_state.atm.check_balance()
    
    with tab2:
        deposit_amount = st.number_input("Enter amount to deposit:", min_value=1.0, step=1.0)
        if st.button("Deposit"):
            st.session_state.message = st.session_state.atm.deposit(deposit_amount)
    
    with tab3:
        withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=1.0, step=1.0)
        if st.button("Withdraw"):
            st.session_state.message = st.session_state.atm.withdraw(withdraw_amount)
    
    # Display operation result
    if st.session_state.message:
        st.info(st.session_state.message)
    
    # Logout button
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.message = "Logged out successfully!"
        st.experimental_rerun()