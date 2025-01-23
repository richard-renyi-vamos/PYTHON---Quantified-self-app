import json
import os
from datetime import datetime

class QuantifiedSelfApp:
    def __init__(self):
        self.data_file = 'quantified_self_data.json'
        self.activities = self.load_data()

    def load_data(self):
        """Load activity data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return []

    def save_data(self):
        """Save activity data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.activities, file)

    def log_activity(self):
        """Log a new activity."""
        date = input("Enter the date (YYYY-MM-DD): ")
        activity = input("Enter the activity: ")
        duration = input("Enter the duration (in minutes): ")
        
        entry = {
            'date': date,
            'activity': activity,
            'duration': int(duration)
        }
        
        self.activities.append(entry)
        self.save_data()
        print("Activity logged successfully!")

    def view_activities(self):
        """View all logged activities."""
        if not self.activities:
            print("No activities logged yet.")
            return
        
        print("\nLogged Activities:")
        for entry in self.activities:
            print(f"Date: {entry['date']}, Activity: {entry['activity']}, Duration: {entry['duration']} minutes")
    
    def run(self):
        """Run the main app loop."""
        while True:
            print("\nQuantified Self App")
            print("1. Log Activity")
            print("2. View Activities")
            print("3. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.log_activity()
            elif choice == '2':
                self.view_activities()
            elif choice == '3':
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = QuantifiedSelfApp()
    app.run()
