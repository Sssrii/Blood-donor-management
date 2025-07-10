#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

class Donor {
public:
    std::string name, bloodGroup, location, phone;
    int age, pincode;

    void input();     // Take donor details
    void display();   // Display donor details
};

void Donor::input() {
    std::cout << "Enter Name: ";
    std::getline(std::cin, name);
    std::cout << "Enter Age: ";
    std::cin >> age;
    std::cin.ignore(); // Clear newline
    std::cout << "Enter Blood Group (e.g., A+, O-): ";
    std::getline(std::cin, bloodGroup);
    std::cout << "Enter Location (e.g., Pune): ";
    std::getline(std::cin, location);
    std::cout << "Enter Pincode: ";
    std::cin >> pincode;
    std::cin.ignore();
    std::cout << "Enter Phone Number: ";
    std::getline(std::cin, phone);
}

void Donor::display() {
    std::cout << "\nName: " << name
              << "\nAge: " << age
              << "\nBlood Group: " << bloodGroup
              << "\nLocation: " << location
              << "\nPincode: " << pincode
              << "\nPhone: " << phone << "\n";
}

void saveDonorToFile(Donor d) {
    std::ofstream file("donors.txt", std::ios::app);
    if (file.is_open()) {
        file << d.name << "," << d.age << "," << d.bloodGroup << ","
             << d.location << "," << d.pincode << "," << d.phone << "\n";
        file.close();
    } else {
        std::cout << "Error saving to file.\n";
    }
}

void searchByBloodGroup(std::string bg) {
    std::ifstream file("donors.txt");
    std::string line;
    bool found = false;

    while (getline(file, line)) {
        std::stringstream ss(line);
        std::string name, age, bloodGroup, location, pincode, phone;

        getline(ss, name, ',');
        getline(ss, age, ',');
        getline(ss, bloodGroup, ',');
        getline(ss, location, ',');
        getline(ss, pincode, ',');
        getline(ss, phone, ',');

        if (bloodGroup == bg) {
            found = true;
            std::cout << "\nDonor Found:\n";
            std::cout << "Name: " << name << "\nAge: " << age
                      << "\nBlood Group: " << bloodGroup
                      << "\nLocation: " << location
                      << "\nPincode: " << pincode
                      << "\nPhone: " << phone << "\n";
        }
    }

    if (!found)
        std::cout << "No donor found with blood group " << bg << "\n";
}

void searchByBloodGroupAndLocation(std::string bg, std::string loc) {
    std::ifstream file("donors.txt");
    std::string line;
    bool found = false;

    while (getline(file, line)) {
        std::stringstream ss(line);
        std::string name, age, bloodGroup, location, pincode, phone;

        getline(ss, name, ',');
        getline(ss, age, ',');
        getline(ss, bloodGroup, ',');
        getline(ss, location, ',');
        getline(ss, pincode, ',');
        getline(ss, phone, ',');

        if (bloodGroup == bg && location == loc) {
            found = true;
            std::cout << "\nDonor Found:\n";
            std::cout << "Name: " << name << "\nAge: " << age
                      << "\nBlood Group: " << bloodGroup
                      << "\nLocation: " << location
                      << "\nPincode: " << pincode
                      << "\nPhone: " << phone << "\n";
        }
    }

    if (!found)
        std::cout << "No donor found with blood group " << bg
                  << " in location " << loc << "\n";
}

struct DonorRecord {
    std::string name, bloodGroup, location, phone;
    int age, pincode, distance;
};

void findNearestDonors(int userPincode) {
    std::ifstream file("donors.txt");
    std::string line;
    std::vector<DonorRecord> donors;

    while (getline(file, line)) {
        std::stringstream ss(line);
        DonorRecord d;
        std::string temp;

        getline(ss, d.name, ',');
        getline(ss, temp, ','); d.age = std::stoi(temp);
        getline(ss, d.bloodGroup, ',');
        getline(ss, d.location, ',');
        getline(ss, temp, ','); d.pincode = std::stoi(temp);
        getline(ss, d.phone, ',');

        d.distance = std::abs(userPincode - d.pincode);
        donors.push_back(d);
    }

    std::sort(donors.begin(), donors.end(), [](DonorRecord a, DonorRecord b) {
        return a.distance < b.distance;
    });

    std::cout << "\nDonors Sorted by Nearest Pincode:\n";
    for (auto d : donors) {
        std::cout << "Name: " << d.name << ", Blood Group: " << d.bloodGroup
                  << ", Location: " << d.location << ", Pincode: " << d.pincode
                  << ", Distance: " << d.distance << ", Phone: " << d.phone << "\n";
    }
}

int main() {
    int choice;

    do {
        std::cout << "\n--- Blood Donation Manager ---\n";
        std::cout << "1. Register Donor\n";
        std::cout << "2. Search by Blood Group\n";
        std::cout << "3. Search by Blood Group + Location\n";
        std::cout << "4. Show Nearest Donors (Using Pincode)\n";
        std::cout << "5. Exit\n";
        std::cout << "Enter choice: ";
        std::cin >> choice;
        std::cin.ignore();  // To clear newline after number

        if (choice == 1) {
            Donor d;
            d.input();
            saveDonorToFile(d);
            std::cout << "Donor Registered Successfully!\n";
        }
        else if (choice == 2) {
            std::string bg;
            std::cout << "Enter Blood Group to search: ";
            std::getline(std::cin, bg);
            searchByBloodGroup(bg);
        }
        else if (choice == 3) {
            std::string bg, loc;
            std::cout << "Enter Blood Group: ";
            std::getline(std::cin, bg);
            std::cout << "Enter Location: ";
            std::getline(std::cin, loc);
            searchByBloodGroupAndLocation(bg, loc);
        }
        else if (choice == 4) {
            int myPincode;
            std::cout << "Enter your current Pincode: ";
            std::cin >> myPincode;
            std::cin.ignore();
            findNearestDonors(myPincode);
        }
        else if (choice == 5) {
            std::cout << "Thank you for using Blood Donation Manager.\n";
        }
        else {
            std::cout << "Invalid choice. Try again.\n";
        }

    } while (choice != 5);

    return 0;
}
