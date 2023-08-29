import DBG

def print_menu():
    print("********************************")
    print("*    Menú de Garage Database   *")
    print("********************************")
    print("1. Mostrar todos los vehículos")
    print("2. Buscar vehículo por ID")
    print("3. Buscar vehículos por marca")
    print("4. Buscar vehículos por modelo")
    print("5. Buscar vehículos por año")
    print("6. Buscar vehículos por numero de placa")
    print("7. Buscar vehículos por nombre del propietario")
    print("8. Buscar vehículos por apellido del propietario")
    print("9. Buscar vehículos por direccion")
    print("10. Buscar vehículos por numero de telefono")
    print("11. Añadir un coche")
    print("12. Borrar un coche por ID")
    print("13. Modificar un coche")
    # Agregar más opciones aquí según las funciones que quieras implementar
    print("0. Salir")
    print("********************************")

def main():

    while True:
        print_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            vehicles = DBG.get_all_vehicles()
            print("\nTodos los vehículos:")
            for vehicle in vehicles:
                print(vehicle)
        elif choice == "2":	#ID
            vehicle_id = int(input("Ingrese el ID del vehículo: "))
            vehicle = DBG.get_vehicle_by_id(vehicle_id)
            if vehicle:
                print("\nInformación del vehículo:")
                print(vehicle)
            else:
                print("\nVehículo no encontrado.")
        elif choice == "3":	#BRAND
            brand = input("Ingrese la marca del vehículo: ")
            vehicles = DBG.get_vehicle_by_brand(brand)
            if vehicles:
                print("\nVehículos de la marca:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos de esa marca.")
        elif choice == "4":	#MODEL
            model = input("Ingrese la modelo del vehículo: ")
            vehicles = DBG.get_vehicle_by_model(model)
            if vehicles:
                print("\nVehículos de la modelo:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos de ese modelo.")
        elif choice == "5":	#YEAR
            year = input("Ingrese el año del vehículo: ")
            vehicles = DBG.get_vehicle_by_brand(year)
            if vehicles:
                print("\nVehículos del año:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos de ese año.")
        elif choice == "6":	#PLATE
            plate_number = input("Ingrese la placa del vehículo: ")
            vehicles = DBG.get_vehicle_by_plate_number(plate_number)
            if vehicles:
                print("\nVehículos de la placa:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos de esa placa.")
        elif choice == "7":	#Owners name
            owner_last_name = input("Ingrese la nombre del propietario del vehículo: ")
            vehicles = DBG.get_vehicle_by_owner_first_name(owner_last_name)
            if vehicles:
                print("\nVehículos a su nombre:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos con ese nombre de propietario.")
        elif choice == "8":	#Ownoers Lastname
            owner_last_name = input("Ingrese el apellido propietario del vehículo: ")
            vehicles = DBG.get_vehicle_by_owner_last_name(owner_last_name)
            if vehicles:
                print("\nVehículos a su apellido:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos con un propietario con es apellido.")
        elif choice == "9":	#ADDRESS
            owner_address = input("Ingrese la direccion del vehículo: ")
            vehicles = DBG.get_vehicle_by_owner_address(owner_adress)
            if vehicles:
                print("\nVehículos de la direccion:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos con esa direccion.")
        elif choice == "10":	#PHONE
            owner_phone = input("Ingrese el numero de telefono del propietario del vehículo: ")
            vehicles = DBG.get_vehicle_by_owner_phone(owner_phone)
            if vehicles:
                print("\nVehículos con el numero asociado:")
                for vehicle in vehicles:
                    print(vehicle)
            else:
                print("\nNo se encontraron vehículos con ese numero asociado.")
        elif choice == "11":	#Añadir
            brand = input("Ingrese la marca del vehículo: ")
            model = input("Ingrese la modelo del vehículo: ")
            year = input("Ingrese el año del vehículo: ")
            plate_number = input("Ingrese la placa del vehículo: ")
            owner_first_name = input("Ingrese la nombre del propietario del vehículo: ")
            owner_last_name = input("Ingrese el apellido propietario del vehículo: ")
            owner_address = input("Ingrese la direccion del vehículo: ")
            owner_phone = input("Ingrese el numero de telefono del propietario del vehículo: ")      
            DBG.add_vehicle(brand, model, year, plate_number, owner_first_name, owner_last_name, owner_address, owner_phone)
            vehicles = DBG.get_all_vehicles()
        elif choice == "12":
            vehicle_id = int(input("Ingrese el ID del vehículo a borrar: "))
            garage_db.delete_vehicle_by_id(vehicle_id)
            print("Vehículo borrado exitosamente.")
        elif choice == "13":
            print("Introduzca el ID del coche a modificar")
            vehicles = DBG.get_all_vehicles()
            for vehicle in vehicles:
                print(vehicle)
            ID = input("ID: ")
            vehicle = DBG.get_vehicle_by_id(ID)
            print(vehicle)
                        
            while True:
                print("Que caractiristica quiere cambiar?")
                print("1. marca")
                print("2. modelo")
                print("3. año")
                print("4. placa")
                print("5. nombre del propietario")
                print("6. apellido del propietario")
                print("7. direccion")
                print("8. numero de telefono")
                print("0. Salir")            
            
                cambio = input("Seleccione una opción: ")
                
                if cambio == "1":
                    brand = input("Marca del vehiculo: ")
                    DBG.update_vehicle_brand_by_id(ID ,brand)
                elif cambio == "2":
                    model = input("Modelo del vehiculo: ")
                    DBG.update_vehicle_model_by_id(ID ,model)
                elif cambio == "3":
                    year = input("Año del vehiculo: ")
                    DBG.update_vehicle_year_by_id(ID ,year)
                elif cambio == "4":
                    plate_number = input("Placa del vehiculo: ")
                    DBG.update_vehicle_plate_number_by_id(ID ,plate_number)
                elif cambio == "5":
                    owner_first_name = input("Nombre del propietario del vehiculo: ")
                    DBG.update_vehicle_owner_first_name_by_id(ID ,owner_first_name)
                elif cambio == "6":
                    owner_last_name = input("Apellido del propietario del vehiculo: ")
                    DBG.update_vehicle_owner_last_name_by_id(ID ,owner_last_name)
                elif cambio == "7":
                    address = input("Direccion del vehiculo: ")
                    DBG.update_vehicle_owner_address_by_id(ID ,address)
                elif cambio == "8":
                    phone_number = input("Telefono del vehiculo: ")
                    DBG.update_vehicle_phone_number_by_id(ID ,phone_number)    
                elif cambio == "0":
                    print("Saliendo")
                    break
            
                print("Vehículo editado exitosamente:")
                vehicle = DBG.get_vehicle_by_id(ID)            
                print(vehicle)
                
            
        elif choice == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

