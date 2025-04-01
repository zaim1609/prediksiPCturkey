import kagglehub

# Download latest version
path = kagglehub.dataset_download("cabbar14ylnce/computer-price-prediction")

print("Path to dataset files:", path)