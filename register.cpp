#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 7) {
        cout << "Invalid input. Usage: register.exe Name Age BloodGroup Location Pincode Phone\n";
        return 1;
    }

    string name = argv[1];
    string age = argv[2];
    string bloodGroup = argv[3];
    string location = argv[4];
    string pincode = argv[5];
    string phone = argv[6];

    ofstream file("donors.txt", ios::app);
    if (file.is_open()) {
        file << name << "," << age << "," << bloodGroup << "," << location << "," << pincode << "," << phone << "\n";
        file.close();
        cout << "Donor Registered Successfully!\n";
    } else {
        cout << "Error opening file.\n";
    }

    return 0;
}
