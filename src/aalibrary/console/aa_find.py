from aalibrary.ices_ship_names import get_all_ices_ship_names


        
        
def main():
    
    all_ship_names = get_all_ices_ship_names(normalize_ship_names=True)
    for ship_name in all_ship_names:
        if "lasker" in ship_name.lower():
            print(ship_name)

if __name__ == "__main__":
    main()