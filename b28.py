# ------------------ Medical Prescription Logic ------------------
def prescribe_medication(symptoms, age):
    age_group = "adult" if age >= 18 else "child"

    medication_rules = {
        "cold": {
            "adult": {
                "primary": ("Cetirizine", "10mg", "at bedtime", "Drowsiness"),
                "alternate": ("Levocetirizine", "5mg", "at bedtime", "Dry mouth"),
                "home_remedy": "Steam inhalation and warm fluids"
            },
            "child": {
                "primary": ("Saline nasal drops", "2 drops", "per nostril", "None"),
                "alternate": ("Steam inhalation", "—", "under supervision", "None"),
                "home_remedy": "Honey (if age > 1), warm soups"
            }
        },
        "cough": {
            "adult": {
                "primary": ("Dextromethorphan syrup", "10ml", "twice daily", "Drowsiness, dry mouth"),
                "alternate": ("Bromhexine syrup", "10ml", "twice daily", "Nausea, headache"),
                "home_remedy": "Steam inhalation and honey with warm water"
            },
            "child": {
                "primary": ("Honey + warm water", "1 tsp", "twice daily", "None if age > 1"),
                "alternate": ("Ambroxol syrup", "5ml", "twice daily", "Mild stomach upset"),
                "home_remedy": "Warm fluids and rest"
            }
        },
        "fever": {
            "adult": {
                "primary": ("Paracetamol", "500mg", "every 6 hours", "Nausea, rash, liver strain"),
                "alternate": ("Ibuprofen", "400mg", "every 8 hours", "Stomach upset, dizziness"),
                "home_remedy": "Cold compress and hydration"
            },
            "child": {
                "primary": ("Paracetamol syrup", "15ml", "every 6 hours", "Mild rash, drowsiness"),
                "alternate": ("Ibuprofen syrup", "10ml", "every 8 hours", "Stomach irritation"),
                "home_remedy": "Lukewarm sponge bath and fluids"
            }
        },
        "constipation": {
            "adult": {
                "primary": ("Lactulose syrup", "15ml", "at bedtime", "Bloating, gas"),
                "alternate": ("Isabgol husk", "1 tbsp", "once daily", "Flatulence"),
                "home_remedy": "High-fiber diet, warm water, and regular exercise"
            },
            "child": {
                "primary": ("Lactulose syrup", "5–10ml", "at bedtime", "Mild cramps"),
                "alternate": ("Glycerin suppository", "1 unit", "as needed", "Rectal irritation"),
                "home_remedy": "Fruits like papaya, hydration, and gentle movement"
            }
        },
        "skill issue": {
            "adult": {
                "primary": ("Vitamin B-complex", "1 tablet", "daily", "Mild nausea"),
                "alternate": ("Ginkgo biloba", "60mg", "twice daily", "Headache, dizziness"),
                "home_remedy": "Sleep hygiene, meditation, and mental exercises"
            },
            "child": {
                "primary": ("Multivitamin syrup", "10ml", "daily", "Sweet taste, mild nausea"),
                "alternate": ("Omega-3 supplements", "As advised", "daily", "Fishy aftertaste"),
                "home_remedy": "Brain games, structured routine, and sleep"
            }
        },
        "jaundice": {
            "adult": {
                "primary": ("Supportive care", "—", "—", "Depends on cause"),
                "alternate": ("Liver tonics", "As prescribed", "daily", "Rare: nausea"),
                "home_remedy": "Sugarcane juice, boiled vegetables, and rest"
            },
            "child": {
                "primary": ("Phototherapy", "—", "—", "Skin dryness"),
                "alternate": ("Supportive care", "—", "—", "Monitor bilirubin levels"),
                "home_remedy": "Breastfeeding, hydration, and pediatric follow-up"
            }
        },
        "periods": {
            "adult": {
                "primary": ("Mefenamic acid", "250mg", "every 8 hours", "Stomach upset"),
                "alternate": ("Ibuprofen", "400mg", "every 6 hours", "Drowsiness"),
                "home_remedy": "Warm compress, yoga, and herbal teas"
            },
            "child": {
                "primary": ("Paracetamol", "500mg", "as needed", "Mild rash"),
                "alternate": ("Consult pediatric gynecologist", "", "", ""),
                "home_remedy": "Rest, hydration, and gentle exercise"
            }
        },
        "cancer": {
            "adult": {
                "primary": ("Refer to oncologist", "", "", "Depends on treatment"),
                "alternate": ("Supportive care", "", "", "Fatigue, nausea"),
                "home_remedy": "Emotional support, balanced diet, and rest"
            },
            "child": {
                "primary": ("Specialist referral", "", "", "Depends on treatment"),
                "alternate": ("Pediatric oncology support", "", "", "Fatigue, nausea"),
                "home_remedy": "Family care, play therapy, and nutrition"
            }
        },
        "aids": {
            "adult": {
                "primary": ("Antiretroviral therapy (ART)", "As prescribed", "daily", "Fatigue, nausea"),
                "alternate": ("CD4 monitoring", "—", "regular intervals", "None"),
                "home_remedy": "Nutritious diet, hygiene, and stress reduction"
            },
            "child": {
                "primary": ("Pediatric ART", "As prescribed", "daily", "Fatigue, nausea"),
                "alternate": ("Immune boosters", "—", "daily", "None"),
                "home_remedy": "Clean environment and emotional support"
            }
        },
        "diarrhea": {
            "adult": {
                "primary": ("ORS solution", "200ml", "after each loose stool", "None"),
                "alternate": ("Racecadotril", "100mg", "twice daily", "Abdominal pain"),
                "home_remedy": "Banana, rice, and hydration"
            },
            "child": {
                "primary": ("ORS solution", "100ml", "after each episode", "None"),
                "alternate": ("Zinc syrup", "5ml", "daily for 10 days", "Metallic taste"),
                "home_remedy": "Rice water, mashed banana, and fluids"
            }
        },
        "bodyache": {
            "adult": {
                "primary": ("Diclofenac", "50mg", "twice daily", "Gastric irritation"),
                "alternate": ("Naproxen", "250mg", "twice daily", "Dizziness, nausea"),
                "home_remedy": "Warm bath and rest"
            },
            "child": {
                "primary": ("Paracetamol syrup", "15ml", "twice daily", "Mild rash"),
                "alternate": ("Rest + hydration", "", "", ""),
                "home_remedy": "Gentle massage and fluids"
            }
        },
        "sore throat": {
            "adult": {
                "primary": ("Lozenges", "1 unit", "every 3 hours", "Mouth irritation"),
                "alternate": ("Chlorhexidine mouthwash", "10ml", "twice daily", "Taste alteration"),
                "home_remedy": "Warm saline gargles"
            },
            "child": {
                "primary": ("Honey + warm water", "1 tsp", "twice daily", "None if age > 1"),
                "alternate": ("Salt water gargles", "—", "if age > 5", "Mild discomfort"),
                "home_remedy": "Warm fluids and rest"
            }
        },
        "headache": {
            "adult": {
                "primary": ("Ibuprofen", "400mg", "once daily", "Stomach upset"),
                "alternate": ("Acetaminophen", "500mg", "twice daily", "Liver strain"),
                "home_remedy": "Cold compress and hydration"
            },
            "child": {
                "primary": ("Acetaminophen syrup", "10ml", "as needed", "Mild rash"),
                "alternate": ("Consult pediatrician", "", "", ""),
                "home_remedy": "Quiet rest and fluids"
            }
        }
        # Add more symptoms as needed...
    }

    prescription = []

    for symptom in symptoms:
        symptom = symptom.lower()
        if symptom in medication_rules:
            data = medication_rules[symptom][age_group]
            p_med, p_dose, p_freq, p_side = data["primary"]
            a_med, a_dose, a_freq, a_side = data["alternate"]
            remedy = data["home_remedy"]

            prescription.append(
                f"{symptom.title()}:\n"
                f"  - Primary Medication: {p_med} ({p_dose}, {p_freq})\n"
                f"    • Side Effects: {p_side}\n"
                f"  - Alternate Medication: {a_med} ({a_dose}, {a_freq})\n"
                f"    • Side Effects: {a_side}\n"
                f"  - Home Remedy: {remedy}"
            )
        else:
            prescription.append(f"{symptom.title()}: No rule found. Please consult a specialist.")

    return prescription
def main():
    print("🩺 Welcome to the Medical Prescription Assistant")
    try:
        age = int(input("Enter patient's age: "))
        symptoms_input = input("Enter symptoms (comma-separated): ")
        symptoms = [s.strip() for s in symptoms_input.split(",") if s.strip()]

        if not symptoms:
            print("⚠ No symptoms provided. Please enter at least one.")
            return

        prescriptions = prescribe_medication(symptoms, age)

        print("\n📋 Prescription Summary:")
        for item in prescriptions:
            print(item)
            print("-" * 50)

    except ValueError:
        print("Invalid input. Age must be a number.")

if _name_ == "_main_":
    main()
