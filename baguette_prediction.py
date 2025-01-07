import os
import sys
import random
import numpy as np
import skimage.io
import matplotlib.pyplot as plt
from mrcnn import utils
from mrcnn import visualize
import mrcnn.model as modellib
from baguette import BaguetteConfig, BaguetteDataset

# Configuration du chemin vers le dossier contenant les poids et les images de test
MODEL_DIR = "C:\\Object Detection\\logs"
WEIGHTS_PATH = "C:\\Object Detection\\logs\\mask_rcnn_baguette_0004.h5"
TEST_IMAGE_DIR = "C:\\Object Detection\\dataset\\test"

# Configurer la classe de configuration pour le mode inference
class InferenceConfig(BaguetteConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()

# Initialiser le modèle en mode inference
model = modellib.MaskRCNN(mode="inference", config=config, model_dir=MODEL_DIR)

# Charger les poids réentraînés
print("Chargement des poids du modèle à partir de :", WEIGHTS_PATH)
model.load_weights(WEIGHTS_PATH, by_name=True)

# Initialiser l'ensemble de données de test
dataset_test = BaguetteDataset()
dataset_test.load_baguette("C:\\Object Detection\\dataset\\", "val")
dataset_test.prepare()

# Fonction pour tester sur une image spécifique et afficher les résultats
def test_on_image(image_path):
    # Charger l'image
    image = skimage.io.imread(image_path)

    # Effectuer la détection
    results = model.detect([image], verbose=1)
    r = results[0]

    # Afficher les résultats
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                                dataset_test.class_names, r['scores'])

# Calculer le mAP moyen sur l'ensemble de test
def evaluate_model(dataset, model, config):
    APs = []

    for image_id in dataset.image_ids:
        # Charger l'image et ses annotations
        image, image_meta, gt_class_id, gt_bbox, gt_mask = modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)
        molded_images = np.expand_dims(modellib.mold_image(image, config), 0)

        # Exécuter la détection
        results = model.detect([image], verbose=0)
        r = results[0]

        # Calculer Average Precision (AP)
        AP, precisions, recalls, overlaps = utils.compute_ap(gt_bbox, gt_class_id, gt_mask,
                                                             r["rois"], r["class_ids"], r["scores"], r['masks'])
        APs.append(AP)

    print("mAP moyen sur l'ensemble de test: ", np.mean(APs))

# Tester le modèle sur une image unique
dirs=os.listdir(TEST_IMAGE_DIR)
for file in dirs:
    if not "annotations2.json" in file :
        test_image_path =os.path.join(TEST_IMAGE_DIR, file)
        test_on_image(test_image_path)
#test_image_path =os.path.join(TEST_IMAGE_DIR, random.choice(os.listdir(TEST_IMAGE_DIR)))
#test_on_image(test_image_path)

# Évaluer le modèle sur l'ensemble de test
#evaluate_model(dataset_test, model, config)

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# def compute_confusion_matrix(dataset, model, config):
    # y_true = []
    # y_pred = []

    # for image_id in dataset.image_ids:
        # Charger l'image et ses vraies classes
        # image, _, gt_class_id, _, _ = modellib.load_image_gt(dataset, config, image_id, use_mini_mask=False)

        # Effectuer la détection
        # results = model.detect([image], verbose=0)
        # r = results[0]

        # Ajouter les vraies classes et les prédictions dans les listes
        # y_true.extend(gt_class_id)
        # y_pred.extend(r['class_ids'])

    # Créer la matrice de confusion
    # cm = confusion_matrix(y_true, y_pred)
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=dataset.class_names, yticklabels=dataset.class_names)
    # plt.xlabel("Prédictions")
    # plt.ylabel("Vérité Terrain")
    # plt.title("Matrice de Confusion")
    # plt.show()

# Appeler la fonction
#compute_confusion_matrix(dataset_test, model, config)
