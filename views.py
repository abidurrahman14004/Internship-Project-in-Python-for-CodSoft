import csv

def add(contact):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(contact)

def view():
    data = []
    with open('data.csv') as file:
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
    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            if phone not in row:
                new_list.append(row)
    
    save(new_list)

def search(phone):
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if phone in row:
                data.append(row)
    return data

def update(new_contact):
    name, email, phone = new_contact
    updated_list = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2] == phone:
                updated_list.append([name, email, phone])
            else:
                updated_list.append(row)
    
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_list)
