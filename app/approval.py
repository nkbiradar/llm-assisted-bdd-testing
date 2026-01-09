def get_manual_approval():
    choice = input("\nApprove happy path execution? (yes/no): ")
    return choice.lower() == "yes"
