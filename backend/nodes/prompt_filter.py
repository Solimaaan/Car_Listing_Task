from backend.state import CarState

def filter_input(state:CarState) -> CarState:
    user_input = state.get("input", "can't reach")
    state['filtered_input'] = user_input.strip()
    blacklist = ["ignore", "password", "username", 
                 "passwords", "usernames", "system", "admin", 
                 "api key", "user's", "hack", "override", "malware", 
                 "pretend", "config", "url", "forget", "exploit"]

    if any(word in state['filtered_input'].lower() for word in blacklist):
        print("Filtered input contains blacklisted words.")
        state['filtered_input'] = "This input has been filtered due to blacklisted content."
        raise ValueError("Filtered input contains malicious commands.")
    else:
        print("Filtered input is clean.")
        
    return state