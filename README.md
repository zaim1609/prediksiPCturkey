Pipeline PC price prediction in turkey

i use dataset from kaggle under title "", at that dataset there all about pc component from processor until monitor, but in this case i only using pc without the monitor, i use several label like "Marka: Brand of the computer (e.g., XASER, DMC, HP, Dell)

Fiyat: Selling price of the computer (in TL)

İşlemci Tipi: Processor brand and model (e.g., Intel Core i5, AMD Ryzen 7)

SSD Kapasitesi: SSD storage capacity (e.g., 256 GB, 512 GB)

Ram (Sistem Belleği): Memory capacity (e.g., 8 GB, 16 GB, 32 GB)

Ekran Kartı: Graphics card model in the computer

Ekran Kartı Kapasitesi: Memory capacity of the graphics card (e.g., 4 GB, 8 GB)

İşletim Sistemi: Pre-installed operating system (e.g., Windows, Free DOS)

Ekran Kartı Bellek Tipi: Memory type of the graphics card (e.g., DDR3, GDDR5)

Ekran Kartı Tipi: Whether the graphics card is dedicated or integrated

Ekran Kartı Hafızası: GPU memory size (e.g., 4 GB, 8 GB)

Temel İşlemci Hızı: Base clock speed of the processor (GHz)

Bağlantılar: Connection options such as HDMI, DisplayPort

Cihaz Ağırlığı: Total weight of the computer

Ekran Boyutu: Monitor screen size (e.g., 24 inches, 27 inches)

İşlemci Frekansı: Processor speed frequency (e.g., above 3.00 GHz)

Ekran Yenileme Hızı: Monitor screen refresh rate (e.g., 75 Hz, 165 Hz)

Panel Tipi: Panel type such as VA, IPS, TN

Menşei: Country of manufacture

Arttırılabilir Azami Bellek: Maximum expandable memory capacity"


firts step i learn about a data seeking about sum off null knowing data dissemination and etc. after that i put several label like "Marka",
    "Fiyat",
    "İşlemci Tipi",
    "Temel İşlemci Hızı (GHz)",
    "İşlemci Frekansı",
    "Ram (Sistem Belleği)",
    "Arttırılabilir Azami Bellek",
    "SSD Kapasitesi",
    "Ekran Kartı",
    "Ekran Kartı Hafızası",
    "Ekran Kartı Tipi",
    "Ekran Kartı Bellek Tipi"
next we preprocessing data we use regular expression to erase string or simbol in data type number and make a categorical data to number by encode the data, fill in blank data by mean after all data is ready we drop fiyat(currentcy in turkey) 
for Maintains the consistency of data points i did standard scaler to data befor i spilt to 20% data test and 80% data train, i comparing some linear model like 
linear reggression
Ridge
lasso
ElasticNet
DecisionTreeRegressor
RandomForestRegessor
GradientBosstingRegreesor
HistGradientBoostingRegressor
KNeighborsRegressor
XGBRegressor
LGBMRegressor
we use r2 for comparing perfomance from all model and we got Gradient boosting model is the best model with R2 score 0.78/1 after we got the best model we save that model and using it for making pc price prediction website
now you just input the all of form and you can predict the pc price
