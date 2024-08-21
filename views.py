import csv

def add(contact):
   
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

def view():
  
    data = []
    with open('data.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def remove(phone):

    def save(data):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
    new_list = []
    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and phone != row[2]:  
                new_list.append(row)
    
    save(new_list)

def search(phone):

    data = []
    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and phone == row[2]:  
                data.append(row)
    return data
def update(new_contact):
    name, email, phone = new_contact
    updated = False
    updated_list = []

    print(f"Updating contact with phone: {phone}")

    with open('data.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  
                if row[2] == phone:
                    print(f"Found matching contact: {row}")
                    updated_list.append([name, email, phone])  
                    updated = True
                else:
                    updated_list.append(row)

    if updated:
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_list)
        print("Contact updated successfully.")
    else:
        print("No matching contact found.")


    print("Updated contact list:")
    for item in updated_list:
        print(item)

