# Pipin' Hot Main Application Entry Point
# Skeleton: Modular CLI Database Pipeline


import sys

# Defining functions used in main outside of modules
# the AI gave us the ASCII borders and I thought they were cool so we kept them
def display_menu():
    print("\n" + "="*40)
    print("      PIPIN' HOT DATABASE MANAGEMENT      ")
    print("="*40)
    print("1. Load from Local (CSV -> Memory -> Normalize -> Cleanse)")
    print("2. Upload to Adminer (Remote Database)")
    print("3. Exit")
    print("="*40)

def get_user_choice():
# We decided on manual user input to prevent accidental execution for the purposes of load and strain
    try:
        choice = input("Select an option (1-3): ").strip()
        return choice
    except (KeyboardInterrupt, SystemExit):
        print("\nExiting safely.")
        sys.exit(0)


# --- Module Imports (Subroutines written by other users) ---
# We wrap these in try/except so the main script still runs if any file is incomplete
try:
    import db_setup
    import data_loader
    import cloud_upload
except ImportError as e:
    print(f"[Warning] Missing a module, to be improved next sprint! Error: {e}")


# --- Main Menu Logic ---
def main():
    # Placeholder initialization steps

    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            print("\n[Action] Loading from Local...")
            try:
                # 1. Loads from CSV into memory
                raw_data = data_loader.load_csv_to_memory()
                
                # 2. Creates DB for data manipulation if not already created
                # 3. Execute SQL function to normalise
                # 4. Execute SQL functions to cleanse
                db_setup.initialize_database()
                db_setup.execute_normalization(raw_data)
                db_setup.execute_cleansing()
                
                print("[Success] Local data processed, normalized, cleansed, and saved in real-time.")
            except NameError:
                print("[Error] Subroutine modules are not fully implemented yet.")
                
        elif choice == '2':
            print("\n[Action] Uploading to Remote Database...")
            try:
                # Loads to database in Adminer (Connects to Pipin' Hot DB)
                pipin_hot_address = "PENDING_ADDRESS_PLACEHOLDER" 
                cloud_upload.upload_to_adminer(target_address=pipin_hot_address)
            except NameError:
                print("[Error] Upload module is not fully implemented yet.")
                
        elif choice == '3':
            print("\nExiting system. Goodbye!")
            break
        else:
            print("\n[Invalid Option] Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()