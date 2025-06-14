import celestial_sandbox.types.celestial_body.star


ELifecycleStage = celestial_sandbox.types.celestial_body.star.EStarLifecycleStage


def calculate_star_type(mass, temperature, stage, radius):
    # Convert radius from km to solar radii
    radius = radius / 696340

    if stage == ELifecycleStage.PRE_MAIN_SEQUENCE:
        if mass <= 2 and radius >= 0.5 and radius <= 2:
            return 'T_Tauri_Star'
        elif mass > 2 and radius > 2 and radius <= 5:
            return 'Herbig_AE_BE_Star'
    elif stage == ELifecycleStage.MAIN_SEQUENCE:
        if mass <= 0.08 and temperature <= 3000:
            return 'Subdwarf'
        elif mass <= 0.5 and temperature <= 3700:
            return 'Red_Dwarf'
        elif mass > 0.5 and mass <= 0.8 and temperature > 3700 and temperature <= 5200:
            return 'Orange_Dwarf'
        elif mass > 0.8 and mass <= 1.4 and temperature > 5200 and temperature <= 6000:
            return 'Yellow_Dwarf'
        elif mass > 15 and temperature > 30000:
            return 'O_Type_Star'
    elif stage == ELifecycleStage.POST_MAIN_SEQUENCE:
        if radius > 1.5 and radius <= 5:
            return 'Subgiant'
        elif radius > 5 and radius <= 100:
            return 'Red_Giant'
        elif radius > 100:
            return 'Red_Supergiant'
    elif stage == ELifecycleStage.SUPERGIANT:
        if mass > 15 and mass <= 25 and radius > 600:
            return 'Blue_Supergiant'
        elif mass > 25 and temperature > 30000:
            return 'Hypergiant'
    elif stage == ELifecycleStage.FINAL_STAGE:
        if mass <= 1.4:
            return 'White_Dwarf'
        elif mass > 1.4 and mass <= 3:
            return 'Neutron_Star'
        elif mass > 3:
            return 'Stellar_Black_Hole'
    elif stage == ELifecycleStage.FAILED_STAR:
        return 'Brown_Dwarf'
    
    return 'Unknown Star Type'



# T Tauri Star
print(calculate_star_type(0.5, 3000, ELifecycleStage.PRE_MAIN_SEQUENCE, 1.5 * 696340))  # V1057 Cyg

# Herbig AE BE Star
print(calculate_star_type(2.5, 10000, ELifecycleStage.PRE_MAIN_SEQUENCE, 2.5 * 696340))  # HD 163296

# Red Dwarf
print(calculate_star_type(0.3, 3000, ELifecycleStage.MAIN_SEQUENCE, 0.3 * 696340))  # Proxima Centauri

# Orange Dwarf
print(calculate_star_type(0.7, 5000, ELifecycleStage.MAIN_SEQUENCE, 0.7 * 696340))  # 61 Cygni A

# Yellow Dwarf
print(calculate_star_type(1, 5778, ELifecycleStage.MAIN_SEQUENCE, 696340))  # Our Sun

# O Type Star
print(calculate_star_type(16, 40000, ELifecycleStage.MAIN_SEQUENCE, 7 * 696340))  # Zeta Ophiuchi

# Subgiant
print(calculate_star_type(1.1, 5500, ELifecycleStage.POST_MAIN_SEQUENCE, 2 * 696340))  # Beta Hydri

# Red Giant
print(calculate_star_type(0.8, 3500, ELifecycleStage.POST_MAIN_SEQUENCE, 50 * 696340))  # Aldebaran

# Red Supergiant
print(calculate_star_type(12, 3500, ELifecycleStage.POST_MAIN_SEQUENCE, 600 * 696340))  # Betelgeuse

# Blue Supergiant
print(calculate_star_type(20, 20000, ELifecycleStage.SUPERGIANT, 700 * 696340))  # Rigel

# Hypergiant
print(calculate_star_type(30, 35000, ELifecycleStage.SUPERGIANT, 1300 * 696340))  # Eta Carinae

# White Dwarf
print(calculate_star_type(0.6, 8000, ELifecycleStage.FINAL_STAGE, 0.01 * 696340))  # Sirius B

# Neutron Star
print(calculate_star_type(1.4, 6000000, ELifecycleStage.FINAL_STAGE, 10))  # PSR J0108-1431

# Stellar Black Hole
print(calculate_star_type(10, 0, ELifecycleStage.FINAL_STAGE, 0))  # Cygnus X-1

# Brown Dwarf
print(calculate_star_type(0.05, 1700, ELifecycleStage.FAILED_STAR, 0.1 * 696340))  # WISE 0855−0714
