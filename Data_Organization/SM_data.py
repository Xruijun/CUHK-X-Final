import os
from pathlib import Path
import pandas as pd
import re

base_path = Path("SM_data/RGB_final")
output_file = "SM_data_new.xlsx"

def extract_user_number(user_name: str) -> int:
    """Extract numeric part from user folder like 'user6' → 6"""
    match = re.search(r"\d+", user_name)
    return int(match.group()) if match else float("inf")

def extract_sublevel_numbers(sublevel_name: str):
    """Extract numbers from sublevel name like '1-1-1' → (1,1,1)"""
    nums = re.findall(r"\d+", sublevel_name)
    return tuple(map(int, nums)) if nums else (float("inf"),)

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    # Iterate over actions
    for action_dir in base_path.iterdir():
        if action_dir.is_dir():
            action_name = action_dir.name
            rows = []

            # Iterate over users inside the action
            for user_dir in action_dir.iterdir():
                if user_dir.is_dir():
                    user_name = user_dir.name

                    # Iterate over sublevels inside the user
                    for sublevel_dir in user_dir.iterdir():
                        if sublevel_dir.is_dir():
                            sublevel_name = sublevel_dir.name
                            rows.append({
                                "User": user_name,
                                "User_num": extract_user_number(user_name),
                                "Sublevel": sublevel_name,
                                "Sublevel_nums": extract_sublevel_numbers(sublevel_name),
                            })

            if rows:
                df = pd.DataFrame(rows)

                # Sort by user number, then sublevel tuple
                df = df.sort_values(by=["User_num", "Sublevel_nums"], ascending=[True, True])

                # Drop helper columns
                df = df.drop(columns=["User_num", "Sublevel_nums"])

                # Write sheet (Excel sheet names max 31 chars)
                df.to_excel(writer, sheet_name=action_name[:31], index=False)
                print(f"✅ Added sorted sheet '{action_name}' with {len(df)} entries.")

print(f"\n📁 All actions saved into {output_file}")
