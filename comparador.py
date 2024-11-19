import cv2
import fingerprint_feature_extractor
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

image_path1 = r'C:\Users\joaov\Desktop\db\106_3(1).tif'
image_path2 = r'C:\Users\joaov\Desktop\db\106_5(1).tif'

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Image not found at {image_path}")
    return image

def extract_features(image):
    # Extrai as características de minutiae
    FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(image, invertImage=True)
    return FeaturesTerminations + FeaturesBifurcations

def clean_features(features):
    # Extrai apenas o endereço hexadecimal e converte para inteiro
    return [int(re.search(r'0x[0-9A-Fa-f]+', str(item)).group(), 16) for item in features]

def pad_arrays_to_same_length(arr1, arr2):
    max_len = max(len(arr1), len(arr2))
    arr1_padded = np.pad(arr1, (0, max_len - len(arr1)), 'constant')
    arr2_padded = np.pad(arr2, (0, max_len - len(arr2)), 'constant')
    return arr1_padded, arr2_padded

def compare_features(features1, features2):
    # Converte listas para arrays e preenche até o mesmo comprimento
    features1_array, features2_array = pad_arrays_to_same_length(
        np.array(features1), np.array(features2)
    )
    # Ajusta a dimensão para 2D para uso com cosine_similarity
    features1_array = features1_array.reshape(1, -1)
    features2_array = features2_array.reshape(1, -1)
    similarities = cosine_similarity(features1_array, features2_array)
    return np.max(similarities)

def main(image_path1, image_path2):
    # Processa a primeira imagem
    image1 = preprocess_image(image_path1)
    features1 = extract_features(image1)
    features1_clean = clean_features(features1)

    # Processa a segunda imagem
    image2 = preprocess_image(image_path2)
    features2 = extract_features(image2)
    features2_clean = clean_features(features2)

    # Compara as features das duas imagens
    similarity = compare_features(features1_clean, features2_clean)

    # Avalia o nível de similaridade e exibe o resultado
    if similarity > 0.9999:  # Ajustar limiar conforme necessário
        print(f"Acesso permitido com nível de similaridade: {similarity}")
        print(features1_clean)
    else:
        print("Acesso negado")

# Executa a função principal com os dois caminhos de imagem
main(image_path1, image_path2)
