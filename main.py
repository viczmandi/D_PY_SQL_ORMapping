__author__ = 'viczmandi'
import mysql.connector

class Customers():

    def __init__(self):
        self.CustomerID = ""
        self.ProductID = ""
        self.UnitPrice = ""
        self.Quantity = ""
        self.Discount = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""


    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        customer = Customers()
        customer.CustomerID = parsed_row[0]
        customer.ProductID = parsed_row[1]
        customer.UnitPrice = parsed_row[2]
        customer.Quantity = parsed_row[3]
        customer.Discount = parsed_row[4]
        customer.City = parsed_row[5]
        customer.Region = parsed_row[6]
        customer.PostalCode = parsed_row[7]
        customer.Region = parsed_row[8]
        customer.PostalCode = parsed_row[9]
        customer.Country = parsed_row[10]
        return customer


    @staticmethod
    def csv_reader(filename):
        file_rows = []
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                file_rows.append(line)
        return file_rows


    def persist(self):
        db = mysql.connector.connect(user="root", password="", host="localhost", database="proba")
        cursor = db.cursor()

        sql = "INSERT INTO `proba`.`customers` (`CustomerID`, `CompanyName`, `ContactName`, `ContactTitle`, `Address`, `City`, `Region`, `PostalCode`, `Country`, `Phone`, `Fax`) VALUES \
('" + self.CustomerID + "', '" + self.ProductID + "', '" + self.UnitPrice + "', '" + self.Quantity + "', '" + self.Discount + "', '" + self.City + "', '" + self.Region + "', '" + self.PostalCode + "', '" + self.Region + "', '" + self.PostalCode + "', '" + self.Country + "');"

        try:
           cursor.execute(sql)
           db.commit()
        except Exception as ex:
           print("Something went wrong: ", ex)
           db.rollback()
        db.close()

    def main_caller(self):
        csv_data = self.csv_reader("customers.csv")
        for i in range(len(csv_data)):
            customer = Customers.parse(csv_data[i])
            customer.persist()


class Employees():

    def __init__(self):
        self.EmployeeID = ""
        self.LastName = ""
        self.FirstName = ""
        self.Title = ""
        self.TitleOfCourtesy = ""
        self.BirthDate = ""
        self.HireDate = ""
        self.Address = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""
        self.HomePhone = ""
        self.Extension = ""
        self.Photo = ""
        self.Notes = ""
        self.ReportsTo = ""
        self.PhotoPath = ""
        self.Salary = ""


    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        employee = Employees()
        employee.EmployeeID = parsed_row[0]
        employee.LastName = parsed_row[1]
        employee.Title = parsed_row[2]
        employee.TitleOfCourtesy = parsed_row[3]
        employee.BirthDate = parsed_row[4]
        employee.HireDate = parsed_row[5]
        employee.Address = parsed_row[6]
        employee.City = parsed_row[7]
        employee.Region = parsed_row[8]
        employee.PostalCode = parsed_row[9]
        employee.Country = parsed_row[10]
        employee.HomePhone = parsed_row[11]
        employee.Extension = parsed_row[12]
        employee.Photo = parsed_row[13]
        employee.Notes = parsed_row[14]
        employee.ReportsTo = parsed_row[15]
        employee.PhotoPath = parsed_row[16]
        employee.Salary = parsed_row[17]
        return employee


    @staticmethod
    def csv_reader(filename):
        file_rows = []
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                file_rows.append(line)
        return file_rows


    def persist(self):
        db = mysql.connector.connect(user="root", password="", host="localhost", database="proba")
        cursor = db.cursor()

        sql = "INSERT INTO `proba`.`employees` (`EmployeeID`, `LastName`, `Title`, `TitleOfCourtesy`, " \
              "`BirthDate`, `HireDate`, `Address`, `City`, `Region`, `PostalCode`, `Country`, " \
              "`HomePhone`, `Extension`, `Photo`, `Notes`, `ReportsTo`, `PhotoPath`, `Salary`) VALUES \
('" + self.EmployeeID + "', '" + self.LastName + "', '" + self.Title + "', '" + self.TitleOfCourtesy + "', '" + self.BirthDate + "', '" + self.HireDate + "', '" + self.Address + "', '" + self.City + "', '" + self.Region + "', '" + self.PostalCode + "', '" + self.Country + "', '" + self.HomePhone + "', '" + self.Extension + "', '" + self.Photo + "', '" + self.Notes + "', '" + self.ReportsTo + "', '" + self.PhotoPath + "', '" + self.Salary + "');"

        try:
           cursor.execute(sql)
           db.commit()
        except Exception as ex:
           print("Something went wrong: ", ex)
           db.rollback()
        db.close()

    def main_caller(self):
        csv_data = self.csv_reader("employees.csv")
        for i in range(len(csv_data)):
            employee = Employees.parse(csv_data[i])
            employee.persist()


class Order_details():

    def __init__(self):
        self.OrderID = ""
        self.ProductID = ""
        self.UnitPrice = ""
        self.Quantity = ""
        self.Discount = ""



    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        order_detail = Order_details()
        order_detail.OrderID = parsed_row[0]
        order_detail.ProductID = parsed_row[1]
        order_detail.UnitPrice = parsed_row[2]
        order_detail.Quantity = parsed_row[3]
        order_detail.Discount = parsed_row[4]
        return order_detail


    @staticmethod
    def csv_reader(filename):
        file_rows = []
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                file_rows.append(line)
        return file_rows


    def persist(self):
        db = mysql.connector.connect(user="root", password="", host="localhost", database="proba")
        cursor = db.cursor()

        sql = "INSERT INTO `proba`.`order_details` (`OrderID`, `ProductID`, `UnitPrice`, `Quantity`, `Discount`) VALUES \
('" + self.OrderID + "', '" + self.ProductID + "', '" + self.UnitPrice + "', '" + self.Quantity + "', '" + self.Discount + "');"

        try:
           cursor.execute(sql)
           db.commit()
        except Exception as ex:
           print("Something went wrong: ", ex)
           db.rollback()
        db.close()

    def main_caller(self):
        csv_data = self.csv_reader("order_details.csv")
        for i in range(len(csv_data)):
            order_detail = Order_details.parse(csv_data[i])
            order_detail.persist()


class Orders():

    def __init__(self):
        self.OrderID = ""
        self.CustomerID = ""
        self.EmployeeID = ""
        self.ContactTitle = ""
        self.OrderDate = ""
        self.RequiredDate = ""
        self.ShippedDate = ""
        self.ShipVia = ""
        self.Freight = ""
        self.ShipName = ""
        self.ShipAddress = ""
        self.ShipCity = ""
        self.ShipRegion = ""
        self.ShipPostalCode = ""
        self.ShipCountry = ""


    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        order = Orders()
        order.OrderID = parsed_row[0]
        order.CustomerID = parsed_row[1]
        order.EmployeeID = parsed_row[2]
        order.ContactTitle = parsed_row[3]
        order.OrderDate = parsed_row[4]
        order.RequiredDate = parsed_row[5]
        order.ShippedDate = parsed_row[6]
        order.ShipVia = parsed_row[7]
        order.Freight = parsed_row[8]
        order.ShipName = parsed_row[9]
        order.ShipAddress = parsed_row[10]
        order.ShipCity = parsed_row[11]
        order.ShipRegion = parsed_row[12]
        order.ShipPostalCode = parsed_row[13]
        order.ShipCountry = parsed_row[14]
        return order


    @staticmethod
    def csv_reader(filename):
        file_rows = []
        with open(filename, "r", encoding="utf8") as f:
            for line in f:
                file_rows.append(line)
        return file_rows


    def persist(self):
        db = mysql.connector.connect(user="root", password="", host="localhost", database="proba")
        cursor = db.cursor()

        sql = "INSERT INTO `proba`.`orders` (`OrderID`, `CustomerID`, `EmployeeID`, `ContactTitle`, " \
              "`OrderDate`, `RequiredDate`, `ShippedDate`, `ShipVia`, `Freight`, `ShipName`, `ShipAddress`, " \
              "`ShipCity`, `ShipRegion`, `ShipPostalCode`, `ShipCountry`) VALUES \
('" + self.OrderID + "', '" + self.CustomerID + "', '" + self.ContactTitle + "', '" + self.OrderDate + "', '" + self.RequiredDate + "', '" + self.ShippedDate + "', '" + self.ShipVia + "', '" + self.Freight + "', '" + self.ShipName + "', '" + self.ShipAddress + "', '" + self.ShipCity + "', '" + self.ShipRegion + "', '" + self.ShipPostalCode + "', '" + self.ShipCountry + "');"

        try:
           cursor.execute(sql)
           db.commit()
        except Exception as ex:
           print("Something went wrong: ", ex)
           db.rollback()
        db.close()

    def main_caller(self):
        csv_data = self.csv_reader("orders.csv")
        for i in range(len(csv_data)):
            employee = Employees.parse(csv_data[i])
            employee.persist()


if __name__ == "__main__":
    proba = Customers()
    proba.main_caller()