from features import extract_features


url = input("Enter URL: ")

features = extract_features(url)

print("\nExtracted Features")
print("=" * 40)

for name, value in features.items():
    print(f"{name:25} : {value}")
