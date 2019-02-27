import pickle
favorites=['лада','седан','баклажан','опа']
save_file = open('favorites.dat', 'wb')
pickle.dump(favorites, save_file)
save_file.close()

load_file = open('favorites.dat', 'rb')
loaded_favorites = pickle.load(load_file)
load_file.close()
print(loaded_favorites)
