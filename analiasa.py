from flask import Flask, request, render_template
import joblib
import pickle
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import numpy as np
import sklearn

print(sklearn.__version__)

app = Flask(__name__)

# load model
model = pickle.load(open("modelfix.pkl", "rb"))


processors = {
    'AMD': 0, 'AMD Ryzen 3': 1, 'AMD Ryzen 5': 2, 'AMD Ryzen 7': 3, 'AMD Ryzen 9': 4,
    'Apple M1': 5, 'Intel Core i3': 6, 'Intel Core i5': 7, 'Intel Core i7': 8, 'Intel Core i9': 9,
    'Intel Pentium': 10, 'Intel Xeon': 11, 'M2': 12, 'nan': 13
}

graphic_cards = {
    'AMD CPU Entegre Grafik': 0, 'AMD Radeon Graphics': 1, 'AMD Radeon R5': 2, 'AMD Radeon R7 240': 3,
    'Intel HD Graphics': 13, 'Nvidia GeForce GTX 1650': 26, 'Nvidia GeForce RTX 3050': 32, 'nan': 50
}

memory_types = {
    'Belirtilmemiş': 0, 'DDR': 1, 'DDR2 + DDR3': 2, 'DDR3': 3, 'DDR4': 4, 'DDR5': 5, 
    'Dahili': 6, 'GDDR5': 7, 'GDDR5X': 8, 'GDDR6': 9, 'GDDR6X': 10, 'SD': 11, 'nan': 12
}

card_types = {
    'Belirtilmemiş': 0, 'Dahili': 1, 'Harici': 2, 'nan': 3
}

brands = {
    'ACER': 0, 'ARTITEKNİKPC': 1, 'ASUS': 2, 'Apple': 3, 'Avantron': 4, 'CASPER': 5, 'Canar': 6, 
    'ColdPower': 7, 'Corsair': 8, 'DAGMOR': 9, 'DMC': 10, 'Dell': 11, 'EFS TEKNOLOJİ': 12, 
    'GAMELİNE': 13, 'Gamepage': 14, 'Gaming Game': 15, 'Gigabyte': 16, 'Grundig': 17, 
    'Güneysu Gaming': 18, 'HP': 19, 'IZOLY': 20, 'Jedi': 21, 'LENOVO': 22, 'Life Teknoloji': 23, 
    'METSA': 24, 'MSI': 25, 'OEM': 26, 'OXpower': 27, 'Oksid Bilişim Teknoloji': 28, 'PCDEPO': 29, 
    'Quadro': 30, 'Quantum Gaming': 31, 'RAMTECH': 32, 'ROGAME': 33, 'RaXius': 34, 'Redrock': 35, 
    'Revenge': 36, 'Rexdragon': 37, 'SECLIFE': 38, 'Super': 39, 'TOPLAMA': 40, 'TRİNİTY': 41, 
    'TURBOX': 42, 'Technopc': 43, 'Tiranozor': 44, 'Tiwox': 45, 'UCARTECH': 46, 'WARBOX': 47, 
    'XASER': 48, 'Zeiron': 49, 'Zetta': 50, 'jetucuzal': 51
};

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        # Get selected options from the dropdown
        merek = request.form.get("dropdownInput")
        processor = request.form.get("processor")
        graphic_card = request.form.get("graphic_card")
        memory_type = request.form.get("memory_type")
        card_type = request.form.get("card_type")  # ← lebih aman pakai .get()
        ghz = request.form.get("ghz")
        islemci_frekansi = request.form.get("islemci_frekansi")
        Ram = request.form.get("Ram")
        arttiri = request.form.get("arttiri")
        ssd = request.form.get("ssd")
        ekran = request.form.get("ekran")
        
        if processor and graphic_card and memory_type and card_type:
            processor_num = processors.get(processor, -1)
            graphic_card_num = graphic_cards.get(graphic_card, -1)
            memory_type_num = memory_types.get(memory_type, -1)
            card_type_num = card_types.get(card_type, -1)
            
            # Create a feature vector (make sure all features are numeric)
            features = np.array([processor_num, graphic_card_num, memory_type_num, card_type_num, 
                                 float(ghz), float(islemci_frekansi), float(Ram), float(arttiri), 
                                 float(ssd), float(ekran)])
            
            print(features)
            
            # Make the prediction using the model
            # prediction = model.predict([features])[0]  # Assuming a regression model
            
            # hasil = f"Hasil prediksi: {prediction:.2f} (Predicted Value)"

    return render_template("index.html",processors=processors, 
                           graphic_cards=graphic_cards, 
                           memory_types=memory_types, 
                           card_types=card_types, hasil=hasil)
