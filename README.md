# Vaccine Management System
This Python-based Vaccine Management System is designed to efficiently manage vaccine stocks, track storage room capacities, and ensure that vaccines are stored at their required temperatures. The system simplifies inventory functions such as adding new vaccines, checking stock levels, updating storage, and preventing overstocking. It also provides features for easy sorting, filtering, and removing stock, all within a user-friendly interface.

## Features
* Add New Vaccine : The system automatically assigns vaccines to appropriate storage rooms based on temperature requirements and checks if there’s enough storage capacity before adding them.

* View and Manage Stocks: A comprehensive table displays all available vaccines, including critical details like batch number, expiry date, stock levels, and required storage temperatures.

* Sorting and Filtering:
    * Sorting: Sort vaccines by expiry date or stock levels to prioritize usage.
    * Filtering: Filter vaccines by type (bacteria/virus) or by storage temperature for easy management.

* Update Vaccine Stock: Easily increase or decrease the stock of any vaccine. The system ensures that storage room limits aren’t exceeded and that the stock isn’t reduced below zero.

* Delete Vaccine: Remove a vaccine from the system, and the storage room’s capacity is automatically adjusted accordingly.

## How It Works
* Storage Room Assignment: When a new vaccine is added, the system searches for a storage room that meets the required temperature and has enough available capacity. If no room fits these criteria, the user is notified, and the vaccine cannot be added.

* Capacity Management: Whenever stock is added or removed, the system dynamically updates the used storage capacity. This ensures that rooms don’t exceed their limits, preventing overstocking or wastage.

* Dynamic Updates: Stock levels can be adjusted up or down, with the system automatically updating the available space in each storage room. The system also prevents invalid actions, such as trying to reduce stock below zero or exceeding room capacity.

## Flowchart
To better understand the system's workflow, here's the Vaccine Management System Flowchart:

### Main Menu
[alt text](https://github.com/syarifaahk/Capstone-Module-1/blob/8e4a4bddcbcd7c26c67ffb7098273af5043f95b2/Flowchart%20Capstone%20Module_Main%20Menu.jpg)

### Create Menu
[alt text](https://github.com/syarifaahk/Capstone-Module-1/blob/8e4a4bddcbcd7c26c67ffb7098273af5043f95b2/Flowchart%20Capstone%20Module_Create%20Menu.jpg)

### Read Menu
[alt text](https://github.com/syarifaahk/Capstone-Module-1/blob/8e4a4bddcbcd7c26c67ffb7098273af5043f95b2/Flowchart%20Capstone%20Module_Read%20Menu.jpg)

### Update Menu
[alt text](https://github.com/syarifaahk/Capstone-Module-1/blob/8e4a4bddcbcd7c26c67ffb7098273af5043f95b2/Flowchart%20Capstone%20Module_Update%20Menu.jpg)

### Delete Menu
[alt text](https://github.com/syarifaahk/Capstone-Module-1/blob/8e4a4bddcbcd7c26c67ffb7098273af5043f95b2/Flowchart%20Capstone%20Module_Delete%20Menu.jpg)


## 🎉 Wrapping Up!
Thank you for exploring the Vaccine Management System! I hope you found it as helpful as I did while building it. Feel free to clone, explore, and even improve the code—contributions are always welcome!

A huge shout-out to Purwadhika Digital Technology School for providing an amazing opportunity to grow and learn in the world of data science and machine learning. 🙌

Happy coding! 🚀


Name                : Syarifah Khaerunnisa
Capstone Module 1   : Programming Fundamental
Purwadhika DTI      : Data Science and Machine Learning
Lecturer            : Ilham Candra

