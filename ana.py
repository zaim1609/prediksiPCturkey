import pickle

model = pickle.load(open("modelfix.pkl", "rb"))

y_pred = model.predict([[512.0,0,0,0,16.0,0,48,7,2,7,5]])

nilai = y_pred[0] * 550
print("Harga prediksi dalam TL:", y_pred[0])
print("Harga prediksi dalam Rupiah (IDR):", round(nilai))