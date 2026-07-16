mysql_credentials = {
    'host': 'localhost',
    'user': 'root',
    'password' : 'newmee',
    'database' : 'car_damage_detection'
}
# config.py

# ===============================================================
# >> CENTRALIZED CAR PRICE DATA & HELPERS <<
# ===============================================================
CAR_PRICES_DATA = {
    
 "HONDA": {
        "City": {"Bonnet": 15000, "Bumper": 10000, "Dickey": 8000, "Door": 20000, "Fender": 5000, "Light": 3000, "Windshield": 8000},
        "Amaze": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6000, "Door": 18000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "WR-V": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "Jazz": {"Bonnet": 14000, "Bumper": 9000, "Dickey": 7000, "Door": 19000, "Fender": 4500, "Light": 2800, "Windshield": 8000},
        "HR-V": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Pilot": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "CR-V": {"Bonnet": 20000, "Bumper": 13000, "Dickey": 11000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Accord": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Civic": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000}
    },
    "MARUTI SUZUKI": {
        "Swift": {"Bonnet": 10000, "Bumper": 7000, "Dickey": 5000, "Door": 15000, "Fender": 3000, "Light": 2000, "Windshield": 6000},
        "Baleno": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6000, "Door": 18000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "Vitara Brezza": {"Bonnet": 14000, "Bumper": 9000, "Dickey": 7000, "Door": 20000, "Fender": 4500, "Light": 2800, "Windshield": 8000},
        "Wagon R": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6000, "Door": 18000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "Ertiga": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "Grand Vitara": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Dzire": {"Bonnet": 11000, "Bumper": 7500, "Dickey": 5500, "Door": 16000, "Fender": 3500, "Light": 2200, "Windshield": 6500},
        "Alto K10": {"Bonnet": 9000, "Bumper": 6000, "Dickey": 4500, "Door": 13000, "Fender": 2500, "Light": 1800, "Windshield": 5500},
        "Fronx": {"Bonnet": 13000, "Bumper": 8500, "Dickey": 6500, "Door": 19000, "Fender": 4200, "Light": 2600, "Windshield": 7500},
        "S-Presso": {"Bonnet": 8500, "Bumper": 5500, "Dickey": 4000, "Door": 12000, "Fender": 2200, "Light": 1600, "Windshield": 5000}
    },
    "TOYOTA": {
        "Corolla": {"Bonnet": 20000, "Bumper": 13000, "Dickey": 11000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Camry": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Fortuner": {"Bonnet": 25000, "Bumper": 17000, "Dickey": 15000, "Door": 30000, "Fender": 9000, "Light": 6000, "Windshield": 14000},
        "Innova": {"Bonnet": 23000, "Bumper": 16000, "Dickey": 14000, "Door": 29000, "Fender": 8500, "Light": 5500, "Windshield": 13000},
        "Yaris": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Urban Cruiser Hyryder": {"Bonnet": 17000, "Bumper": 11500, "Dickey": 9500, "Door": 23000, "Fender": 6500, "Light": 3750, "Windshield": 9500},
        "Urban Cruiser Taisor": {"Bonnet": 15000, "Bumper": 10000, "Dickey": 8000, "Door": 21000, "Fender": 5500, "Light": 3200, "Windshield": 8500}
    },
    "HYUNDAI": {
        "i20": {"Bonnet": 15000, "Bumper": 10000, "Dickey": 8000, "Door": 20000, "Fender": 5000, "Light": 3000, "Windshield": 8000},
        "Creta": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Verna": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "Venue": {"Bonnet": 17000, "Bumper": 11500, "Dickey": 9500, "Door": 23000, "Fender": 6500, "Light": 3750, "Windshield": 9500},
        "Tucson": {"Bonnet": 20000, "Bumper": 13000, "Dickey": 11000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Exter": {"Bonnet": 13500, "Bumper": 9000, "Dickey": 7000, "Door": 18500, "Fender": 4200, "Light": 2700, "Windshield": 7500},
        "Grand i10 Nios": {"Bonnet": 12500, "Bumper": 8500, "Dickey": 6500, "Door": 17000, "Fender": 3800, "Light": 2400, "Windshield": 7000}
    },
    "NISSAN": {
        "Altima": {"Bonnet": 18000, "Bumper": 13000, "Dickey": 11000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Rogue": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Sentra": {"Bonnet": 17000, "Bumper": 12000, "Dickey": 10000, "Door": 22000, "Fender": 6500, "Light": 3750, "Windshield": 9500},
        "Pathfinder": {"Bonnet": 18000, "Bumper": 13000, "Dickey": 11000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Titan": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Kicks": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 21000, "Fender": 6000, "Light": 3500, "Windshield": 8500},
        "X-Trail": {"Bonnet": 19000, "Bumper": 13500, "Dickey": 11500, "Door": 25000, "Fender": 7200, "Light": 4200, "Windshield": 10500}
    },
    "SKODA": {
        "Octavia": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Superb": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Rapid": {"Bonnet": 18000, "Bumper": 12000, "Dickey": 10000, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Kodiaq": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Karoq": {"Bonnet": 19000, "Bumper": 13500, "Dickey": 11500, "Door": 25000, "Fender": 7250, "Light": 4250, "Windshield": 10500},
        "Kushaq": {"Bonnet": 17000, "Bumper": 11500, "Dickey": 9500, "Door": 23000, "Fender": 6500, "Light": 3750, "Windshield": 9500},
        "Slavia": {"Bonnet": 18500, "Bumper": 12500, "Dickey": 10500, "Door": 24500, "Fender": 7200, "Light": 4200, "Windshield": 10200}
    },
    "TATA": {
        "Punch": {"Bonnet": 14000, "Bumper": 9500, "Dickey": 7500, "Door": 19000, "Fender": 4500, "Light": 2800, "Windshield": 8000},
        "Nexon": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "Harrier": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Safari": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Tiago": {"Bonnet": 11000, "Bumper": 7500, "Dickey": 5500, "Door": 16000, "Fender": 3500, "Light": 2200, "Windshield": 6500},
        "Altroz": {"Bonnet": 13000, "Bumper": 8500, "Dickey": 6500, "Door": 18000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "Tigor": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6000, "Door": 17000, "Fender": 3700, "Light": 2300, "Windshield": 6700},
        "Curvv": {"Bonnet": 18000, "Bumper": 12500, "Dickey": 10500, "Door": 24000, "Fender": 6800, "Light": 3900, "Windshield": 9800}
    },
    "MAHINDRA": {
        "Scorpio N": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "XUV700": {"Bonnet": 24000, "Bumper": 16000, "Dickey": 14000, "Door": 30000, "Fender": 8500, "Light": 5500, "Windshield": 13000},
        "Thar": {"Bonnet": 18000, "Bumper": 12500, "Dickey": 10500, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "XUV 3XO": {"Bonnet": 15000, "Bumper": 10000, "Dickey": 8000, "Door": 20000, "Fender": 5500, "Light": 3200, "Windshield": 8500},
        "Bolero": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 21000, "Fender": 6000, "Light": 3500, "Windshield": 8800},
        "Scorpio Classic": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Marazzo": {"Bonnet": 19000, "Bumper": 13000, "Dickey": 11000, "Door": 25000, "Fender": 7200, "Light": 4200, "Windshield": 10500},
        "Thar ROXX": {"Bonnet": 19000, "Bumper": 13000, "Dickey": 11000, "Door": 25000, "Fender": 7200, "Light": 4200, "Windshield": 10500}
    },
    "KIA": {
        "Sonet": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "Seltos": {"Bonnet": 18000, "Bumper": 12500, "Dickey": 10500, "Door": 24000, "Fender": 7000, "Light": 4000, "Windshield": 10000},
        "Carens": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Carnival": {"Bonnet": 28000, "Bumper": 19000, "Dickey": 16000, "Door": 35000, "Fender": 10000, "Light": 6500, "Windshield": 15000},
        "EV6": {"Bonnet": 25000, "Bumper": 17000, "Dickey": 14000, "Door": 32000, "Fender": 9000, "Light": 6000, "Windshield": 14000},
        "Syros": {"Bonnet": 17000, "Bumper": 11500, "Dickey": 9500, "Door": 23000, "Fender": 6500, "Light": 3750, "Windshield": 9500}
    },
    "MG MOTOR": {
        "Hector": {"Bonnet": 19000, "Bumper": 13000, "Dickey": 11000, "Door": 25000, "Fender": 7200, "Light": 4200, "Windshield": 10500},
        "Astor": {"Bonnet": 16000, "Bumper": 11000, "Dickey": 9000, "Door": 22000, "Fender": 6000, "Light": 3500, "Windshield": 9000},
        "ZS EV": {"Bonnet": 20000, "Bumper": 14000, "Dickey": 12000, "Door": 26000, "Fender": 7500, "Light": 4500, "Windshield": 11000},
        "Gloster": {"Bonnet": 26000, "Bumper": 18000, "Dickey": 15000, "Door": 33000, "Fender": 9500, "Light": 6200, "Windshield": 14500},
        "Comet EV": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6500, "Door": 17000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "Windsor EV": {"Bonnet": 18000, "Bumper": 12500, "Dickey": 10500, "Door": 24000, "Fender": 6800, "Light": 3900, "Windshield": 9800}
    },
    "RENAULT": {
        "Kwid": {"Bonnet": 9000, "Bumper": 6000, "Dickey": 4500, "Door": 13000, "Fender": 2800, "Light": 1800, "Windshield": 5500},
        "Triber": {"Bonnet": 12000, "Bumper": 8000, "Dickey": 6000, "Door": 17000, "Fender": 4000, "Light": 2500, "Windshield": 7000},
        "Kiger": {"Bonnet": 14000, "Bumper": 9500, "Dickey": 7500, "Door": 19000, "Fender": 5000, "Light": 3000, "Windshield": 8000},
        "Duster": {"Bonnet": 17000, "Bumper": 12000, "Dickey": 10000, "Door": 23000, "Fender": 6500, "Light": 3800, "Windshield": 9500}
    },
    "JEEP": {
        "Compass": {"Bonnet": 22000, "Bumper": 15000, "Dickey": 13000, "Door": 28000, "Fender": 8000, "Light": 5000, "Windshield": 12000},
        "Meridian": {"Bonnet": 25000, "Bumper": 17000, "Dickey": 14500, "Door": 31000, "Fender": 8800, "Light": 5500, "Windshield": 13500},
        "Wrangler": {"Bonnet": 35000, "Bumper": 25000, "Dickey": 20000, "Door": 42000, "Fender": 12000, "Light": 8000, "Windshield": 18000},
        "Grand Cherokee": {"Bonnet": 38000, "Bumper": 27000, "Dickey": 22000, "Door": 45000, "Fender": 13000, "Light": 8500, "Windshield": 20000}
    },
    "BMW": {
        "2 Series": {"Bonnet": 45000, "Bumper": 32000, "Dickey": 25000, "Door": 55000, "Fender": 15000, "Light": 10000, "Windshield": 25000},
        "3 Series": {"Bonnet": 50000, "Bumper": 35000, "Dickey": 28000, "Door": 60000, "Fender": 18000, "Light": 12000, "Windshield": 28000},
        "5 Series": {"Bonnet": 60000, "Bumper": 42000, "Dickey": 35000, "Door": 70000, "Fender": 22000, "Light": 15000, "Windshield": 35000},
        "7 Series": {"Bonnet": 80000, "Bumper": 55000, "Dickey": 45000, "Door": 90000, "Fender": 28000, "Light": 18000, "Windshield": 45000},
        "X1": {"Bonnet": 45000, "Bumper": 32000, "Dickey": 25000, "Door": 55000, "Fender": 16000, "Light": 10000, "Windshield": 25000},
        "X3": {"Bonnet": 55000, "Bumper": 38000, "Dickey": 30000, "Door": 65000, "Fender": 20000, "Light": 13000, "Windshield": 30000},
        "X5": {"Bonnet": 70000, "Bumper": 48000, "Dickey": 40000, "Door": 80000, "Fender": 25000, "Light": 16000, "Windshield": 38000},
        "X7": {"Bonnet": 85000, "Bumper": 60000, "Dickey": 50000, "Door": 95000, "Fender": 30000, "Light": 20000, "Windshield": 48000}
    },
    "MERCEDES-BENZ": {
        "A-Class": {"Bonnet": 42000, "Bumper": 30000, "Dickey": 24000, "Door": 52000, "Fender": 15000, "Light": 9500, "Windshield": 24000},
        "C-Class": {"Bonnet": 50000, "Bumper": 35000, "Dickey": 28000, "Door": 60000, "Fender": 18000, "Light": 12000, "Windshield": 28000},
        "E-Class": {"Bonnet": 65000, "Bumper": 45000, "Dickey": 38000, "Door": 75000, "Fender": 23000, "Light": 15000, "Windshield": 38000},
        "S-Class": {"Bonnet": 90000, "Bumper": 62000, "Dickey": 50000, "Door": 100000, "Fender": 32000, "Light": 20000, "Windshield": 50000},
        "GLA": {"Bonnet": 45000, "Bumper": 32000, "Dickey": 25000, "Door": 55000, "Fender": 16000, "Light": 10000, "Windshield": 25000},
        "GLC": {"Bonnet": 55000, "Bumper": 38000, "Dickey": 30000, "Door": 65000, "Fender": 20000, "Light": 13000, "Windshield": 30000},
        "GLE": {"Bonnet": 70000, "Bumper": 48000, "Dickey": 40000, "Door": 80000, "Fender": 25000, "Light": 16000, "Windshield": 38000},
        "GLS": {"Bonnet": 85000, "Bumper": 60000, "Dickey": 50000, "Door": 95000, "Fender": 30000, "Light": 20000, "Windshield": 48000}
    },
    "AUDI": {
        "A3": {"Bonnet": 40000, "Bumper": 28000, "Dickey": 22000, "Door": 50000, "Fender": 14000, "Light": 9000, "Windshield": 22000},
        "A4": {"Bonnet": 48000, "Bumper": 34000, "Dickey": 27000, "Door": 58000, "Fender": 17000, "Light": 11000, "Windshield": 27000},
        "A6": {"Bonnet": 60000, "Bumper": 42000, "Dickey": 35000, "Door": 70000, "Fender": 22000, "Light": 14000, "Windshield": 35000},
        "A8": {"Bonnet": 80000, "Bumper": 55000, "Dickey": 45000, "Door": 90000, "Fender": 28000, "Light": 18000, "Windshield": 45000},
        "Q3": {"Bonnet": 42000, "Bumper": 30000, "Dickey": 24000, "Door": 52000, "Fender": 15000, "Light": 9500, "Windshield": 24000},
        "Q5": {"Bonnet": 52000, "Bumper": 36000, "Dickey": 29000, "Door": 62000, "Fender": 19000, "Light": 12000, "Windshield": 29000},
        "Q7": {"Bonnet": 68000, "Bumper": 47000, "Dickey": 38000, "Door": 78000, "Fender": 24000, "Light": 15500, "Windshield": 38000},
        "Q8": {"Bonnet": 75000, "Bumper": 52000, "Dickey": 42000, "Door": 85000, "Fender": 26000, "Light": 17000, "Windshield": 42000}
    }
}

def get_part_name_from_id(class_id):
    """Maps a YOLO class ID to a part name string."""
    class_names = ['Bonnet', 'Bumper', 'Dickey', 'Door', 'Fender', 'Light', 'Windshield']
    if 0 <= class_id < len(class_names):
        return class_names[int(class_id)]
    return None