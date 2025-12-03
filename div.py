import os
import random
import shutil

# caminho para a pasta onde tens as 4 classes
TRAIN_DIR = "Training"

# nomes das classes (iguais às pastas)
CLASSES = ["glioma", "meningioma", "notumor", "pituitary"]

# novas pastas a criar
LABELED_DIR = "labeled_pool"
UNLABELED_DIR = "unlabeled_pool"

# quantas imagens por classe queres no labeled_pool
N_LABELED_PER_CLASS = 20   # podes mudar este valor

# se True copia, se False move (eu recomendo copiar para não estragar o original)
COPY_FILES = True

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    # criar estrutura de pastas
    for base in [LABELED_DIR, UNLABELED_DIR]:
        for cls in CLASSES:
            ensure_dir(os.path.join(base, cls))

    for cls in CLASSES:
        class_dir = os.path.join(TRAIN_DIR, cls)
        files = [f for f in os.listdir(class_dir)
                 if os.path.isfile(os.path.join(class_dir, f))]

        random.shuffle(files)

        labeled_files = files[:N_LABELED_PER_CLASS]
        unlabeled_files = files[N_LABELED_PER_CLASS:]

        print(f"Classe {cls}: {len(labeled_files)} labeled, {len(unlabeled_files)} unlabeled")

        # copiar/mover para labeled_pool
        for f in labeled_files:
            src = os.path.join(class_dir, f)
            dst = os.path.join(LABELED_DIR, cls, f)
            if COPY_FILES:
                shutil.copy2(src, dst)
            else:
                shutil.move(src, dst)

        # copiar/mover para unlabeled_pool
        for f in unlabeled_files:
            src = os.path.join(class_dir, f)
            dst = os.path.join(UNLABELED_DIR, cls, f)
            if COPY_FILES:
                shutil.copy2(src, dst)
            else:
                shutil.move(src, dst)

if __name__ == "__main__":
    main()
